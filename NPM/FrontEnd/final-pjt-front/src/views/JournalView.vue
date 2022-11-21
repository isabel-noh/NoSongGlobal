<template>
  <div class="journal">
    <div class="journal-header">
      <div>
        <h3>Remember Movie Moment</h3>

      </div>
      <div>
      <button 
        type="button" 
        class="btn btn-dark"
        @click="goAddJournalView"  
      >Add Moment</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'JournalView',
    methods: {
      goAddJournalView(){
        this.$router.push({name:'createJournal'})
      }
    }
}
</script>

<style>
.journal-header{
  display: flex;
  justify-content: space-between;
  font-family: 'Do Hyeon';
  padding: 10px 0px;
}
</style>