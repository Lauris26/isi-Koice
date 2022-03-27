<template>

<div class="containerInformacion">
    <div class="row informacion">
      <div class="col-9">
        <div class="poster">
          <img class="card-image" :src="getPicPortada()"> 
          <button class="btn play" ><svg viewBox="0 0 24 24" width="50" height="50" fill="none" stroke="#f4f1f1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5,5.74V18.26a2,2,0,0,0,3.11,1.67l9.39-6.27a2,2,0,0,0,0-3.32L8.11,4.07A2,2,0,0,0,5,5.74Z" fill="#fbf7f7" opacity="1" stroke-width="0"></path><path d="M5,5.74V18.26a2,2,0,0,0,3.11,1.67l9.39-6.27a2,2,0,0,0,0-3.32L8.11,4.07A2,2,0,0,0,5,5.74Z"></path></svg></button>
        </div>

        <div class="row">
          <div class="col titulo">  
            <h2 class="tituloElemento">{{serie.title}}</h2>
            <div class="yearDuration">
              <h4>{{serie.year}}</h4> &ensp;&bull;&ensp;
              <h4>{{serie.season}} temporadas</h4>
            </div>     

          <div class="generos">
          <h3 class="titloDescripcion">Generos</h3>
          <div class="col generos"> 
            <a class="btn btn-lg btn-secondary" v-for="item in serie.genre" :key="item.id">{{item}}</a>
          </div>
          </div>
            
          </div>
          <div class="col mando"> 
            <router-link to="/mando" class="nav-link px-2 link-dark"> 
            <button class="btn mando"> Mando</button>
            </router-link>
          </div>


         <h3 class="titloDescripcion">Descripcion</h3>
         <p>{{serie.plot}}</p>
        </div>
        <br>

        <div class="reparto">
          <h3 class="titloDescripcion">Temporadas</h3>
          <div class="row">
            <ul class="list-group">
              <div class="col" v-for="item in serie.seasons" :key="item.id">
              <li class="list-group-item">{{item.label}}</li>
            </div>
            </ul>
          </div>
        </div>
        
        <div class="reparto">
          <h3 class="titloDescripcion">Reparto</h3>
          <div class="row">
            <div class="col" v-for="item in serie.actores" :key="item.id">
              <div class="elenco">
                 <img class="card-image" :src="getPic(item)"> 
                <div class="titlePoster">{{item.nombre}}</div>
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
import { obtenerSeriesInfo }  from '../api.js';
import {similaresSeries }  from '../main.js';

export default{
  name:"MandoKoice",
  data () {
    return {
      id: 0,
      similaresSeriess: [],
      serie: null
    }
  },
      methods: {
        getPoster(serie) {
      return serie.poster;
    },
        getPic(actor) {
          return actor.foto;
        },
        getPicPortada() {
          return this.serie.poster;
        },
        async obtenerSerieInfo(id){
          this.serie=await obtenerSeriesInfo(id);
        }
    },
  created() {
    this.id = this.$route.params.id;
    console.log(this.id);
    this.obtenerSerieInfo(this.id);
    this.similaresSeriess = similaresSeries();
  },
}
</script>