<template>
  <div class="MyPageBodyView">
    <MyJournalList v-if="comp_num === 1"/>          
    <LikeJournalList v-else-if="comp_num === 2"/>          
    <div v-else>
      <SettingsView v-if="!changeProfile"/>
      <div v-else>
        <div class="d-flex flex-column justify-content-center align-items-center mt-5" v-if="nop === 0">
          <button class="change_button btn btn-light m-3" @click="changeNickname">닉네임 변경</button>
          <button class="change_button btn btn-light m-3" @click="changePassword">비밀번호 변경</button>
        </div>
        <NicknameChange v-else-if="nop === 1"/>
        <ChangePassword v-else/>          
      </div>
    </div>
  </div>
</template>

<script>
import SettingsView from '@/components/SettingsView'
import MyJournalList from '@/components/MyJournalList'
import LikeJournalList from '@/components/LikeJournalList'
import SettingsView from '@/views/SettingsView'
import ChangePassword from '@/components/ChangePassword'
import NicknameChange from '@/components/NicknameChange'

export default {
    name:'MyPageBodyView',
    data(){
      return{
      }
    },
    components: {
      NicknameChange,
      ChangePassword,
      SettingsView,
      LikeJournalList,
      MyJournalList
    },
    
    props: {
      userJournalList:Array,
    },
    methods:{
      goToDetailPage(id){
        this.$router.push({name : 'journalDetail', params:{journal_id :id}})
      },
      changeNickname(){
        this.$store.commit('CHANGE_NOP', 1)
      },
      changePassword(){
        this.$store.commit('CHANGE_NOP', 2)
      },
      created() {
      this.$store.commit('USER_JOURNAL_LIST', this.userJournalList)
      },
    },
    computed: {
      comp_num() {
        return this.$store.getters.tabNum
      },
      changeProfile() {
        return this.$store.getters.changeProfile
      },
      nop() {
        return this.$store.getters.nop
      }
    }
}
</script>

<style>
.change_button {
  width:8rem;
  height:3rem;
}
</style>