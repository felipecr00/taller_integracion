<template>
  <div class="small">
    <line-chart :chart-data="datacollection" id="mychart"></line-chart>
  </div>
</template>

<script>
import LineChart from '../LineChart.js';
import io from 'socket.io-client';
var socket = io.connect('wss://le-18262636.bitzonte.com', {
  path: '/stocks',
});

export default {
  name: 'StockChart',
  components: {
    LineChart,
  },
  data() {
    return {
      datacollection: {},
    };
  },
  created() {
    this.getRealtimeData();
  },
  methods: {
    fillData(fetchedData) {
      console.log('entra aca');
      if (fetchedData['ticker'] === 'AAPL') {
        this.datacollection = {
          labels: [fetchedData['value'], fetchedData['time']],
          datasets: [
            {
              label: fetchedData['ticker'],
              backgroundColor: '#1A73E8',
              data: [fetchedData['value'], fetchedData['time']],
            },
          ],
        };
      }
    },
    getRealtimeData() {
      socket.on('UPDATE', (fetchedData) => {
        this.fillData(fetchedData);
      });
    },
  },
};
</script>
<style>
.small {
  max-width: 400px;
  margin: 100px auto;
}
</style>
