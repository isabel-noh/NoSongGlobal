<template>
  <div class="MyPageBodyView">
    MyPageBodyView
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name:'MyPageBodyView',
    components: {
    },
    methods:{
      getUser(){
        const local = localStorage.getItem('vuex')
        const user = JSON.parse(local)
        axios({
          method: 'GET',
          url: `${API_URL}/useraddfields/mypage/`,
          headers: {
            'Authorization' : `Token ${user.token}`
          }
        })
        .then((response) => {      
          console.log(response.data)
        })
        .catch((error) => {
            console.log(error)
        })
      }
    }
}
</script>

<style>

</style>