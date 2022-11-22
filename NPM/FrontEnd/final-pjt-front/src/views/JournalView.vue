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
          @click="goAddJournalView">Add Moment</button>
      </div>
    </div>
    <div class="journal-lists">
        <div class="row row-cols-1 row-cols-md-3">
          <!-- 아래 반복 -->
          <div class="col" v-for="journal in journalList" :key="journal.journal_pk">
            <div class="card">
              <img :src="journal.journal_image" class="card-img-top" style="padding:10px;">
              <div class="card-body">
                <h5 class="card-title">{{journal.title}}</h5>
                <p class="card-text">{{journal.movie_title}}</p>
              </div>
              <div class="card-footer">
                <small class="text-muted">
                  {{journal.watched_at}}
                </small>
              </div>
            </div>
          </div>
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
          url: `${API_URL}/journals/`
        })
        .then((response) => {
          this.journalList = response.data
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
  margin-bottom: 10px;
}
</style>