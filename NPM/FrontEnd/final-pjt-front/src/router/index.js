import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'
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
    path: '/mypage',
    name: 'myPage',
    component: () => import('../views/MyPageView.vue'),
    beforeEnter(to, from, next){
      const isLoggedIn = store.getters.isLogin
      if(isLoggedIn === true){
        next()
      } else {
        alert('로그인된 회원님만 마이페이지를 볼 수 있어요.')
        next({ name : 'home' })
      }
    }
  },
  {
    path: '/info',
    name: 'info',
    component: () => import('../views/InfoView.vue')
  },
  {
    path: '/addJournal',
    name: 'createJournal',
    component: CreateJournalView,
    beforeEnter(to, from, next){
      const isLoggedIn = store.getters.isLogin
      if(isLoggedIn === true){
        next()
      } else {
        alert('글 작성을 위해서 로그인을 해주세요.')
        next({ name : 'journal' })
      }
    }
  },
  {
    path: '/journal',
    name: 'journal',
    component: () => import('../views/JournalView.vue')
  },
  {
    path: '/journal/:journal_id',
    name: 'journalDetail',
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
