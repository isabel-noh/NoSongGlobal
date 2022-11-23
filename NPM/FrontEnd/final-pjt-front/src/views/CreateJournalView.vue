color: black;
<template>
  <div class="create-journal-view">
    <h2>Add My Movie Moment</h2>
    <div class="journal-form">
        <form @submit.prevent="addJournal" >
            <div class="content-div">
                <label for="journal_title" style="margin-right:10px;">제목: </label>
                <input 
                    id="journal_title" type="text" 
                    v-model="journal_title"
                    placeholder="글 제목을 입력해주세요">
            </div>
            <div class="content-div">
              <label for="movie-select" style="margin-right:10px;">영화: </label>
              <i>
                <input id="movie-select" 
                  :value="searchInput" 
                  @input="submitAutoComplete" 
                  placeholder="시청한 영화 제목을 입력해주세요"
                  type="text"/>
              </i>
              <div v-show="isShow">
                <option
                  class="border border-dark"
                  @click="searchInputChange"
                  v-for="(res,i) in result"
                  :key="i"
                  :value="res.id"
                  style="width:400px; margin-left:90px;"
                  >{{ res.title }}
                </option>
              </div>
                <!-- <label for="movie_title" style="margin-right:10px;">영화 제목: </label>
                <input 
                    id="movie_title"
                    type="text" v-model="movie_title" placeholder="영화제목을 선택해주세요"> -->
            </div>
            <div class="content-div">
                <label for="journal_date" style="margin-right:10px;">날짜: </label>
                <input
                    id="journal_date" 
                    type="date" v-model="journal_date">
            </div>
            <div class="content-div d-flex">
              <span>별점: </span>
              <div class="d-flex star-div">
                <div
                v-for="index in 5"
                :key="index"
                @click="check(index)"
                >
                <span v-if="index <= journal_rank">⭐</span>
                <span v-if="index > journal_rank"><img class="star" :src="require('@/assets/dark_star.png')" alt=""></span>
                </div>
              </div>
            </div>
            <div class="content-div">
                <label for="journal_content" style="margin-right:10px;">글 내용</label>
                <div class="form-floating">
                    <textarea class="form-control" 
                    v-model="journal_content"
                    placeholder="공유하고 싶은 내용을 입력해주세요" id="floatingTextarea2" style="height: 100px"></textarea>
                    <label for="floatingTextarea2">Content</label>
                </div>
                <!-- <div>
                    <textarea
                        id="journal_content"
                        v-model="journal_content"
                        placeholder="공유하고 싶은 내용을 입력해주세요"></textarea>
                </div> -->
            </div>
            <div class="content-div">
                <label for="setImg" style="margin-right:10px;">이미지: </label>
                <input 
                    id="setImg"
                    type="file"  
                    @change="encodeFileToBase64"
                    style="width:170px">
                <div id="imgPreview-box" v-if="{uploadPreview}">
                    <img :src="uploadPreview" id="imgPreview">
                </div>
            </div>
            <input type="submit" value="전송">
        </form>
    </div>
  </div>
</template>

<script>
export default {
    name: 'CreateJournalView',
    data(){
        return{
            journal_title:null,
            journal_content:null,
            journal_date:null,
            journal_img:null,
            journal_rank:0,
            uploadPreview:null,
            result:null,
            searchInput:null,
            selectedMovieId:null,
            isShow:false,
        }
    },
    methods:{
        addJournal(){
            const movie_id = this.selectedMovieId
            const journal_title = this.journal_title
            const journal_content = this.journal_content
            const journal_date = this.journal_date
            const journal_img = this.journal_img
            const journal_rank = this.journal_rank
            const data = {
                movie_id,
                journal_title,
                journal_content,
                journal_date,
                journal_img,
                journal_rank,
            }
            this.$store.dispatch('addJournal', data)
        },
        encodeFileToBase64 (e){
            const reader = new FileReader()
            const file = (e.target.files[0])
            this.journal_img = e.target.files[0]
            reader.readAsDataURL(file);
            return new Promise (() => {
                reader.onload = () => {
                    this.uploadPreview = reader.result;
                }
            })
        },
        check(index) {
            this.journal_rank = index
        },
        submitAutoComplete(event) {
          this.searchInput = event.target.value
          if (this.searchInput) {
            this.isShow = true
            this.result = this.movieList.filter((movie) => {
              return movie.title.includes(this.searchInput)
            })
          } else {
            this.isShow = false
          }
        },
        searchInputChange(event) {
          console.log(event.target.innerHTML)
          console.log(event.target.value)
          this.searchInput = event.target.innerHTML
          this.selectedMovieId = event.target.value
          this.isShow = false
        }
        
    },
    computed: {
      movieList() {
        return this.$store.getters.movieData
      }
    },
    mounted(){
      var now_utc = Date.now()
      var timeOff = new Date().getTimezoneOffset()*60000;
      var today = new Date(now_utc-timeOff).toISOString().split("T")[0];
      document.getElementById("journal_date").setAttribute("max", today);
        }
}
</script>

<style>
.star {
  height: 18px;
  width: 18px;
  margin: 2px;
}
.star-div {
  margin-left: 4rem;
}
.create-journal-view{
    font-family: 'Do Hyeon';
}
.journal-form{
    max-width: 500px;
    margin: 10px auto;
}
.content-div{
    margin: 5px auto;
    width: 100%;
    text-align: start;
}
.content-div input{
    width: 80%;
}
.content-div label{
    width: 16%;
}
.content-div textarea{
    width: 100%;
    min-height: 100px;
}
#imgPreview{
    width: 100%;
    height: auto;
    margin: 0px auto;
}
</style>