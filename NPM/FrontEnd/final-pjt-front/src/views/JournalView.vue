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
    <div>
      <div style="display:flex; margin-bottom: 20px;">
        <button 
          class="btn btn-bright"
          style="font-family: Do Hyeon"
          @click="getListNewest">최신순</button>
        <button 
          style="font-family: Do Hyeon"
          class="btn btn-bright"
          @click="getListPopluar">인기순</button>
      </div>
    </div>
    <div class="journal-lists">
        <div class="row row-cols-1 row-cols-md-3">
          <!-- 아래 반복 -->
          <div class="col" 
            @click="goToDetailPage(journal?.pk)"
            v-for="journal in journalList" 
            :key="journal.pk" style="margin-bottom:10px;">
            <div class="card">
              <div 
                v-if="!journal?.journal_image"
                style="width: 100%; height: 100px; padding: 10px;"></div>
              <img
                v-if="journal?.journal_image"
                :src= "journal?.journal_image" class="card-img-top" style="padding:10px;">
              <div class="card-body">
                <h5 class="card-title">{{journal.title}}</h5>
                <p class="card-text">{{journal.movieTitle}}</p>
              </div>
              <div class="card-footer">
                <small class="text-muted">
                  date: {{journal.watched_at}}
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
        axios({
          method: 'GET',
          url: `${API_URL}/journals/`
        })
        .then((response) => {
          for (const j of response.data){
            console.log(j)
            if(j.journal_image !== null){
              j.journal_image = 'http://localhost:8000' + j.journal_image
            }
            j['movieTitle'] = this.movieList[j.movie_id-1].title
            this.journalList.push(j)
          }
        })
        .catch((error) => {
          console.log(error)
        })
      },
      getListNewest(){
        this.journalList = this.journalList.sort((a, b) => b.pk - a.pk)
      },
      getListPopluar(){

      },
      goToDetailPage(id){
        this.$router.push({name : 'journalDetail', params:{journal_id :id}})
      },
      
    },
    
    computed:{
      movieList() {
        return this.$store.getters.movieData
      }
    },
    created(){
      this.getJournalAll()
    },
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