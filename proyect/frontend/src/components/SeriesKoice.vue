<template>

  <div class="home">
    <div id="myCarousel" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img class="bd-placeholder-img" width="100%" height="100%" src="../assets/blackMirror.jpg">
          <div class="container">
            <div class="carousel-caption text-start">
              <h1>Black Mirror</h1>
              <p>El lado oscuro de la era tecnológica en la que se vive: la paranoia de ser vigilados como en un 
                panóptico, los usos terroristas de las nuevas herramientas y su relación con la experiencia cotidiana.</p>
               <router-link :to="{ name: 'informacionSeries', params: {id: 1}}" class="nav-link px-2 link-dark">  
                <button class="btn btn-lg btn-primary" >Mas informacion</button>
              </router-link>
            </div>
          </div>
        </div>

        <div class="carousel-item">
        <img class="bd-placeholder-img" width="100%" height="100%" src="../assets/squid-game.jpg">
          <div class="container">
            <div class="carousel-caption text-start">
              <h1>El juego del calamar</h1>
              <p>Cientos de personas con dificultades económicas aceptan una extraña invitación a un juego 
                  de supervivencia. Les espera un premio millonario, pero hay mucho en juego.</p>
              <router-link :to="{ name: 'informacionSeries', params: {id: 2}}" class="nav-link px-2 link-dark">  
                <button class="btn btn-lg btn-primary" >Mas informacion</button>
              </router-link>
            </div>
          </div>
        </div>
      </div>
      
      <button class="carousel-control-prev" type="button" data-bs-target="#myCarousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#myCarousel" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
  </div>

  <div class="album">
    <div class="container">
      <div class="row catalogo">
        <div class="col" v-for="item in peliculas" :key="item.id" >
          <div class="elementoPelicula">
             <router-link :to="{ name: 'informacionSeries', params: { id: item.id } }" class="nav-link px-2 link-dark">
             <img class="card-image" :src="getPic(item)"> 
             <div class="titlePoster">{{item.titulo}}</div>
             </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>


<script>
import { obtenerSeries}  from '../api.js'; 

export default{
    name:"MandoKoice",
     data(){
       return{
        peliculas: null,
      }
    },
    methods: {
        getPic(peliculas) {
          return peliculas.poster;
        },
        async obtenerSeries(){
          this.peliculas=await obtenerSeries();
        }
    },

    beforeCreate() {
      console.log('No se ha ejecutado nada todavía')
    },
    created() {
    console.log("Componentes cargados"),
    this.obtenerSeries();
    }, 
    mounted() {
      console.log(this.$el.querySelectorAll('a'));
    },
    updated() {
      console.log("Componente actualizado");
    }
};

</script>


