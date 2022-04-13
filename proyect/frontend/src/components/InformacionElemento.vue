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

<div class="containerInformacion">
    <div class="row informacion">
      <div class="col-9">
        <div class="poster">
          <img src="https://flxt.tmsimg.com/assets/p12386480_p_v8_af.jpg" > 
          <button class="btn play" ><svg viewBox="0 0 24 24" width="50" height="50" fill="none" stroke="#f4f1f1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5,5.74V18.26a2,2,0,0,0,3.11,1.67l9.39-6.27a2,2,0,0,0,0-3.32L8.11,4.07A2,2,0,0,0,5,5.74Z" fill="#fbf7f7" opacity="1" stroke-width="0"></path><path d="M5,5.74V18.26a2,2,0,0,0,3.11,1.67l9.39-6.27a2,2,0,0,0,0-3.32L8.11,4.07A2,2,0,0,0,5,5.74Z"></path></svg></button>
        </div>

        <div class="row">
          <div class="col titulo">  
            <h2 class="tituloElemento">La La Land</h2>
            <div class="yearDuration">
              <h4>2016</h4> &ensp;&bull;&ensp;
              <h4>128 min</h4>
            </div>
            
          <div class="col generos"> 
            <a class="btn btn-lg btn-secondary">Romance</a>
            <a class="btn btn-lg btn-secondary">Musical</a>
          </div>
          </div>

          <div class="col mando"> 
            <button class="btn mando"> Mando</button>
          </div>


         <h3 class="titloDescripcion">Descripcion</h3>
         <p>Mia y Sebastian son dos jóvenes que quieren abrirse camino en el mundo de Hollywood. Mia es una joven aspirante a actriz que 
           trabaja como camarera mientras acude a castings y Sebastian toca el piano en bares. Un día sus caminos se cruzan e inmediatamente se enamoran. </p>
        </div>
        <br>
        
        <div class="reparto">
          <h3 class="titloDescripcion">Reparto</h3>
          <div class="row">
            <div class="col" v-for="item in repartoActores" :key="item.id">
              <div class="elenco">
                 <img class="card-image" :src="getPhoto(item)"> 
                <div class="titlePoster">{{item.titulo}}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

    <div class="col">
        <h3 class="titloRecomendaciones">Similares</h3>
          <div class="recomendaciones">
            
              <div class="row">
                <div class="col" v-for="item in similaresPeliculas" :key="item.id" >
                  
                  <div class="elementoRecomendacion" >
                    <img class="card-image" :src="getPoster(item)">
                    <div class="titlePoster">{{item.titulo}}</div>
                  </div>
                  </div>
              </div>
          </div>        
      </div> 
    </div>
  </div>
</div>
</template>

<script>
import {similaresPelis, reparto}  from '../main.js';
export default{
  name:"InformacionElemento",
  data () {
    return {
      id: 0,
      similaresPeliculas: [],
      repartoActores: []
    }
  },
  methods: {
    getPoster(pelicula) {
      return pelicula.poster;
    },
    getPhoto(nombre){
      return nombre.foto;
    }

  },
  created() {
    this.id = this.$route.params.id;
    this.similaresPeliculas = similaresPelis();
    this.repartoActores = reparto();

  },
  
}
</script>