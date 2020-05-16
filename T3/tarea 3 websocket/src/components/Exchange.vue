<template>

  <div class="scroll md-scrollbar">
    <md-card
      v-for="id in exchangeData"
      :key="id"
      class="mr-4"
    >
      <md-card-area>

        <md-card-header>
          <h1>
            <b-icon-bar-chart-fill></b-icon-bar-chart-fill>
          </h1>

          <div class="md-title"><b>{{ id }}</b></div>
        </md-card-header>

        <md-card-content>
          <h4>Información de mercado</h4>
        </md-card-content>

        <md-card-content>
          <h5>Volumen Compra: <b-badge variant="danger">{{exchangeInfo[id]['compra']}}</b-badge>
          </h5>
          <h5>Volumen Venta: <b-badge variant="success">{{exchangeInfo[id]['venta']}}</b-badge>
          </h5>
          <h5>Volumen Total: <b-badge variant="dark">{{exchangeInfo[id]['total']}}</b-badge>
          </h5>
          <h5>Cantidad de Acciones: <b-badge variant="light">{{exchangeInfo[id]['lista_empresas'].length}}</b-badge>
          </h5>
          <h5>Participación de Mercado: <b-badge variant="warning">{{exchangeInfo[id]['participacion']}}%</b-badge>
          </h5>
        </md-card-content>

      </md-card-area>
    </md-card>
  </div>

</template>

<script>
// import StockChart2 from './StockChart2.vue';
import { mapState } from 'vuex';

export default {
  name: 'Exchange',

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
    // StockChart2,
  },
  computed: {
    ...mapState(['exchangeData']),
    ...mapState(['exchangeInfo'])
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
