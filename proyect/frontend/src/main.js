import {createApp} from 'vue'
import App from './App.vue'
import 'bootstrap';
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
{
        path: '/peliculas/:filter/:s',
        name: 'peliculas',
        component: () => import('./components/PeliculasKoice.vue')
    },
    {
        path: '/series/:s',
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

export function similaresPelis(){
  const similaresPeliculas = [
    {
      id: 1,
      poster: "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_Ratio0.6791_AL_.jpg",
      titulo: "Origen"
    },
    {
      id:2,
      poster: "https://flxt.tmsimg.com/assets/p14064584_v_v10_ad.jpg",
      titulo: "La forma del agua"
    },
    {
      id:3,
      poster: "https://flxt.tmsimg.com/assets/p14426291_p_v10_ad.jpg",
      titulo: "Lady Bird"
    },
    {
      id:4,
      poster: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIOfQ9D6z7hgFgxTt3EqEOBcKvpfslnjfbov6flHp5mZkWQX0nBjYNCz_UdfzxrlLQCD4&usqp=CAU",
      titulo: "Dune"
    },
    {
      id:5,
      poster: "https://flxt.tmsimg.com/assets/p16390_p_v12_ah.jpg",
      titulo: "Antes del amanecer"
    },
    {
      id:6,
      poster: "https://flxt.tmsimg.com/assets/p10213771_v_v10_ab.jpg",
      titulo: "El viento se levanta"
    }, 
]
return similaresPeliculas
}

export function similaresSeries(){
  const similaresSeriess = [
    {
      id: 1,
      poster: "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/es-es-vikingsvalhalla-main-vertical-4x5-rgb-pre-1644252019.jpg",
      titulo: "Vikings: Valhalla"
    },
    {
      id:2,
      poster: "https://as01.epimg.net/meristation/imagenes/2022/01/18/noticias/1642540022_359194_1642540142_sumario_normal.jpg",
      titulo: "The cuphead show"
    },
    {
      id:3,
      poster: "https://i1.wp.com/www.sopitas.com/wp-content/uploads/2021/11/Hellbound-Rumbo-al-infierno-Poster.jpeg",
      titulo: "Hellbound"
    },
    {
      id:4,
      poster: "https://preview.redd.it/yv34abpytjr61.jpg?auto=webp&s=1e2db51425b594ea0aacc9359077f3d3e0b5a4c1",
      titulo: "Shadow and bone"
    },
    {
      id:5,
      poster: "https://comoacaba.com/wp-content/uploads/2021/11/fqldf2t8ztc9aiwn3k6mlX3tvRT-2.jpg",
      titulo: "Arcane"
    },
    {
      id:6,
      poster: "https://es.web.img3.acsta.net/pictures/18/04/04/22/52/3191575.jpg",
      titulo: "Breaking bad"
    }, 
]
return similaresSeriess
}

export function reparto(){
  const actores = [
    {
      id: 1,
      foto: "https://www.alohacriticon.com/wp-content/uploads/2018/10/ryan-gosling-foto-biografia.jpg",
    },
    {
      id:2,
      foto: "https://www.alohacriticon.com/wp-content/uploads/2017/03/emma-stone-2017-foto.jpg",
    },
    {
      id:3,
      foto: "http://t1.gstatic.com/licensed-image?q=tbn:ANd9GcQ64o_4A3av1DMKUW2WI2gnwkoFXk6S4GDPlmhSjoxyohdBwB0frowykIG6C5tT",
    },
    {
      id:4,
      foto: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/JK_Simmons_2009.jpg/640px-JK_Simmons_2009.jpg",
    },
    {
      id:5,
      foto: "https://es.web.img2.acsta.net/pictures/15/12/03/15/55/425301.jpg",
    }
]
return actores
}

const app = createApp(App)
app.use(router)
app.mount('#app')


