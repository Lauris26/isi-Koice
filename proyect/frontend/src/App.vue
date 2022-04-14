<template>
<div>

  <router-view/>
  
  <footer class="footer mt-auto py-3 bg-light">
    <div class="container">
      <span class="text-muted">Pagina realizada para el proyecto de la asignatura de Integracion de sistemas informaticos</span>
      <div>
        <span class="text-muted">Escuela Superior de Informatica</span>
      </div>
    </div>
  </footer>

  </div>
</template>


<script>
export default {
  name: 'App',
  components: {},
  data(){
    return{
      busqueda:'',
      busque: 'null',
      filter: 'Nombre',
      place : 'Buscar...',
    }
    
  },
  methods: {
    onEnter() {
      this.busque = this.busqueda;
    },
    buscarAnio(){
      this.filter = 'Anio';
      this.place = 'Buscar por año'
    }
  },
};
</script>