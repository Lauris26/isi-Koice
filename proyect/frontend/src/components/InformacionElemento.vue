<template>
<div class="containerInformacion">
<div class="hello">
        <h1>{{ msg }}, your id is {{ id }}</h1>
        <button v-on:click=reproducirPeli></button>
    </div>


    <div class="row informacion">
      <div class="col-9">
        <div class="poster">
          <img class="card-image" :src="getPicPortada()"> 
          <buttom v-on:click=reproducirPeli class="btn play" href="#"><svg viewBox="0 0 24 24" width="50" height="50" fill="none" stroke="#f4f1f1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5,5.74V18.26a2,2,0,0,0,3.11,1.67l9.39-6.27a2,2,0,0,0,0-3.32L8.11,4.07A2,2,0,0,0,5,5.74Z" fill="#fbf7f7" opacity="1" stroke-width="0"></path><path d="M5,5.74V18.26a2,2,0,0,0,3.11,1.67l9.39-6.27a2,2,0,0,0,0-3.32L8.11,4.07A2,2,0,0,0,5,5.74Z"></path></svg></buttom>

        </div>

        <div class="row">
          <div class="col titulo">  
            <h2 class="tituloElemento">{{pelicula.title}}</h2>
            <div class="yearDuration">
              <h4>{{pelicula.year}}</h4> &ensp;&bull;&ensp;
              <h4>{{pelicula.runtime}} min</h4>
            </div>
            
          <div class="col generos"> 
            <a class="btn btn-lg btn-secondary" href="#">{{pelicula.genre[0]}}</a>
            <a class="btn btn-lg btn-secondary" href="#">{{pelicula.genre[1]}}</a> 
          </div>
            
          </div>
          <div class="col mando"> 
            <buttom class="btn mando" href="#">Mando</buttom>
          </div>


         <h3 class="titloDescripcion">Descripcion</h3>
         <p>{{pelicula.plot}} </p>
        </div>
        <br>
        
<div class="reparto">
          <h3 class="titloDescripcion">Reparto</h3>
          <div class="row">
            <div class="col" v-for="item in pelicula.actores" :key="item.id">
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
                <div class="col">
                  <div class="elementoRecomendacion">
                    <img class="card-image" src="https://m.media-amazon.com/images/M/MV5BNGZiMzBkZjMtNjE3Mi00MWNlLWIyYjItYTk3MjY0Yjg5ODZkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_SX300.jpg">
                    <div class="titlePoster">Avengers: Endgame</div>
                  </div>
                </div>

                <div class="col">
                  <div class="elementoRecomendacion">
                    <img class="card-image" src="https://m.media-amazon.com/images/M/MV5BNGZiMzBkZjMtNjE3Mi00MWNlLWIyYjItYTk3MjY0Yjg5ODZkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_SX300.jpg">
                    <div class="titlePoster">Avengers: Endgame</div>
                  </div>
                </div>

                <div class="col">
                  <div class="elementoRecomendacion">
                    <img class="card-image" src="https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg">
                    <div class="titlePoster">Avengers: Endgame</div>
                  </div>
                </div>

                <div class="col">
                  <div class="elementoRecomendacion">
                    <img class="card-image" src="https://m.media-amazon.com/images/M/MV5BNGZiMzBkZjMtNjE3Mi00MWNlLWIyYjItYTk3MjY0Yjg5ODZkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_SX300.jpg">
                    <div class="titlePoster">Avengers: Endgame</div>
                  </div>       
                </div>

                <div class="col">
                  <div class="elementoRecomendacion">
                    <img class="card-image" src="https://m.media-amazon.com/images/M/MV5BNGZiMzBkZjMtNjE3Mi00MWNlLWIyYjItYTk3MjY0Yjg5ODZkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_SX300.jpg">
                    <div class="titlePoster">Avengers: Endgame</div>
                  </div>
                </div>

                <div class="col">
                  <div class="elementoRecomendacion">
                    <img class="card-image" src="https://m.media-amazon.com/images/M/MV5BNGZiMzBkZjMtNjE3Mi00MWNlLWIyYjItYTk3MjY0Yjg5ODZkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_SX300.jpg">
                    <div class="titlePoster">Avengers: Endgame</div>
                  </div>
                </div>
              </div>
          </div>        
      </div> 
    </div>
    
  </div>

</template>

<script>
import { obtenerPeliculasInfo, reproducirPeli }  from '../api.js';

export default{
  name:"MandoKoice",
  data () {
    return {
      id: 0,
      msg: 'Hey Nic Raboy',
      pelicula: null
    }
  },
      methods: {
        getPic(actor) {
          return actor.foto;
        },
        getPicPortada() {
          return this.pelicula.poster;
        },
        async obtenerPelisInfo(id){
          this.pelicula=await obtenerPeliculasInfo(id);
        },
        async reproducirPeli(){
          await reproducirPeli(this.id);
        }
    },
  created() {
    this.id = this.$route.params.id;
    console.log(this.id);
    this.obtenerPelisInfo(this.id);
  },

}
</script>