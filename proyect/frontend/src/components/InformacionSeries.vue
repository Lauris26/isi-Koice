<template>

<div class="containerInformacion">
    <div class="row informacion">
      <div class="col-9">
        <div class="poster">
          <img src="https://static3.elnortedecastilla.es/www/multimedia/201910/11/media/cortadas/suitsbuena-kJiH-U903760469145RG-1248x770@El%20Norte.jpg" > 
          <button class="btn play" ><svg viewBox="0 0 24 24" width="50" height="50" fill="none" stroke="#f4f1f1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5,5.74V18.26a2,2,0,0,0,3.11,1.67l9.39-6.27a2,2,0,0,0,0-3.32L8.11,4.07A2,2,0,0,0,5,5.74Z" fill="#fbf7f7" opacity="1" stroke-width="0"></path><path d="M5,5.74V18.26a2,2,0,0,0,3.11,1.67l9.39-6.27a2,2,0,0,0,0-3.32L8.11,4.07A2,2,0,0,0,5,5.74Z"></path></svg></button>
        </div>

        <div class="row">
          <div class="col titulo">  
            <h2 class="tituloElemento">Suits</h2>
            <div class="yearDuration">
              <h4>2019</h4> &ensp;&bull;&ensp;
              <h4>6 temporadas</h4>
            </div>
            
          <div class="col generos"> 
            <a class="btn btn-lg btn-secondary" href="#">Comedia</a>
            <a class="btn btn-lg btn-secondary" href="#">Drama</a> 
          </div>
            
          </div>
          <div class="col mando"> 
            <router-link to="/mando" class="nav-link px-2 link-dark"> 
            <button class="btn mando"> Mando</button>
            </router-link>
          </div>


         <h3 class="titloDescripcion">Descripcion</h3>
         <p>Londres, 1970. El joven Farrokh, Freddie para los amigos, trabaja en el aeropuerto, estudia diseño gráfico y escribe canciones. 
           Un día, tras escuchar al grupo Smile en un bar, se ofrece como cantante de la banda al enterarse de que se han quedado sin vocalista. </p>
        </div>
        <br>

        <div class="temporadas">
          <h3 class="titloDescripcion">Temporadas</h3>
          <div class="row">
            <ul class="list-group">
              <div class="col" v-for="item in similaresSeriess" :key="item.id">
              <li class="list-group-item">Temporada {{item.id }}</li>
            </div>
            </ul>
          </div>
        </div>
        
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
                <div class="col" v-for="item in similaresSeriess" :key="item.id" >
                  
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
import {similaresSeries, reparto }  from '../main.js';
export default{
  name:"InformacionSeries",
  data () {
    return {
      id: 0,
      repartoActores: [],
      similaresSeriess: [],
    }
  },
  methods: {
    getPoster(serie) {
      return serie.poster;
    },
    getPhoto(nombre){
      return nombre.foto;
    },
  },
  created() {
    this.id = this.$route.params.id;
    this.similaresSeriess = similaresSeries();
    this.repartoActores = reparto();
    console.log("holi");

  },
}
</script>