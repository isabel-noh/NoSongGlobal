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
      const journalList = this.$store.getters.journalList
      const userJournalList = journalList.filter((journal)=>{
        return journal.user_id == this.$store.getters.userData.user_id
      })
      this.$store.commit('USER_JOURNAL_LIST', userJournalList)
      const likeJournalList = journalList.filter((journal => {
        return journal.like_users.includes(this.$store.getters.userData.user_id)
      }))
      this.$store.commit('LIKE_JOURNAL_LIST', likeJournalList)
  }
}
</script>

<style>

</style>