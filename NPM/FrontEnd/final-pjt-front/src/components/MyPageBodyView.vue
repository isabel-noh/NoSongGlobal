<!-- 
  - journal detail 이동 오류 수정
  - 페이지 새로고침 시 이미지 로드 되지 않는 오류 수정
-->

<template>
  <div class="MyPageBodyView">
    <MyJournalList v-if="comp_num === 1"/>          
    <LikeJournalList v-else-if="comp_num === 2"/>          
    <SettingsView v-else/>          
  </div>
</template>

<script>
import MyJournalList from '@/components/MyJournalList'
import LikeJournalList from '@/components/LikeJournalList'

export default {
    name:'MyPageBodyView',
    components: {
      LikeJournalList,
      MyJournalList
    },
    methods:{
      goToDetailPage(id){
        this.$router.push({name : 'journalDetail', params:{journal_id :id}})
      },
    },
    computed: {
      comp_num() {
        return this.$store.getters.tabNum
      }
    }
}
</script>

<style>

</style>