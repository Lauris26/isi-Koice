<template>

  <div class="home">
    <div id="myCarousel" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img class="bd-placeholder-img" width="100%" height="100%" src="../assets/gameofthrones.jpg">
        <div class="container">
          <div class="carousel-caption text-start">
            
            <h1>Juego de tronos</h1>
            <p>Es la descripción de dos familias poderosas, reyes y reinas, caballeros y renegados, 
                hombres falsos y honestos, haciendo parte de un juego mortal por el control de los Siete 
                Reinados de Westeros y por sentarse en el trono más alto. Martin es el co productor ejecutivo 
                y uno de los escritores de la serie que fue filmada en el Norte de Irlanda y Malta.</p>
            <p><a class="btn btn-lg btn-primary" href="#">Ver serie</a></p>
          </div>
        </div>
      </div>
      
      <div class="carousel-item">
        <img class="bd-placeholder-img" width="100%" height="100%" src="../assets/walkingdead.jpg">
        <div class="container">
          <div class="carousel-caption text-start">
            <h1>The walking dead</h1>
            <p>Este drama crudo describe las vidas de un grupo de sobrevivientes que está siempre en 
                movimiento en busca de un hogar seguro durante las semanas y meses de un apocalipsis zombi. 
                Sin embargo, la presión de estar con vida cada día, lleva a algunos del grupo a la crueldad 
                profunda de cada ser humano y descubren que el miedo abrumador puede ser más mortal que los zombis 
                que caminan a su alrededor. Los conflictos interpersonales pueden representar una amenaza mayor para
                 su supervivencia que los caminantes que deambulan por las calles.</p>
            <p><a class="btn btn-lg btn-primary" href="#">Ver serie</a></p>
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
            <p><a class="btn btn-lg btn-primary" href="#">Ver serie</a></p>
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

        <div class="col" v-for="id in peliculas" v-bind:key="id">
          <div class="elementoPelicula">
            <img class="card-image" :src="getPic(id)">
            <div class="titlePoster">{{id.titulo}}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </div>



</template>


<script>
import fetch from 'node-fetch';
import { peliculas }  from '../main.js';

export default{
    name:"MandoKoice",
     data(){
       return{
        peliculas
      }
    },
    methods: {
        async algo(){
          const response = await fetch('http://127.0.0.1:5000/');
          const body = await response.text();
          return body['result'];
        },

        getPic(peliculas) {
          return peliculas.poster;
        },
    },

    beforeCreate() {
      console.log('No se ha ejecutado nada todavía')
    },
    created: () => console.log("Componentes cargados"),
    mounted() {
      console.log(this.$el.querySelectorAll('a'));
    },
    updated() {
      console.log("Componente actualizado");
    }
};

</script>


