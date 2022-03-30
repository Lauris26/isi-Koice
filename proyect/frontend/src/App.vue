<template>

  <header class="p-3 mb-3 border-bottom">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <img class="logo-image" alt="" src="./assets/logo.png">
        <span class="fs-4">Koice</span>
        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
          <li> 
             <router-link to="/peliculas" class="nav-link px-2 link-dark">
              <img class="icons2" src="./assets/movie.png"> Peliculas
            </router-link>
          </li>
          <li>
            <router-link to="/series" class="nav-link px-2 link-dark"> 
              <img class="icons" src="./assets/watching-tv.png"> Series
            </router-link>
          </li>
          <li>
            <router-link to="/mando" class="nav-link px-2 link-dark"> 
              <img class="icons" src="./assets/remote-control.png"> Mando
            </router-link>
          </li>
        </ul>
        <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3">
          <div class="search-icon">
            <input type="search" class="form-control" placeholder="Buscar..." aria-label="Search" v-model="s">
            <div class="btn-group dropstart">
              <button class="btn-group dropstart" data-bs-toggle="dropdown" data-bs-display="static" aria-expanded="false">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="36" height="36" fill="none" stroke="#807e81" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><path d="M21.57,5l-7.14,8.48A1.82,1.82,0,0,0,14,14.67V20a2,2,0,0,1-2,2h0a2,2,0,0,1-2-2V14.67a1.82,1.82,0,0,0-.43-1.18L2.43,5A1.82,1.82,0,0,1,2,3.83H2A1.83,1.83,0,0,1,3.83,2H20.17A1.83,1.83,0,0,1,22,3.83h0A1.82,1.82,0,0,1,21.57,5Z" fill="#807e81" opacity="1" stroke-width="0"></path><path d="M21.57,5l-7.14,8.48A1.82,1.82,0,0,0,14,14.67V20a2,2,0,0,1-2,2h0a2,2,0,0,1-2-2V14.67a1.82,1.82,0,0,0-.43-1.18L2.43,5A1.82,1.82,0,0,1,2,3.83H2A1.83,1.83,0,0,1,3.83,2H20.17A1.83,1.83,0,0,1,22,3.83h0A1.82,1.82,0,0,1,21.57,5Z"></path></svg>          
              </button>
            <div class="dropdown-menu megamenu" role="menu">
              <div class="margenesFiltro">
                <h3>Filtros</h3>
                <div class="filtros"> 
                  <h5>Genero:</h5>
                  <a class="btn btn-lg btn-secondary" href="#">Comedia</a>
                  <a class="btn btn-lg btn-secondary" href="#">Accion</a>
                  <a class="btn btn-lg btn-secondary" href="#">Terror</a>
                  <a class="btn btn-lg btn-secondary" href="#">Ciencia Ficcion</a> 
                  <a class="btn btn-lg btn-secondary" href="#">Drama</a>
                </div>
                <hr>
                <div class="filtros"> 
                  <h5>Año:</h5>
                  <a class="btn btn-lg btn-secondary" href="#">2010</a>
                  <a class="btn btn-lg btn-secondary" href="#">2011</a>
                  <a class="btn btn-lg btn-secondary" href="#">2012</a>
                  <a class="btn btn-lg btn-secondary" href="#">2013</a>
                  <a class="btn btn-lg btn-secondary" href="#">2014</a>
                  <a class="btn btn-lg btn-secondary" href="#">2015</a>
                  <a class="btn btn-lg btn-secondary" href="#">2016</a>
                  <a class="btn btn-lg btn-secondary" href="#">2017</a>
                  <a class="btn btn-lg btn-secondary" href="#">2018</a>
                  <a class="btn btn-lg btn-secondary" href="#">2019</a>
                  <a class="btn btn-lg btn-secondary" href="#">2020</a>
                  <a class="btn btn-lg btn-secondary" href="#">2021</a>
                  <a class="btn btn-lg btn-secondary" href="#">2022</a>
                </div>
                <hr>
                <div class="filtros"> 
                  <h5>Pais:</h5>
                    <a class="btn btn-lg btn-secondary" href="#">España</a>
                    <a class="btn btn-lg btn-secondary" href="#">Estados Unidos</a> 
                    <a class="btn btn-lg btn-secondary" href="#">Corea del Sur</a>
                    <a class="btn btn-lg btn-secondary" href="#">Francia</a> 
                    <a class="btn btn-lg btn-secondary" href="#">Rusia</a>
                    <a class="btn btn-lg btn-secondary" href="#">Alemania</a> 
                </div>
              </div> 
            </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </header>

  <router-view/>
  
  <footer class="footer mt-auto py-3 bg-light">
    <div class="container">
      <span class="text-muted">Pagina realizada para el proyecto de la asignatura de Integracion de sistemas informaticos</span>
      <div>
        <span class="text-muted">Escuela Superior de Informatica</span>
      </div>
    </div>
  </footer>

  
</template>


<script>
export default {
  name: 'App',
  components: {},
  data(){
    return{
    }
  }
};
</script>