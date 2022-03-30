<template>
    <div class="mando">
        <div class="row">
            <div class="col settings">
                <div class="col container">
                    <div class="row">
                        <button class="btn btn-lg btn-secondary" >
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48"><path fill="none" d="M0 0H24V24H0z"/><path d="M21 3c.552 0 1 .448 1 1v16c0 .552-.448 1-1 1H3c-.552 0-1-.448-1-1V4c0-.552.448-1 1-1h18zm-1 2H4v14h16V5zM9 8c1.105 0 2.105.448 2.829 1.173l-1.414 1.414C10.053 10.224 9.553 10 9 10c-1.105 0-2 .895-2 2s.895 2 2 2c.553 0 1.053-.224 1.414-.586l1.414 1.414C11.104 15.552 10.104 16 9 16c-2.208 0-4-1.792-4-4s1.792-4 4-4zm7 0c1.105 0 2.105.448 2.829 1.173l-1.414 1.414C17.053 10.224 16.553 10 16 10c-1.105 0-2 .895-2 2s.895 2 2 2c.552 0 1.052-.224 1.414-.586l1.414 1.414C18.104 15.552 17.104 16 16 16c-2.208 0-4-1.792-4-4s1.792-4 4-4z" fill="rgba(128,126,129,1)"/></svg>                    
                        </button>
                    </div>
                    <div class="row">
                        <button class="btn btn-lg btn-secondary" >
                            <svg fill="none" viewBox="0 0 16 16" width="48" height="48" xmlns="http://www.w3.org/2000/svg"><g fill="#807E81"><path d="m12.5 1.99634c.2761 0 .5.22386.5.5v2.50622h.5c.2761 0 .5.22386.5.5 0 .27615-.2239.5-.5.5h-.5v4.49744c0 .2761-.2239.5-.5.5s-.5-.2239-.5-.5v-8.00366c0-.27614.2239-.5.5-.5z"/><path d="m7.5 2.99635h2.5v1.25366c0 .41337-.15763.708-.39945.90822-.25208.20872-.63079.34178-1.09793.34178-.27614 0-.5.22386-.5.5s.22386.5.5.5c.64784 0 1.26782-.18415 1.73568-.57154.4781-.39589.7617-.97625.7617-1.67846v-1.75366c0-.13261-.0527-.25979-.1464-.35356-.0938-.09377-.221-.14644-.3536-.14644h-3c-.27614 0-.5.22386-.5.5s.22386.5.5.5z"/><path d="m6.45393 5.29939c-.0797-.18196-.25956-.29948-.45821-.2994-.19865.00009-.3784.11776-.45795.29979l-3.49593 8.00002c-.11057.253.00491.5478.25795.6584s.5478-.0049.65838-.258l1.17998-2.7002h3.69819c.00756 0 .01508-.0002.02256-.0005l1.18311 2.7011c.11079.253.40566.3682.6586.2574s.36819-.4056.25739-.6586zm.96718 4.7006h-2.84597l1.42133-3.25255z"/></g></svg>                        </button>
                    </div>
                    <!-- <div class="row">
                        <a class="btn btn-lg btn-secondary" >
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="#807e81" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="11.99" y1="7" x2="12.01" y2="7" stroke-linecap="round"></line><line x1="12" y1="11" x2="12" y2="17"></line></svg>
                        </a>
                    </div> -->
                </div>
                <div class="col volumen">
                    <button>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="#807e81" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2,10v4a2,2,0,0,0,2,2H5.36a2,2,0,0,1,1.16.37l4.9,3.5A1,1,0,0,0,13,19.06V4.94a1,1,0,0,0-1.58-.81l-4.9,3.5A2,2,0,0,1,5.36,8H4A2,2,0,0,0,2,10Z"></path><path d="M17.72,5.55a7,7,0,0,1,0,12.9"></path><path d="M17.12,9.88a3,3,0,0,1,0,4.24"></path></svg>
                    </button>
                    <div class="volumen-bar"></div>
                    <button>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="#807e81" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2,10v4a2,2,0,0,0,2,2H5.36a2,2,0,0,1,1.16.37l4.9,3.5A1,1,0,0,0,13,19.06V4.94a1,1,0,0,0-1.58-.81l-4.9,3.5A2,2,0,0,1,5.36,8H4A2,2,0,0,0,2,10Z"></path><path d="M17.12,9.88a3,3,0,0,1,0,4.24"></path></svg>
                    </button>
                </div>
            </div>
            <div class="col controls">
                <div class="play">
                    <button class="boton-play">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="84" height="84" fill="none" stroke="#957fb0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5,5.74V18.26a2,2,0,0,0,3.11,1.67l9.39-6.27a2,2,0,0,0,0-3.32L8.11,4.07A2,2,0,0,0,5,5.74Z"></path></svg>
                    </button>
                </div>
                <button class="btnPasarSiguiente">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="84" height="84" fill="none" stroke="#957fb0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="20" x2="4" y2="4"></line><path d="M20,17.34V6.66A2,2,0,0,0,16.92,5l-8.3,5.34a2,2,0,0,0,0,3.36L16.92,19A2,2,0,0,0,20,17.34Z"></path></svg>
                </button>
                <button class="btnvolverAtras">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="84" height="84" fill="none" stroke="#957fb0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4,6.66V17.34A2,2,0,0,0,7.08,19l8.3-5.34a2,2,0,0,0,0-3.36L7.08,5A2,2,0,0,0,4,6.66Z"></path><line x1="20" y1="4" x2="20" y2="20"></line></svg>
                </button>
            </div>
            <div class="col">
                <div class="row viendoAhora">
                    <h2>Estas viendo: <br> Bohemian Rhapsody</h2>
                </div>
                <div class="row siguiente">
                    <h2>Siguiente: Parasitos</h2>
                    <img class="card-image siguiente" src="../assets/parasites.png">
                </div>
            </div>
        </div>
    </div>
</template>


<script>

export default{
    name:"MandoKoice",
};
</script>