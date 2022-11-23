<template>
  <div class="myPage">
    <MyPageHeader

    />
    <MyPageTabbar/>
    <MyPageBodyView/>
  </div>
</template>

<script>
import MyPageHeader from '@/components/MyPageHeader'
import MyPageTabbar from '@/components/MyPageTabbar'
import MyPageBodyView from '@/components/MyPageBodyView'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name:'MyPageView',
    components: {
      MyPageHeader,
      MyPageTabbar,
      MyPageBodyView,
    },
    data() {
      return{
        // user: localStorage.getItem('token')
      }
    },
    methods: {
      getProfileImg(){
        axios({
          mothod: 'GET',
          url: `${API_URL}/auth/mypage`,
          // headers: {
          //   'Authorization' : `Token ${this.user}`,
          // }
        })
        .then((response) => {
          console.log(response.data)
          // for (const j of response.data) {
          //   if (j.)
          // }
        })
      }
    },
    created(){
      this.$store.dispatch('isLogin')
      this.getProfileImg()
    }
}
</script>

<style>

</style>