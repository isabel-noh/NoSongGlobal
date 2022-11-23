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
                <label for="movie_title" style="margin-right: 10px;">영화 제목: </label>
                <input type="text" id="movie_title"
                    v-model="movie_title"
                    placeholder="영화 제목을 입력해주세요">
            </div>
            <div class="content-div">
                <label for="watched_at" style="margin-right: 10px;">날짜:</label>
                <input type="date" id="watched_at"
                    v-model="watched_at" />
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
            movie_title : null,
            journal_image : null,  // 새 이미지 
            uploadPreview : null,  // 새 이미지 preview
            previous_image : null,  // 전의 이미지
            watched_at : null,
        }
    },
    methods: {
        deletePreviousImage(){
            this.previous_image = null
        },
        getJournal(){
            this.journal = this.$store.getters.aJournal
            this.journal_title = this.journal?.title
            this.journal_content = this.journal?.content
            this.movie_title = this.journal?.movie_title
            this.journal_image = this.journal?.journal_image
            this.previous_image = this.journal?.journal_image
            this.watched_at = this.journal?.watched_at
        },
        updateJournal(){
            const journal_title = this.journal_title
            const journal_content = this.journal_content
            const movie_title = this.movie_title
            const journal_image = this.journal_image
            const watched_at = this.watched_at

            const payload = {
                movie_title : movie_title,
                journal_title : journal_title,
                journal_content : journal_content,
                watched_at : watched_at,
                journal_image : journal_image,
            }
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
    },
    computed:{
      url_formatting: function(){
        // 이미지 경로가 서버에 저장된 경로로 불러와져 데이터 로드되지 않아
        // 경로에 'http://localhost:8000'를 붙여줘 computed로 계산된 값을 보여게 함
        let new_journal = ''
        new_journal = 'http://localhost:8000' + this.journal?.journal_image
        return new_journal
      },
    },
    created(){
        this.getJournal()
    },


}
</script>

<style>

</style>