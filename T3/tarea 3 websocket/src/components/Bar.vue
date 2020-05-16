<template>
  <infinite-slide-bar duration="25s">
    <div class="items">
      <div
        v-for="ticker in tickerData"
        :key="ticker"
      >
        <div class="f-left pd-t-8px mg-r-10px">
          <b-icon-graph-up class="icon-size"></b-icon-graph-up>
        </div>
        <div class="f-left">
          <div class=""><b>{{tickerInfo[ticker]['name']}}</b></div>
          <div>
            {{tickerInfo[ticker]['alto']}} USD
            <span :class="{ 'success': tickerInfo[ticker]['variacion'] > 0, 'danger': tickerInfo[ticker]['variacion'] < 0 }">

              ({{tickerInfo[ticker]['variacion']}}%)
            </span>
          </div>
        </div>
      </div>
    </div>
  </infinite-slide-bar>
</template>

<script>

import { mapState } from 'vuex';
import InfiniteSlideBar from 'vue-infinite-slide-bar'

export default {
  name: 'Stock',

  data() {
    return {
      // stocks: [
      //   { id: 'act1' },
      //   { id: 'act2' },
      //   { id: 'act3' },
      //   { id: 'act4' },
      //   { id: 'act5' },
      //   { id: 'act6' },
      //   { id: 'act7' },
      // ]
    };
  },
  components: {
    InfiniteSlideBar
    //StockChart2,
  },
  computed: {
    ...mapState(['tickerData']),
    ...mapState(['tickerInfo']),
  },

  methods: {},
};
</script>

<style lang="scss" scoped>
.items {
  display: flex;
  justify-content: space-around;
}
.icon-size {
  font-size: 50px;
  margin-bottom: 7px;
}
.success {
  color: green;
}
.danger {
  color: red;
}
</style>
