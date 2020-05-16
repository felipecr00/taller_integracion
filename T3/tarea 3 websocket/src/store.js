import Vue from 'vue';
import Vuex from 'vuex';
import io from 'socket.io-client';

var socket = io.connect('wss://le-18262636.bitzonte.com', {
  path: '/stocks',
});

Vue.use(Vuex);

let update_stock = (infoStock, value) => {
  if (infoStock['alto'] <= value) {
    infoStock['alto'] = value;
  }
  if (infoStock['bajo'] >= value) {
    infoStock['bajo'] = value;
  }
  infoStock['variacion'] = (
    (100 * (infoStock['ultimo'] - value)) /
    infoStock['ultimo']
  ).toFixed(2);
  infoStock['ultimo'] = value;
};

let update_volume = (infoVol, value, echangeData, exchangeInfo) => {
  if (value['tipo'] === 'BUY') {
    infoVol['compra'] = infoVol['compra'] + value['volume'];
    update_exchange(
      echangeData,
      exchangeInfo,
      value['volume'],
      'BUY',
      infoVol['name']
    );
  }

  if (value['tipo'] === 'SELL') {
    infoVol['venta'] = infoVol['venta'] + value['volume'];
    update_exchange(
      echangeData,
      exchangeInfo,
      value['volume'],
      'SELL',
      infoVol['name']
    );
  }
  infoVol['total'] = infoVol['total'] + value['volume'];
};

let update_exchange = (echangeData, exchangeInfo, value, tipo, name) => {
  echangeData.forEach((ex) => {
    console.log(name);
    if (exchangeInfo[ex]['lista_empresas'].includes(name)) {
      if (tipo === 'BUY') {
        exchangeInfo[ex]['compra'] = value + exchangeInfo[ex]['compra'];
      }
      if (tipo === 'SELL') {
        exchangeInfo[ex]['venta'] = value + exchangeInfo[ex]['venta'];
      }

      exchangeInfo[ex]['total'] = value + exchangeInfo[ex]['total'];
    }
  });
  let total_object = {};
  let total_both = 0;
  echangeData.forEach((ex) => {
    total_object[ex] = exchangeInfo[ex]['total'];
    total_both = total_both + exchangeInfo[ex]['total'];
  });

  echangeData.forEach((ex) => {
    exchangeInfo[ex]['participacion'] = (
      100 *
      (total_object[ex] / total_both)
    ).toFixed(2);
  });
};

const store = new Vuex.Store({
  state: {
    title: 'holiowi',
    connection: 'connected',
    stockData: [],
    buySellData: [],
    sellData: [],
    tickerData: [],
    exchangeData: [],
    exchangeInfo: {},
    tickerInfo: {},
    tickers: ['AAPL', 'FB', 'SNAP'],
  },
  mutations: {
    SET_CONNECTION: (state, connection) => {
      state.connection = connection;
      if (state.connection === 'connected') {
        socket.disconnect();
        socket = io.connect('wss://le-18262636.bitzonte.com', {
          path: '/stocks',
        });
        socket.on('UPDATE', (fetchedData) => {
          store.commit('ADD_DATA', fetchedData);
          update_stock(
            state.tickerInfo[fetchedData['ticker']],
            fetchedData['value']
          );
        });
        socket.on('BUY', (fetchedData) => {
          let buyD = fetchedData;
          buyD['tipo'] = 'BUY';
          store.commit('ADD_BUY', buyD);
          update_volume(
            state.tickerInfo[fetchedData['ticker']],
            buyD,
            state.exchangeData,
            state.exchangeInfo
          );
          //update_exchange(state.exchangeData, state.exchangeInfo, buyD);
        });
        socket.on('SELL', (fetchedData) => {
          let sellD = fetchedData;
          sellD['tipo'] = 'SELL';
          store.commit('ADD_BUY', sellD);
          update_volume(
            state.tickerInfo[fetchedData['ticker']],
            sellD,
            state.exchangeData,
            state.exchangeInfo
          );
          //update_exchange(state.exchangeData, state.exchangeInfo, sellD);
        });
      } else {
        socket.disconnect();
      }
    },
    SET_EXCHANGE: (state, exchangeData) => {
      state.exchangeData = exchangeData;
    },
    ADD_EXCHANGE_INFO: (state, exchangeData) => {
      state.exchangeInfo = exchangeData;
    },
    SET_TICKER: (state, tickerData) => {
      state.tickerData = tickerData;
    },
    ADD_TICKER_INFO: (state, tickerInfo) => {
      state.tickerInfo = tickerInfo;
    },
    SET_TICKER_INFO: (state, ticker, k, v) => {
      state.tickerInfo[ticker][k] = v;
    },
    ADD_DATA: (state, data) => {
      state.stockData = [...state.stockData, data];
    },
    ADD_BUY: (state, data) => {
      state.buySellData = [...state.buySellData, data];
    },
  },
  actions: {},
});

socket.emit('STOCKS');
socket.once('STOCKS', (data) => {
  let stocks = [];
  let ticker_object = {};
  //console.log(data);
  for (let st in data) {
    stocks = [...stocks, data[st]['ticker']];
    ticker_object[data[st]['ticker']] = {
      alto: 0,
      bajo: Infinity,
      ultimo: 0,
      variacion: 0,
      name: data[st]['company_name'],
      country: data[st]['country'],
      compra: 0,
      venta: 0,
      total: 0,
    };
  }
  store.commit('SET_TICKER', stocks);
  store.commit('ADD_TICKER_INFO', ticker_object);
});

socket.emit('EXCHANGES');
socket.once('EXCHANGES', (data) => {
  const exchanges = Object.keys(data);
  let exchange_object = {};
  exchanges.forEach((entry) => {
    exchange_object[entry] = {
      lista_empresas: data[entry]['listed_companies'],
      compra: 0,
      venta: 0,
      total: 0,
      cantidad: 0,
      participacion: 0,
    };
  });
  //console.log(exchange_object);
  store.commit('SET_EXCHANGE', exchanges);
  store.commit('ADD_EXCHANGE_INFO', exchange_object);
  store.commit('SET_CONNECTION', 'connected');
});

export default store;
