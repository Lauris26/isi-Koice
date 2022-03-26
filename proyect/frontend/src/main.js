import {createApp} from 'vue'
import App from './App.vue'
import 'bootstrap';
import { createRouter, createWebHistory } from 'vue-router';

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
        path: '/informacion/:id',
        name: 'informacion',
        component: () => import('./components/InformacionElemento.vue')
    },
    {
      path: '/informacionSeries/:id',
      name: 'informacionSeries',
      component: () => import('./components/InformacionSeries.vue')
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


export function obtenerPelis(){
    const peliculas2 = [
      {
        id: 1,
        poster: "https://m.media-amazon.com/images/M/MV5BNGZiMzBkZjMtNjE3Mi00MWNlLWIyYjItYTk3MjY0Yjg5ODZkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_SX300.jpg",
        titulo: "vengadores"
      },
      {
        id:2,
        poster: "https://m.media-amazon.com/images/M/MV5BMDY4OTIwMTgtZTE1OC00ZjUwLWJhNzMtOWMxOGZiZGRiZmNiXkEyXkFqcGdeQXVyODIxOTM4MTk@._V1_.jpg",
        titulo: "vengadores 2"
      },
      {
        id:3,
        poster: "https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg",
        titulo: "vengadores asdfasdf"
      },
      {
        id:4,
        poster: "https://m.media-amazon.com/images/M/MV5BMDY4OTIwMTgtZTE1OC00ZjUwLWJhNzMtOWMxOGZiZGRiZmNiXkEyXkFqcGdeQXVyODIxOTM4MTk@._V1_.jpg",
        titulo: "vengadores hasta el infinito"
      },
      {
        id:5,
        poster: "https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg",
        titulo: "vengadores super guays"
      },
      {
        id:6,
        poster: "https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg",
        titulo: "esto no se deberia de ver"
      }
  ]
  return peliculas2
  }

const app = createApp(App)
app.use(router)
app.mount('#app')


