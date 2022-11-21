import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import CreateJournalView from '@/views/CreateJournalView'
import SignUpView from '@/views/SignUpView.vue'
import NotFound404View from '@/views/NotFound404View.vue'
import JournalDetailView from '@/views/JournalDetailView'

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
    path: '/movie/:movie_id',
    name: 'movieDetail',
    component: MovieDetailView,
  },
  {
    path: '/addJournal',
    name: 'createJournal',
    component: CreateJournalView,
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
    path: '/journal/:journal_id',
    name: 'journal',
    component: JournalDetailView,
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
