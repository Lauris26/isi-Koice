import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap';
import { createRouter, createWebHistory } from 'vue-router';
import fetch from 'node-fetch';
// import router from './router'

const routes = [
{
        path: '/peliculas',
        name: 'peliculas',
        component: () => import('./components/PeliculasKoice.vue')
    },
    {
        path: '/series',
        name: 'series',
        component: () => import('./components/SeriesKoice.vue')
    },
    {
        path: '/mando',
        name: 'mando',
        component: () => import('./components/MandoKoice.vue')
    },
    {
        path: '/informacion:id',
        name: 'informacion',
        component: () => import('./components/InformacionElemento.vue')
    },
    {
        path:'',
        component: () => import('./components/PeliculasKoice.vue')
    }

]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
    linkActiveClass: 'active',
});

router.beforeEach((to, _1, next) => {
    console.log('Global before each');
    if (to.path === '/createpost') {
        next();
    } else {
        next();
    }
});

router.afterEach(() => {
    console.log('Router after each');
});

export async function pruebaa(){
    const response = await fetch("http://127.0.0.1:5000/kodi/pelis")
    const body = await response.json()
    return body['result']['movies'];
  
  }


export const peliculas = [
    {
      id: 1,
      poster: "https://m.media-amazon.com/images/M/MV5BNGZiMzBkZjMtNjE3Mi00MWNlLWIyYjItYTk3MjY0Yjg5ODZkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_SX300.jpg",
      titulo: "vengadores"
    },
    {
      id:2,
      poster: "https://m.media-amazon.com/images/M/MV5BNGZiMzBkZjMtNjE3Mi00MWNlLWIyYjItYTk3MjY0Yjg5ODZkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_SX300.jpg",
      titulo: "vengadores 2"
    },
    {
      id:3,
      poster: "https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg",
      titulo: "vengadores 3"
    }
]


//////////////////////////////////////////

export const carrusel = [
    {
      id: 1,
      poster: "https://m.media-amazon.com/images/M/MV5BNGZiMzBkZjMtNjE3Mi00MWNlLWIyYjItYTk3MjY0Yjg5ODZkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_SX300.jpg",
      titulo: "Avatar",
      Description: "En un exuberante planeta llamado Pandora viven los Na'vi, seres que aparentan ser primitivos pero que en realidad son muy evolucionados. Debido a que el ambiente de Pandora es venenoso, los híbridos humanos/Na'vi, llamados Avatares, están relacionados con las mentes humanas, lo que les permite moverse libremente por Pandora. Jake Sully, unexinfante de marina paralítico se transforma a través de un Avatar, y se enamora de una mujer Na'vi.",
    },
    {
      id:2,
      poster: "https://m.media-amazon.com/images/M/MV5BNGZiMzBkZjMtNjE3Mi00MWNlLWIyYjItYTk3MjY0Yjg5ODZkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_SX300.jpg",
      titulo: "Parasitos",
      Description: "Tanto Gi Taek como su familia están sin trabajo. Cuando su hijo mayor, Gi Woo, empieza a recibir clases particulares en la adinerada casa de Park, las dos familias, que tienen mucho en común pese a pertenecer a dos mundos totalmente distintos, comienzan una relación de resultados imprevisibles."
    },
    {
      id:3,
      poster: "https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg",
      titulo: "Batman ",
      Description: "En su segundo año luchando contra el crimen, Batman explora la corrupción existente en la ciudad de Gotham y el vínculo de esta con su propia familia. Además, entrará en conflicto con un asesino en serie conocido como el Acertijo."
    }
]


const app = createApp(App)
app.config.globalProperties.foo = 'datoCompartido';

app.use(router)

app.mount('#app')


