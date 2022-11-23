<template>
        <div>
            <form @submit.prevent="updateJournal">
                <div style="text-align:start; margin: 10px;">
                    <h3>Edit Your Moment</h3>
                    <div>
                        <label for="journal_title">글 제목: </label><input type="text" id="journal_title">
                    </div>
                    <div>
                        <label for="journal_content">글 내용: </label><textarea type="text" id="journal_content"></textarea>
                    </div>
                    <div>
                        <label for="movie_title">영화 제목: </label><input type="text" id="movie_title">
                    </div>
                    <div>
                        <label for="journal_image">영화 이미지: </label><input type="file" id="journal_image">
                    </div>
                    <div>
                        <label for="watched_at">본 날짜:</label><input type="text" id="watched_at">
                    </div>
                </div>
                <div>
                    <button type="submit" class="btn btn-danger">수정하기</button>
                </div>
            </form>
        </div>
    
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'UpdateJournalView',
    data(){
        return{
            journal : null,
            journal_title : null,
            journal_content : null,
            movie_title : null,
            journal_image : null,
            watched_at : null,
        }
    },
    methods: {
        // 게시글 detail 불러오기
        getJournal(){
            axios({
                method:'GET',
                url: `${API_URL}/journals/${this.$route.params.journal_id}/detail`,
            })
            .then((response) => {
                console.log(response.data)
                this.journal = response.data
            })
            .catch((error) => {
                console.log(error)
            })
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
    }


}
</script>

<style>

</style>