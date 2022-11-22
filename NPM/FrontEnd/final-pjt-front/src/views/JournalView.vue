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
        <button class="btn btn-bright"
          style="font-family: 'Do Hyeon';">최신순</button>
        <button class="btn btn-bright"
          style="font-family: 'Do Hyeon';">인기순</button>
      </div>
    </div>
    <div class="journal-lists">
        <div class="row row-cols-1 row-cols-md-3">
          <!-- 아래 반복 -->
          <div class="col" 
            @click="goToDetailPage(journal?.pk)"
            v-for="journal in url_formatting" 
            :key="journal.pk" style="margin-bottom:10px;">
            <div class="card">
              <div 
                v-if="!journal?.journal_image"
                style="width: 100%; height: 100px; padding: 10px;"></div>
              <img
                v-if="journal?.journal_image"
                :src="journal?.journal_image" class="card-img-top" style="padding:10px;">
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
        axios({
          method: 'GET',
          url: `${API_URL}/journals/`
        })
        .then((response) => {
          console.log(response.data)
          this.journalList = response.data
        })
        .catch((error) => {
          console.log(error)
        })
      },
      goToDetailPage(id){
        console.log(id)
        this.$router.push({name : 'journalDetail', params:{journal_id :id}})
      }
    },
    
    computed:{
      url_formatting: function(){
        const new_journaList = []
        for (const j of this.journalList){
          if(j.journal_image !== null){
            j.journal_image = 'http://localhost:8000' + j.journal_image
          }
          new_journaList.push(j)
        }
        return new_journaList
      }
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