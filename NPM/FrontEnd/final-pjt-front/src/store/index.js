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
    journalList: [],
    userJournalList: [],
    likeJournalList: [],
    tabNum: 1,
    NicknameOrPassword: 0,
    changeProfile: false,
    myPageComponent : 0
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
    },
    journalList(state) {
      return state.journalList
    },
    userJournalList(state) {
      return state.userJournalList
    },
    likeJournalList(state) {
      return state.likeJournalList
    },
    tabNum(state) {
      return state.tabNum
    },
    changePassword(state) {
      return state.changePassword
    },
    changeProfile(state) {
      return state.changeProfile
    },
    nop(state) {
      return state.NicknameOrPassword
    },
    myPageComponent(state){
      return state.myPageComponent
    }

  },
  mutations: {
    IS_LOGIN(state, data){
      state.user = data
    }
    ,
    LOG_IN(state, data){
      state.token = data.key
      // state.user = data.user
      if(router.currentRoute.name == 'myPage'){
        state.changeProfile = true
        state.NicknameOrPassword = 0
      }
      else if(router.currentRoute.name != 'home'){
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
      const recommend_data = data
      console.log(recommend_data)
      for(const j of recommend_data) {
        console.log(j)
        let temp = j.overview.split(' ')
        temp = temp.slice(0, 5)
        j.overview = temp.join(' ')
      }
      state.recommendMovieList = recommend_data 
    },
    JOURNAL_LIST(state, data) {
      state.journalList = data
    },
    USER_PROFILE(state, data) {
      state.user['profileImg'] = data.profile_image
    },
    USER_JOURNAL_LIST(state, data) {
      state.userJournalList = data
    },
    LIKE_JOURNAL_LIST(state, data) {
      state.likeJournalList = data
    },
    TAB_NUM(state, num){
      if (num === 3) state.changeProfile = false
      state.tabNum = num
    },
    CHANGE_NOP(state, num) {
      state.NicknameOrPassword = num
    },
    MY_PAGE_COMPONENT(state, num){
      state.myPageComponent = num
    }
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
          console.log(response)
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
        context.commit('LOG_IN', response.data)
        context.dispatch('isLogin')
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
      
    },
    changePassword(context, newPassword) {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/password/change/',
        headers: {
          Authorization : `Token ${context.state.token}`
        },
        data: {
          new_password1 : newPassword.new_password1,
          new_password2 : newPassword.new_password2,
        }
      })
      .then((res) => {
        console.log(res)
        context.state.changePassword = false
        context.state.tabNum = 1
        alert('비밀번호 수정 완료!')
      })
      .catch((err) => {
        console.log(err)
        alert('비밀번호 수정에 실패하였습니다!')
      })
    },
    updateNickname(context, nickname) {
      console.log(context.state.user)
      axios({
        method: 'PUT',
        url: `${API_URL}/auth/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
        data: {
          'user':context.state.user.id,
          'nickname':nickname,
          'name':context.state.user.username
        }
      })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },

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
      console.log(formdata)
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
      if(user?.token){
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
          console.log(res.data)
          const recommendMovieList = [] 
          for (const id in res.data.recommendMovieList) {
            recommendMovieList.push(context.state.movieList[res.data.recommendMovieList[id]])
          }
          context.commit('RECOMMEND_MOVIE_LIST', recommendMovieList)
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    loadJournalList(context) {
      axios({
          method: 'GET',
          url: `${API_URL}/journals/`
      })
      .then((response) => {
        let journalList = []
        let isActive_url = false
        for (const j of response.data){
          if(j.journal_image !== null){
            j.journal_image = 'http://localhost:8000' + j.journal_image
            isActive_url = false
          } else {
            j['poster_path'] = 'https://image.tmdb.org/t/p/w500' + j.poster_path
            isActive_url = true
          }
          j['isActive_url'] = isActive_url
          j['movieTitle'] = context.state.movieList[j.movie_id-1].title
          journalList.push(j)
        }
        context.commit('JOURNAL_LIST', journalList)
      })
      .catch((error) => {
        console.log(error)
      })
    },
  },
  modules: {
    
  }
})
