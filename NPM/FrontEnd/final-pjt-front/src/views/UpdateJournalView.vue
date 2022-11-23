<template>
  <div class="update-journal-view">
    <h2>Edit My Movie Moment</h2>
    <div class="journal-form">
        <form @submit.prevent="updateJournal">
            <div class="content-div">
                <label for="journal_title" style="margin-right: 10px;">제목: </label>
                <input 
                    type="text" id="journal_title"
                    v-model="journal_title"
                    placeholder="글 제목을 입력해주세요">
            </div>
            <div class="content-div">
              <label for="movie-select" style="margin-right:10px;">영화: </label>
              <i>
                <input id="movie-select" 
                  :value="movie_title" 
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
            </div>
            <div class="content-div">
                <label for="watched_at" style="margin-right: 10px;">날짜:</label>
                <input type="date" id="watched_at"
                    v-model="watched_at" />
                    <!-- :value="{{journal?.watched_date}}"> -->
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
                <label for="journal_content" style="margin-right: 10px;">글 내용: </label>
                <textarea type="text" id="journal_content"
                    v-model="journal_content"
                    placeholder="글 내용을 입력해주세요"></textarea>
            </div>
            <div class="content-div">
                <label for="journal_image" style="margin-right: 10px;">이미지: </label>
                <input type="file" id="journal_image" 
                @change="encodeFileToBase64">
            </div>
            <div v-if="previous_image != null">
                <img :src="url_formatting">
            </div>
            <div v-if="{journal_image}">
                <img :src="uploadPreview" id="imgPreview">
            </div>
            <hr>
            <div>
                <button type="submit" class="btn btn-danger">수정하기</button>
            </div>
        </form>
    </div>
  </div>
    
</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'UpdateJournalView',
    data(){
        return{
            journal : null,
            journal_title : null,
            journal_content : null,
            journal_rank:0,
            movie_title : null,
            movie_id : null,
            journal_image : null,  // 새 이미지 
            uploadPreview : null,  // 새 이미지 preview
            previous_image : null,  // 전의 이미지
            watched_at : null,
            result:null,
            searchInput:null,
            isShow:false,
        }
    },
    methods: {
        deletePreviousImage(){
            this.previous_image = null
        },
        getJournal(){
            this.journal = this.$store.getters.aJournal
            console.log(this.journal)
            this.journal_title = this.journal?.title
            this.journal_content = this.journal?.content
            this.movie_id = this.journal?.movie
            this.movie_title = this.movieList[this.movie_id - 1].title
            this.journal_image = this.journal?.journal_image
            this.journal_rank = this.journal?.rank
            this.previous_image = this.journal?.journal_image
            this.watched_at = this.journal?.watched_at
        },
        updateJournal(){
            const movie_id = this.movie_id
            const journal_title = this.journal_title
            const journal_content = this.journal_content
            const journal_image = this.journal_image
            const journal_rank = this.journal_rank
            const watched_at = this.watched_at

            console.log(this.journal)
            const payload = {
                movie_id : movie_id,
                journal_title : journal_title,
                journal_content : journal_content,
                watched_at : watched_at,
                journal_image : journal_image,
                journal_rank : journal_rank,
                journal_id : this.journal.id
            }
            console.log(payload)
            this.$store.dispatch('updateJournal', payload)

        },

        encodeFileToBase64 (e){
            this.deletePreviousImage()
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
          this.movie_title = event.target.value
          if (this.movie_title) {
            this.isShow = true
            this.result = this.movieList.filter((movie) => {
              return movie.title.includes(this.movie_title)
            })
          } else {
            this.isShow = false
          }
        },
        searchInputChange(event) {
          console.log(event.target.innerHTML)
          console.log(event.target.value)
          this.movie_title = event.target.innerHTML
          this.movie_id = event.target.value
          this.isShow = false
        }
    },
    computed:{
      url_formatting: function(){
        // 이미지 경로가 서버에 저장된 경로로 불러와져 데이터 로드되지 않아
        // 경로에 'http://localhost:8000'를 붙여줘 computed로 계산된 값을 보여게 함
        let new_journal = ''
        new_journal = 'http://localhost:8000' + this.journal?.journal_image
        return new_journal
      },
      movieList() {
        return this.$store.getters.movieData
      },
    },
    created(){
        this.getJournal()
    },


}
</script>

<style>

</style>