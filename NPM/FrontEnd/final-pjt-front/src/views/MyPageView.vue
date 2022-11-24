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
        // const user = localStorage.getItem('token')
        // console.log('!', user)
        axios({
          mothod: 'GET',
          url: `${API_URL}/auth/mypage/`,
          headers:{
            'Authorization' : `Token ${this.$store.state.token}`,
          },
        })
        .then((response) => {
          console.log('axios요청 됨', response.data)
          
        })
        .catch((err) => {
          console.log(err)
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