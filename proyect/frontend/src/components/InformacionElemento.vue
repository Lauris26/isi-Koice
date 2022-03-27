<template>

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