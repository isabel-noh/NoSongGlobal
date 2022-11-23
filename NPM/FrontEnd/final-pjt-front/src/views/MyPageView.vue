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
        
      }
    },
    methods: {
      getProfileImg(){
        // const user_data = this.$store.state.token
        const user = localStorage.getItem('token')
        axios({
          mothod: 'GET',
          url: `${API_URL}/auth/mypage`,
          // headers:{
          //   'Authorization' : `Token ${user}`,
          // },
          data: {
            user_token: user,
          }
        })
        .then((response) => {
          console.log('axios요청 됨', response.data)
          // for (const j of response.data) {
          //   if (j.)
          // }
        })
      }
    },
    created(){
      this.$store.dispatch('isLogin')
      console.log('!', this.$store.state.token)
      this.getProfileImg()
    }
}
</script>

<style>

</style>