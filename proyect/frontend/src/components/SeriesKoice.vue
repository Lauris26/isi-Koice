<template>

<div>
  <header class="p-3 mb-3 border-bottom">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <img class="logo-image" alt="" src="../assets/logo.png">
        <span class="fs-4">Koice</span>
        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
          <li> 
             <router-link to="/peliculas" class="nav-link px-2 link-dark">
              <img class="icons2" src="../assets/movie.png"> Peliculas
            </router-link>
          </li>
          <li>
            <router-link to="/series" class="nav-link px-2 link-dark">
              <img class="icons" src="../assets/watching-tv.png"> Series
            </router-link>
          </li>
          <li>
            <router-link to="/mando" class="nav-link px-2 link-dark"> 
              <img class="icons" src="../assets/remote-control.png"> Mando
            </router-link>
          </li>
        </ul>
        <div class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3">
          <div class="search-icon">
            
              <button class="botonBuscar" v-on:click="onEnter()">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="36" height="36" fill="none" stroke="#807e81" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="9" fill="none"></circle><line x1="17.5" y1="17.5" x2="22" y2="22"></line></svg>
              </button>
            <input type="search" class="form-control" :placeholder= "this.place" aria-label="Search" v-model="busqueda">
            
            <div class="btn-group dropstart"> 
              <button class="btn-group dropstart" data-bs-toggle="dropdown" data-bs-display="static" aria-expanded="false">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="36" height="36" fill="none" stroke="#807e81" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M21.57,5l-7.14,8.48A1.82,1.82,0,0,0,14,14.67V20a2,2,0,0,1-2,2h0a2,2,0,0,1-2-2V14.67a1.82,1.82,0,0,0-.43-1.18L2.43,5A1.82,1.82,0,0,1,2,3.83H2A1.83,1.83,0,0,1,3.83,2H20.17A1.83,1.83,0,0,1,22,3.83h0A1.82,1.82,0,0,1,21.57,5Z" fill="#807e81" opacity="1" stroke-width="0"></path><path d="M21.57,5l-7.14,8.48A1.82,1.82,0,0,0,14,14.67V20a2,2,0,0,1-2,2h0a2,2,0,0,1-2-2V14.67a1.82,1.82,0,0,0-.43-1.18L2.43,5A1.82,1.82,0,0,1,2,3.83H2A1.83,1.83,0,0,1,3.83,2H20.17A1.83,1.83,0,0,1,22,3.83h0A1.82,1.82,0,0,1,21.57,5Z"></path></svg>          
              </button>
            <div class="dropdown-menu megamenu" role="menu">
              <div class="margenesFiltro">
                <h3>Filtros</h3>
                <div class="filtros"> 
                  <h5>Genero:</h5>
                  <button class="btn btn-lg btn-secondary" href="#">Comedia</button>
                  <button class="btn btn-lg btn-secondary" href="#">Accion</button>
                  <button class="btn btn-lg btn-secondary" href="#">Terror</button>
                  <button class="btn btn-lg btn-secondary" href="#">Ciencia Ficcion</button> 
                  <button class="btn btn-lg btn-secondary" href="#">Drama</button>
                </div>
                <hr>
                <div class="filtros"> 
                  <h5>Año:</h5>
                  <button v-on:click="buscarAnio()" class="btn btn-lg btn-secondary" href="#">Buscar por año</button>
                </div>
                <hr>
                <div class="filtros"> 
                  <h5>Pais:</h5>
                    <button class="btn btn-lg btn-secondary" href="#">España</button>
                    <button class="btn btn-lg btn-secondary" href="#">Estados Unidos</button> 
                    <button class="btn btn-lg btn-secondary" href="#">Corea del Sur</button>
                    <button class="btn btn-lg btn-secondary" href="#">Francia</button> 
                    <button class="btn btn-lg btn-secondary" href="#">Rusia</button>
                    <button class="btn btn-lg btn-secondary" href="#">Alemania</button> 
                </div>
              </div> 
            </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>

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
        <div class="col" v-for="item in peliculas2" :key="item.id" >
          <div class="elementoPelicula">
             <router-link :to="{ name: 'informacionSeries', params: { id: item.id } }" class="nav-link px-2 link-dark">
             <img class="card-image" :src="getPic(item)"> 
             <div class="ActorNombre">{{item.titulo}}</div>
             </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <h1>{{this.s}}</h1>
  </div>

  </div>
</template>

<script>
import { similaresSeries}  from '../main.js';

export default{
  name:"SeriesKoice",
  data: function(){
    return{
      peliculas2:[],
      s: 'asdfasf',
    }
  },
  methods: {
    getPic(peliculas2) {
      return peliculas2.poster;
    },
    pelisC(){
      this.peliculas2 = similaresSeries();
    },
  },
  created() {
    this.pelisC();
    this.s = this.$route.params.s;
  }
};

</script>


