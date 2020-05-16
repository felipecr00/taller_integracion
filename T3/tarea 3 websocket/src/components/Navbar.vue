<template>
  <div>
    <md-toolbar class="md" md-elevation="1">
      <h1 class="md-title" style="flex: 1"><b>Socket Trading</b></h1>
      <md-button
        class="md-primary"
        @click="disconnect"
        v-if="status === 'connected'"
        >Desconectar</md-button
      >
      <md-button @click="connect" v-if="status === 'disconnected'"
        >Conectar</md-button
      >
      <!-- <md-button>Conectar</md-button>
      <md-button class="md-primary">Desconectar</md-button> -->
    </md-toolbar>
  </div>
</template>

<style lang="scss" scoped>
.md-toolbar + .md-toolbar {
  margin-top: 16px;
}
</style>

<script>
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'Navbar',
  data: function() {
    return {
      message: 'desde el content',
      status: 'connected',
    };
  },
  computed: {
    ...mapState(['connection']),
  },
  methods: {
    ...mapMutations(['SET_CONNECTION']),
    connect() {
      this.status = 'connected';
      this.SET_CONNECTION(this.status);
    },
    disconnect() {
      this.status = 'disconnected';
      this.SET_CONNECTION(this.status);
    },
  },
};
</script>
