<template>
  <b-container
    fluid
    class="trade mt-4"
  >
    <h2>{{ msg }}</h2>
    <h2>{{ connection }}</h2>
    <Bar style="margin-top:50px" />
    <b-container
      fluid
      class="section-header"
      style="margin-top:70px"
    >
      <h2><b>Información de mercados en línea</b></h2>

    </b-container>

    <b-container class="section-header">
      <div class="text-header">
        <h5>La plataforma de negociación de <b>Socket Trading</b> le permite negociar acciones de todos los mercados populares como Estados Unidos y más,
          con apalancamiento y márgenes bajos. Utilizando nuestras herramientas avanzadas de visualización, usted también puede controlar sus ganancias y pérdidas.</h5>
      </div>
    </b-container>

    <Stock />
    <Volume class="mt-4" />
    <b-container
      fluid
      class="section-header mt-4 mb-4"
    >
      <h2 style="margin-top:70px"><b>Mercado de valores</b></h2>

    </b-container>
    <b-container class="section-header">
      <div class="text-header">
        <h5>Acceso instantáneo al Mercado de valores (Exchanges), en cualquier momento y en cualquier lugar.
          Invertir nunca ha sido tan fácil. Todo lo que buscas en una plataforma de inversión definitiva — en el dispositivo de tu elección.</h5>
      </div>
    </b-container>
    <Exchange style="justify-content:center; margin-bottom:100px" />
  </b-container>
</template>

<script>
import { mapState } from 'vuex';
import Stock from './Stock';
import Volume from './Volume';
import Exchange from './Exchange';
import Bar from './Bar'


export default {
  name: 'Trade',
  data() {
    return {
      msg: 'Tarea 3',
      description1: ''
    };
  },
  components: {
    Stock,
    Exchange,
    Volume,
    Bar,
  },
  computed: {
    ...mapState(['connection']),
  },
  methods: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.text-header {
  margin-top: 50px;
  margin-bottom: 80px;
  display: inline;
}

.text-header h5 {
  font-weight: 40;
}
.section-header {
  display: flex;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
