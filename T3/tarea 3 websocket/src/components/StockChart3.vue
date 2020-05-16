<template>
  <div class="small2" ref="volume" :id="id"></div>
</template>

<script>
import { createChart } from 'lightweight-charts';
import { mapState } from 'vuex';

export default {
  name: 'StockChart3',
  components: {},
  props: ['id'],
  data() {
    return {
      inserted: new Set(),
    };
  },
  created() {},
  computed: {
    ...mapState(['buySellData']),
  },
  mounted() {
    const chart = createChart(document.querySelector('#' + this.id), {});
    this.lineSeries = chart.addHistogramSeries();
  },
  methods: {
    fillData(fetchedData) {
      let array = this.id.split('_');

      if (fetchedData['ticker'] === array[0]) {
        //console.log('entra aca');
        //console.log(fetchedData);
        if (fetchedData['tipo'] === 'BUY') {
          this.lineSeries.update({
            time: fetchedData['time'],
            value: fetchedData['volume'],
            color: 'rgba(255,82,82, 0.8)',
          });
        } else {
          this.lineSeries.update({
            time: fetchedData['time'],
            value: fetchedData['volume'],
            color: 'rgba(0, 150, 136, 0.8)',
          });
        }
      }
    },
  },
  watch: {
    buySellData: function() {
      this.buySellData.forEach((i) => {
        const { ticker, time } = i;
        if (!this.inserted.has(ticker + time + '')) {
          this.fillData(i);
          this.inserted.add(ticker + time + '');
        }
      });
      //console.log('watch', this.stockData)
    },
  },
};
</script>
<style>
.small2 {
  padding-left: 10px;
  margin: 10px;
  flex: 1;
  min-height: 300px;
}
#volume {
  height: 300px;
  width: 420px;
  display: inline-flex;
}
</style>
