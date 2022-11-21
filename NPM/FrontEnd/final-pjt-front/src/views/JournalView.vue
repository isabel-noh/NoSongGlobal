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
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'JournalView',
    data(){
      return{
        journalList: [],
      }
    },
    methods: {
      goAddJournalView(){
        this.$router.push({name:'createJournal'})
      },
      getJournalAll(){
        console.log('created')
        axios({
          method: 'GET',
          url: `${API_URL}/journal/all/`
        })
        .then((response) => {
          console.log(response.data)
        })
        .catch((error) => {
          console.log(error)
        })
      },
    },
    created(){
      this.getJournalAll()
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