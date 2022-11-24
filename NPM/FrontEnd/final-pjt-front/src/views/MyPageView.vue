<template>
  <div class="myPage">
    <MyPageHeader

    />
    <MyPageTabbar @changeComponent="changeComponent"/>
    <MyPageBodyView :userJournalList="userJournalList" :comp_num="comp_num"/>
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
        userJournalList: [],
        comp_num : 1,
      }
    },
    methods: {
      changeComponent(num){
        this.comp_num = num
      },
      getProfileImg(){
        axios({
          mothod: 'GET',
          url: `${API_URL}/auth/mypage/`,
          headers:{
            'Authorization' : `Token ${this.$store.state.token}`,
          },
        })
        .then((response) => {
          this.$store.commit('USER_PROFILE', response.data.serializer_add)
          
        })
        .catch((err) => {
          console.log(err, 1)
        })
      }
    },
    created(){
      this.$store.dispatch('isLogin')
      this.getProfileImg()
      const userJournalList = this.$store.getters.journalList.filter((journal)=>{
        return journal.user_id == this.$store.getters.userData.user_id
      })
      this.userJournalList =  userJournalList 
      console.log(this.userJournalList)
    }
}
</script>

<style>

</style>