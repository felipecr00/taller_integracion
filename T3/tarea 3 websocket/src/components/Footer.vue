<template>
  <div
    id="Footer"
    class="scrollspy"
  >
    <div class="container">
      <div class="row">
        <div class="col s12 ">
          <h3 class="center-align">
            Tareita de Taller de Integración
          </h3>

        </div>
      </div>
      <div
        id="social"
        class="col l3"
      />
    </div>
    <div class="container">
      <h5
        class="center-align"
        style="color:white"
      >
        © 2020 Felipe Cornejo Rivas
      </h5>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Footer',

  data() {
    return {
      medias: [
        {
          logo: '',
          link: '',
        }, {
          logo: '',
          link: '',
        },

      ],
      data: [


      ],
      window: {
        width: 0,
        height: 0,
        type: 'l',
      },
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
#Footer {
  background: linear-gradient(to right, #010177, #1c92d2);
  padding-bottom: 3rem;
}
h3 {
  margin-top: 6rem;
  margin-bottom: 4rem;
  color: white;
}
a {
  color: white;
  padding-left: 10rem;
}
ul {
  margin-bottom: 5rem;
}
.autoaling {
  margin: auto !important;
}
.cont {
  margin-left: 10em;
  margin-right: 10em;
}
#mensaje {
  color: white;
}
</style>
