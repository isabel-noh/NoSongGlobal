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
    user:{},
    movieList: [],
    searchList: [],
    journal: null,
    recommendMovieList: null,
  },
  getters: {
    userData(state){
      return state.user ? state.user : ''
    },
    isLogin(state) {
      return state.token ? true : false
    },
    movieData(state) {
      return state.movieList
    },
    aJournal(state){
      return state.journal
    },
    getRecommendMovieList(state){
      return state.recommendMovieList
    }

  },
  mutations: {
    IS_LOGIN(state, data){
      state.user = data
    }
    ,
    LOG_IN(state, data){
      state.token = data.key
      state.user = data.user
      if(router.currentRoute.name != 'home'){
        router.push({ name : 'home' })
      } else {
        router.go(router.currentRoute)
      }
    }, 
    SEARCH_RESULT(state, data){
      state.searchList = data
      if(router.currentRoute.name != 'home'){
        router.push({ name : 'home' })
      } else {
        router.go(router.currentRoute)
      }
    },
    LOG_OUT(state){
      state.token = null
      state.user = null
      if(router.currentRoute.name != 'home'){
        router.push({ name : 'home' })
      } else {
        router.go(router.currentRoute)
      }
    },
    SET_MOVIE_LIST(state, data){
      const objectToList = []
      for (const idx in data) {
        objectToList.push(data[idx]) 
      }
      state.movieList = objectToList
    },
    GET_JOURNAL(state, data){
      state.journal = data
    },
    RECOMMEND_MOVIE_LIST(state, data){
      state.recommendMovieList = data.recommendMovieList
    },
  },
  actions: {
    isLogin(context){
      const local = localStorage.getItem('vuex')
      const user = JSON.parse(local)
      if (user.token){
        axios({
          method:'GET',
          url: `${API_URL}/auth/isLogin/`,
          headers: {
            'Authorization': `Token ${user.token}`
          }
        })
        .then((response) => {
          // console.log('islogin 됨')
          // console.log('->', user.token)
          context.commit('IS_LOGIN', response.data)
        })
        .catch((error) => {
          // console.log('islogin 안됨')
          console.log(error)
        })
      }
    },

    logIn(context, userData) {
      axios({
        method:'POST',
        url:`${API_URL}/accounts/login/`,
        data: {
          username: userData.username,
          password: userData.password
        }
      })
      .then((response) => {
        context.dispatch('isLogin')
        context.commit('LOG_IN', response.data)
      })
      .catch((error) => {
        alert('유저정보를 확인해주세요.')
        console.log(error)
      })
    },

    logOut(context) {
      const local = localStorage.getItem('vuex')
      const user = JSON.parse(local)
      axios({
        method: 'POST',
        url: `${API_URL}/accounts/logout/`,
        headers:{
          'Authorization': `Token ${user.token}`
        }
      })
      .then(() => {
        localStorage.removeItem('vuex')
        context.commit('LOG_OUT')
      })
      .catch((error) => {
        alert('로그아웃을 실패하였습니다.')
        console.log(error)
      })
      
    }
    ,
    search(context, keyword){
      axios({
        method: 'GET',
        url: `${API_URL}/movies/movieList`,
        params:{
          keyword:keyword
        }
      })
      .then((response) => {
        context.commit('SEARCH_RESULT', response.data)
      })
      .catch((error) => {
        console.log(error)
      })
    },

    addJournal(context, data){
      const formdata = new FormData()
      formdata.append('title', data.journal_title)
      formdata.append('content', data.journal_content)
      formdata.append('movie_id', data.movie_id)
      formdata.append('watched_at', data.journal_date)
      formdata.append('journal_image', data.journal_img)
      formdata.append('journal_rank', data.journal_rank)
      const local = localStorage.getItem('vuex')
      const user = JSON.parse(local)

      axios({
        method:'POST',
        url:`${API_URL}/journals/create/`,
        headers:{
          'Content-Type': 'multipart/form-data',
          'Authorization': `Token ${user.token}`,
        },
        data: 
          formdata,
      })
      .then((res) => {
        console.log(res.data)
        router.push({name : 'journalDetail', params:{journal_id : res.data.id}})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    updateJournal(context, data){
      const formdata = new FormData()
      formdata.append('title', data.journal_title)
      formdata.append('content', data.journal_content)
      formdata.append('movie', data.movie_id)
      formdata.append('user', context.state.user.user_id)
      formdata.append('watched_at', data.watched_at)
      formdata.append('journal_image', data.journal_image)
      formdata.append('rank', data.journal_rank)
      formdata.append('movie_id', data.movie_id)
      formdata.append('journal_pk', data.journal_id)
      const local = localStorage.getItem('vuex')
      const user = JSON.parse(local)

      axios({
        method: 'PUT',
        url: `${API_URL}/journals/${data.journal_id}/detail/`,
        headers:{
            'Content-Type': 'multipart/form-data',
            'Authorization' : `Token ${user.token}`
        },
        data: 
          formdata,
      })
      .then((res) => {
        router.push({name : 'journalDetail', params:{journal_id : res.data.id}})
      })
      .catch((err) => {
        console.log(err)
      })
    
    }
    ,
    // TODO 영화 데이터 가져오기
    loadMovieData(context) {
      axios({
        method:'GET',
        url: `${API_URL}/movies/get_movie_data/`
      })
      .then((response) => {
        context.commit('SET_MOVIE_LIST', response.data)
      })
      .catch((error) => {
          console.log(error)
      })
    },
    recommendMovie(context) {
      const local = localStorage.getItem('vuex')
      const user = JSON.parse(local)
      if(user.token){
        axios({
          method:'POST',
          url: `${API_URL}/auth/get_user_data/`,
          headers: {
            Authorization: `Token ${user.token}`
          },
          data: {
            user_id: user.user_id
          }
        })
        .then((res) => {
          context.commit('RECOMMEND_MOVIE_LIST', res.data)
        })   
      }
    }
  },
  modules: {
    
  }
})
