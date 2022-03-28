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
        <img class="bd-placeholder-img" width="100%" height="100%" src="../assets/avatar.jpg">
        <div class="container">
          <div class="carousel-caption text-start">
            
              <h1>Avatar</h1>
              <p>En un exuberante planeta llamado Pandora viven los Na'vi, seres que aparentan 
                ser primitivos pero que en realidad son muy evolucionados. Debido a que el ambiente 
                de Pandora es venenoso, los híbridos humanos /Na'vi, llamados Avatares, están relacionados 
                con las mentes humanas, lo que les permite moverse libremente por Pandora. Jake Sully, un
                exinfante de marina paralítico se transforma a través de un Avatar, y se enamora de una mujer Na'vi.</p>
              <router-link :to="{ name: 'informacion', params: {id: 1}}" class="nav-link px-2 link-dark">
                <button class="btn btn-lg btn-primary" >Mas informacion</button>
              </router-link>
            </div>
          </div>
        </div>
      
        <div class="carousel-item">
        <img class="bd-placeholder-img" width="100%" height="100%" src="../assets/vengadores.jpg">
          <div class="container">
            <div class="carousel-caption text-start">
              <h1>Los vengadores</h1>
              <p>El director de la Agencia SHIELD decide reclutar a un equipo para salvar al mundo de un desastre 
                casi seguro cuando un enemigo inesperado surge como una gran amenaza para la seguridad mundial.</p>
              <router-link :to="{ name: 'informacion', params: {id: 2}}" class="nav-link px-2 link-dark">  
                <button class="btn btn-lg btn-primary" >Mas informacion</button>
              </router-link>
            </div>
          </div>
        </div>
      </div>

        <div class="carousel-item">
          <img class="bd-placeholder-img" width="100%" height="100%" src="../assets/parasites.png">
          <div class="container">
            <div class="carousel-caption text-start">
              <h1>Parasitos</h1>
              <p>Tanto Gi Taek como su familia están sin trabajo. Cuando su hijo mayor, Gi Woo, empieza a 
                recibir clases particulares en la adinerada casa de Park, las dos familias, que tienen mucho 
                en común pese a pertenecer a dos mundos totalmente distintos, comienzan una relación de resultados 
                imprevisibles.</p>
              <router-link :to="{ name: 'informacion', params: {id: 3}}" class="nav-link px-2 link-dark">  
                <button class="btn btn-lg btn-primary" href="#">Mas informacion</button>
              </router-link>
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
        <div class="col peliculas" v-for="item in peliculas" v-bind:key="item.id">
          <div class="elementoPelicula">
             <router-link :to="{ name: 'informacion', params: { id: item.id } }" class="nav-link px-2 link-dark">
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
import fetch from 'node-fetch';
//import { getVideoUso, setVideoUso }  from '../main.js';
import { obtenerPeliculas }  from '../api.js';

export default{
    name:"MandoKoice",
     data(){
       return{
        peliculas:null,
        cosa:null
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
        pelicu(idPeli){
          this.cosa=idPeli;
          //InformacionElemento.idPelicula=idPeli;
          //setVideoUso(idPeli);
          //console.log('id ', getVideoUso());
        },
        async obtenerPelis(){
          this.peliculas=await obtenerPeliculas();
        },
        videoUdo (idPeli){
          this.id=idPeli;
        }
    },

    beforeCreate() {
      console.log('No se ha ejecutado nada todavía')
    },
    created() {
    console.log("Componentes cargados"),
    this.obtenerPelis();
    this.videoUdo(1);
    }, 
    mounted() {
      console.log(this.$el.querySelectorAll('a'));
    },
    updated() {
      console.log("Componente actualizado");
    }
};

</script>