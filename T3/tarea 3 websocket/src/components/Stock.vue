<template>
  <div class="scroll md-scrollbar">
    <md-card
      v-for="id in tickerData"
      :key="id"
      class="mr-4"
    >
      <md-card-area>
        <md-card-media>
          <StockChart2 :id="id" />
        </md-card-media>
        <md-card-header>
          <div class="md-title">
            <b>{{ id }}</b>
            <p style="font-size:15px">{{tickerInfo[id]['name']}}</p>
            <h6>País: {{tickerInfo[id]['country']}}</h6>
          </div>
        </md-card-header>
        <md-card-content>
          <h4>Información de la acción</h4>
        </md-card-content>

        <md-card-content>
          <h5>
            Alto Histórico:
            <b-badge variant="primary">{{ tickerInfo[id]['alto'] }}</b-badge>
          </h5>

          <h5>
            Bajo Histórico:
            <b-badge variant="primary">{{ tickerInfo[id]['bajo'] }}</b-badge>
          </h5>

          <h5>
            Último Precio:
            <b-badge variant="dark">{{ tickerInfo[id]['ultimo'] }}</b-badge>
          </h5>

          <h5>
            Variación Porcentual:

            <b-badge
              variant="danger"
              v-if="tickerInfo[id]['variacion'] <= 0"
            >{{ tickerInfo[id]['variacion'] }}%</b-badge>

            <b-badge
              variant="success"
              v-else
            >{{ tickerInfo[id]['variacion'] }}%</b-badge>
          </h5>
        </md-card-content>
      </md-card-area>
    </md-card>
  </div>
</template>

<script>
import StockChart2 from './StockChart2.vue';
import { mapState } from 'vuex';

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
    StockChart2,
  },
  computed: {
    ...mapState(['tickerData']),
    ...mapState(['tickerInfo']),
  },

  methods: {},
};
</script>

<style lang="scss" scoped>
li {
  list-style-type: none;
}

.scroll {
  display: flex;
  flex-direction: row;
  vertical-align: top;
  overflow-x: auto !important;
  background-color: #fff;
  min-width: 100%;
  min-height: 200px;
  padding: 10px;
  padding-left: 50px;
  padding-right: 50px;
}
.md-card {
  min-width: 420px;
  margin: 4px;
  overflow: auto;
  display: inline-block;
  vertical-align: top;
  flex-direction: row;
}

.md-card-example {
  .md-subhead {
    .md-icon {
      $size: 16px;

      width: $size;
      min-width: $size;
      height: $size;
      font-size: $size !important;
    }

    span {
      vertical-align: middle;
    }
  }

  .card-reservation {
    margin-top: 8px;
    display: flex;
    align-items: center;
    justify-content: space-between;

    .md-icon {
      margin: 8px;
    }
  }

  .md-button-group {
    display: flex;

    .md-button {
      min-width: 60px;
      border-radius: 2px;
    }
  }
}
::-webkit-scrollbar {
  -webkit-appearance: none;
  width: 7px;
}

::-webkit-scrollbar-thumb {
  border-radius: 4px;
  background-color: rgba(0, 0, 0, 0.5);
  box-shadow: 0 0 1px rgba(255, 255, 255, 0.5);
}
</style>
