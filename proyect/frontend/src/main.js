import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap';
import { createRouter, createWebHistory } from 'vue-router';
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
        path: '/informacion',
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

const app = createApp(App)
app.use(router)

app.mount('#app')


