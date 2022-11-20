import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';
import createPersistedState from "vuex-persistedstate";
import router from '@/router'

Vue.use(Vuex)


const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    token: null,
    nickname: null,
    movieList: [],
    soundtrackList: [],
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },

  },
  mutations: {
    LOG_IN(state, data){
      state.token = data.key
      state.nickname = data.nickname
      if(router.currentRoute.name != 'home'){
        router.push({ name : 'home' })
      } else {
        router.go(router.currentRoute)
      }
    }, 
    SEARCH_RESULT(state, data){
      state.movieList = data
      if(router.currentRoute.name != 'home'){
        router.push({ name : 'home' })
      } else {
        router.go(router.currentRoute)
      }
    },
  },
  actions: {
    signUp(context, userData) {
      axios({
        method: 'POST',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: userData.email,
          name: userData.name,
          nickname: userData.nickname,
          email: userData.email,
          password1: userData.password1,
          password2: userData.password2,
          preferMusicGenre: userData.preferMusicGenre
        }
      }).
      then(() => {
        router.push({ name: 'home'})
      }).
      catch((error) => {
        console.log(error)
      })
    },
    logIn(context, userData) {
      console.log(userData)
      axios({
        method:'POST',
        url:`${API_URL}/accounts/login/`,
        data: {
          username: userData.username,
          password: userData.password
        }
      })
      .then((response) => {
        context.commit('LOG_IN', response.data)
      })
      .catch((error) => {
        alert('유저정보를 확인해주세요.')
        console.log(error)
      })
      
    },
    logOut() {
      localStorage.removeItem('vuex')
      if(router.currentRoute.name != 'home'){
        router.push({ name : 'home' })
      } else {
        router.go(router.currentRoute)
      }
    }
    ,
    search(context, keyword){
      axios({
        method: 'GET',
        url: `${API_URL}/movieList`,
        params:{
          keyword:keyword
        }
      })
      .then((response) => {
        console.log(response.data)
        context.commit('SEARCH_RESULT', response.data)
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  modules: {
    
  }
})
