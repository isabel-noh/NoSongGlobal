import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import NotFound404View from '@/views/NotFound404View.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/signUp',
    name: 'signUp',
    component: SignUpView
  },
  {
    path: '/mypage',
    name: 'myPage',
    component: () => import('../views/MyPageView.vue')
  },
  {
    path: '/info',
    name: 'info',
    component: () => import('../views/InfoView.vue')
  },
  {
    path: '/journal',
    name: 'journal',
    component: () => import('../views/JournalView.vue')
  },
  {
    path: '/404NotFound',
    name: 'notfound',
    component: NotFound404View,
  },
  {
    path: '*',
    redirect: '/404NotFound'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
