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
                de Pandora es venenoso, los híbridos humanos/Na'vi, llamados Avatares, están relacionados 
                con las mentes humanas, lo que les permite moverse libremente por Pandora. Jake Sully, un
                exinfante de marina paralítico se transforma a través de un Avatar, y se enamora de una mujer Na'vi.</p>
              <p><a class="btn btn-lg btn-primary" href="#">Ver pelicula</a></p>
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
              <p><a class="btn btn-lg btn-primary" href="#">Ver pelicula</a></p>
            </div>
          </div>
        </div>

        <div class="carousel-item">
        <img class="bd-placeholder-img" width="100%" height="100%" src="../assets/batman.jpg">
          <div class="container">
            <div class="carousel-caption text-start">
              <h1>The Batman</h1>
              <p>En su segundo año luchando contra el crimen, Batman explora la corrupción 
                existente en la ciudad de Gotham y el vínculo de esta con su propia familia. 
                Además, entrará en conflicto con un asesino en serie conocido como "el Acertijo".</p>
              <p><a class="btn btn-lg btn-primary" href="#">Ver pelicula</a></p>
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
          <div class="col peliculas" v-for="item in peliculas2" :key="item.id" >
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
import { obtenerPelis}  from '../main.js';

export default{
  name:"PeliculasKoice",
  data: function(){
    return{
      peliculas2 : [],
      peliculas3: null, 
    }
  },
  methods: {
    getPic(peliculas2) {
      return peliculas2.poster;
    },
    pelisC(){
      this.peliculas2 = obtenerPelis();
    },
  },
  created() {
    this.pelisC();
  }
};
</script>