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
            @click="goToDetailPage(journal?.id)"
            v-for="journal in journalList" 
            :key="journal.pk" style="margin-bottom:10px;">
            <div class="container">
              <div class="card item front">
                <!-- <div 
                  class="item front"
                  v-if="!journal?.journal_image"
                  style="width: 100%; height: 100px; padding: 10px;"></div>
                <img
                  v-if="journal?.journal_image"
                  :src= "journal?.journal_image"
                  class="card-img-top" style="padding:10px;"> -->
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
              <div class="item back" v-if="journal?.journal_image">
                <!-- <img
                  
                  :src= "journal?.journal_image"
                  class="card-img-top item back"> -->
                <div
                class="card-img-top item back rounded-2"
                :style="{ backgroundImage:`url(${journal?.journal_image})`,
              backgroundSize: 'contain', backgroundRepeat: 'no-repeat', backgroundPosition: 'center'}"
                >
                </div>  
                
              </div>
              <div 
                class="item back" 
                style="margin-bottom:10px;"
                v-if="journal?.isActive_url">
                <div
                class="card-img-top item back rounded-2"
                :style="{ backgroundImage:`url(https://image.tmdb.org/t/p/w500/${journal?.poster_path})`,
              backgroundSize: 'contain', backgroundRepeat: 'no-repeat'}"
                >
                </div>  
                <!-- <img 
                  class="card-img-top item back"
                  :src="`https://image.tmdb.org/t/p/w500/${journal?.poster_path}`"> -->

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
        each_movie: null,
        isActive_url: null,
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
            if(j.journal_image !== null){
              j.journal_image = 'http://localhost:8000' + j.journal_image
              this.isActive_url = false
            } else {
              this.each_movie = j
              console.log(this.each_movie)
              // this.poster_url = 'https://image.tmdb.org/t/p/w500' + j.poster_path
              this.isActive_url = true
            }
            j['isActive_url'] = this.isActive_url
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

.container {
  width: 15rem;
  height: 20rem;
  /*        부모의 자식 요소가 3차원의 애니메이션 효과를 가질때, 300px의 거리에서 보는 원근감을 줌*/
  perspective: 300px;
}


.container .item.front {
  /* 앞면 카드가 부유하게 되어, 뒷면 카드가 아래에서 위로 올라감 -> 요소 두개가 겹치게 됨*/
  position: absolute;
  /* 명시적으로 기본값 설정, 없어도 됨*/
  transform: rotateY(0deg);
}

.container:hover .item.front {
  transform: rotateY(180deg);
  backface-visibility: hidden;
  transition: 1s;
}

.container .item.back {
  /*y축을 중심으로 -180도 회전*/
  transform: rotateY(-180deg);
  height: 20rem;
  width: 15rem;
  padding: 2px;
  /*카드의 뒷면을 안보이게 처리-카드가 뒤집히면 뒷면이 안보임*/
  backface-visibility: hidden;
  transition: 1s;
}

.container:hover .item.back {
  transform: rotateY(0deg);
  /* backface-visibility: hidden;
  transition: 1s; */
}

.card-img-top {
  height: 20rem;
  width: 15rem;
  object-fit: cover;
}

.card{
  height: 20rem;
  width: 15rem;
}

/* v-if="journal?.journal_image" */

</style>