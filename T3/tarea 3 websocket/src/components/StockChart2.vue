<template>
  <div class="small" ref="hola" :id="id"></div>
</template>

<script>
import { createChart } from 'lightweight-charts';
import { mapState } from 'vuex';

export default {
  name: 'StockChart',
  components: {},
  props: ['id'],
  data() {
    return {
      inserted: new Set(),
    };
  },
  created() {},
  computed: {
    ...mapState(['stockData']),
  },
  mounted() {
    const chart = createChart(document.querySelector('#' + this.id), {});
    this.lineSeries = chart.addLineSeries();
  },
  methods: {
    fillData(fetchedData) {
      if (fetchedData['ticker'] === this.id) {
        //console.log('entra aca');
        this.lineSeries.update({
          time: fetchedData['time'],
          value: fetchedData['value'],
        });
      }
    },
  },
  watch: {
    stockData: function() {
      this.stockData.forEach((i) => {
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
.small {
  padding-left: 10px;
  margin: 10px;
  flex: 1;
  min-height: 300px;
}
#hola {
  height: 300px;
  width: 420px;
  display: inline-flex;
}
</style>
