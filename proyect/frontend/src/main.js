import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap';
import { createRouter, createWebHistory } from 'vue-router';
import fetch from 'node-fetch';

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
      path: '/informacionSeries/:id',
      name: 'informacionSeries',
      component: () => import('./components/InformacionSeries.vue')
    },
    {
        path:'',
        component: () => import('./components/PeliculasKoice.vue')
    }

]

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
      poster: "https://m.media-amazon.com/images/M/MV5BMDY4OTIwMTgtZTE1OC00ZjUwLWJhNzMtOWMxOGZiZGRiZmNiXkEyXkFqcGdeQXVyODIxOTM4MTk@._V1_.jpg",
      titulo: "vengadores 2"
    },
    {
      id:3,
      poster: "https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg",
      titulo: "vengadores 3"
    }
]

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
      }
  ]
  return peliculas2
  }
  

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


