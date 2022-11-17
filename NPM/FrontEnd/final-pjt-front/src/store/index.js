import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from "vuex-persistedstate";
// import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    LOG_IN(state, token){
      state.token = token
      this.$router.push({ name : 'home' })
    }
  },
  actions: {
    signUp(context, userData) {
      axios({
        method: 'POST',
        url: `${API_URL}/accounts/signup`,
        data: {
          name: userData.name,
          nickname: userData.nickname,
          email: userData.email,
          password1: userData.password1,
          password2: userData.password2,
          preferMusicGenre: userData.preferMusicGenre
        }
      }).
      then(() => {
        this.$router.push({ name: 'login'})
      }).
      catch((error) => {
        console.log(error)
      })
    },
    logIn(context, userData) {
      axios({
        method: 'POST',
        urls: `${API_URL}/accounts/logIn`,
        data: {
          username: userData.username,
          password: userData.password,
        }
      })
      .then((response) => {
        console.log(response)
        context.commit('LOG_IN', response.data)
      })
      .catch((error) => {
        alert('유저정보를 확인해주세요.')
        console.log(error)
      })
    }
  },
  modules: {
    
  }
})
