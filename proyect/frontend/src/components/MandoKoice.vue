<template>

    <div class="mando">
        <div class="row">
            <div class="col settings">
                <div class="col container">
                    <div class="row">
                        <a class="btn btn-lg btn-secondary" href="#">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48"><path fill="none" d="M0 0H24V24H0z"/><path d="M21 3c.552 0 1 .448 1 1v16c0 .552-.448 1-1 1H3c-.552 0-1-.448-1-1V4c0-.552.448-1 1-1h18zm-1 2H4v14h16V5zM9 8c1.105 0 2.105.448 2.829 1.173l-1.414 1.414C10.053 10.224 9.553 10 9 10c-1.105 0-2 .895-2 2s.895 2 2 2c.553 0 1.053-.224 1.414-.586l1.414 1.414C11.104 15.552 10.104 16 9 16c-2.208 0-4-1.792-4-4s1.792-4 4-4zm7 0c1.105 0 2.105.448 2.829 1.173l-1.414 1.414C17.053 10.224 16.553 10 16 10c-1.105 0-2 .895-2 2s.895 2 2 2c.552 0 1.052-.224 1.414-.586l1.414 1.414C18.104 15.552 17.104 16 16 16c-2.208 0-4-1.792-4-4s1.792-4 4-4z" fill="rgba(128,126,129,1)"/></svg>                    
                        </a>
                    </div>
                    <div class="row">
                        <a class="btn btn-lg btn-secondary" href="#">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="#807e81" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18.4,20.8,12,16,5.6,20.8A1,1,0,0,1,4,20V4A2,2,0,0,1,6,2H18a2,2,0,0,1,2,2V20A1,1,0,0,1,18.4,20.8Z"></path></svg>
                        </a>
                    </div>
                    <div class="row">
                        <a class="btn btn-lg btn-secondary" href="#">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="#807e81" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="11.99" y1="7" x2="12.01" y2="7" stroke-linecap="round"></line><line x1="12" y1="11" x2="12" y2="17"></line></svg>
                        </a>
                    </div>
                </div>
                <div class="col volumen">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="#807e81" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2,10v4a2,2,0,0,0,2,2H5.36a2,2,0,0,1,1.16.37l4.9,3.5A1,1,0,0,0,13,19.06V4.94a1,1,0,0,0-1.58-.81l-4.9,3.5A2,2,0,0,1,5.36,8H4A2,2,0,0,0,2,10Z"></path><path d="M17.72,5.55a7,7,0,0,1,0,12.9"></path><path d="M17.12,9.88a3,3,0,0,1,0,4.24"></path></svg>
                    <div class="volumen-bar"></div>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="#807e81" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2,10v4a2,2,0,0,0,2,2H5.36a2,2,0,0,1,1.16.37l4.9,3.5A1,1,0,0,0,13,19.06V4.94a1,1,0,0,0-1.58-.81l-4.9,3.5A2,2,0,0,1,5.36,8H4A2,2,0,0,0,2,10Z"></path><path d="M17.12,9.88a3,3,0,0,1,0,4.24"></path></svg>
                </div>
            </div>
            <div class="col controls">
                <div class="play">
                    <a class="btn btn-lg btn-secondary" href="#">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="84" height="84" fill="none" stroke="#957fb0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5,5.74V18.26a2,2,0,0,0,3.11,1.67l9.39-6.27a2,2,0,0,0,0-3.32L8.11,4.07A2,2,0,0,0,5,5.74Z"></path></svg>
                    </a>
                </div>
                <svg class="chevronUp" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="84" height="84" fill="none" stroke="#957fb0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="17 14 12 9 7 14"></polyline></svg>
                <svg class="pasarSiguiente" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="84" height="84" fill="none" stroke="#957fb0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="20" x2="4" y2="4"></line><path d="M20,17.34V6.66A2,2,0,0,0,16.92,5l-8.3,5.34a2,2,0,0,0,0,3.36L16.92,19A2,2,0,0,0,20,17.34Z"></path></svg>
                <svg class="volverAtras" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="84" height="84" fill="none" stroke="#957fb0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4,6.66V17.34A2,2,0,0,0,7.08,19l8.3-5.34a2,2,0,0,0,0-3.36L7.08,5A2,2,0,0,0,4,6.66Z"></path><line x1="20" y1="4" x2="20" y2="20"></line></svg>
                <svg class="chevronDown" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="84" height="84" fill="none" stroke="#957fb0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="7 10 12 15 17 10"></polyline></svg>
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