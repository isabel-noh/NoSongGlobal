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
          <div class="col" v-for="journal in url_formatting" :key="journal.journal_pk">
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
    computed:{
<<<<<<< HEAD
      url_formatting: function(){
        const new_journaList = []
        for (const j of this.journalList){
          j.journal_image = 'http//localhost:8000' + j.journal_image
          new_journaList.push(j)
        }
        return new_journaList
=======
      url_formatting: function () {
        const new_journalList = []
        for( const j of this.journalList){
          j.journal_image = 'http://localhost:8000' + j.journal_image
          new_journalList.push(j)
        }

        return new_journalList


        // /media/None/%EC%A0%9C%EB%AA%A9_%EC%97%86%EB%8A%94_%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8.drawio_t20fT4j.png
        // return /http://localhost:8000/media/None/%EC%A0%9C%EB%AA%A9_%EC%97%86%EB%8A%94_%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8.drawio_t20fT4j.png
>>>>>>> 492d008cdf1a708f429a6c946332fae97e4fc0eb
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