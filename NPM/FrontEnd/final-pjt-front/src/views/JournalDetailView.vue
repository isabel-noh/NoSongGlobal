<template>
  <div class="JournalDetailView">
    <h1 id="journal-title-h1">Remember Movie Moment</h1>
    <div style="max-height:300px; box-sizing:content-box; overflow:hidden; margin-bottom: 10px;">
        <img
            v-if="journal?.journal_image" 
            :src="url_formatting" 
            style="border-radius:0px; ">
    </div>
    <div class="youtube_music_player"></div>
    <div class="journal_content">
        <p>{{this.movieData[this.journal?.movie-1].title}}</p>
        <p>{{journal?.watched_at}}</p>
        <h5>{{journal?.title}}<span> {{journal?.like_cnt}} </span><button class="btn btn-primary">좋아요</button></h5>
        <p>{{journal?.content}}</p>
    </div>
    <div class="delete-update-btn">
        <div 
            class="delete-post-btn"
            v-if="journal?.user === user_id">
            <button class="btn btn-danger" @click="deletePost">삭제하기</button>
        </div>
        <div 
            class="update-post-btn"
            v-if="journal?.user === user_id">
            <button class="btn btn-warning" @click="gotoEditPostPage">수정하기</button>
        </div>
    </div>
    <hr>
    <div class="comment-div">
        <CommentWriteView 
            :journal_id="journal?.journal_id"
            @addComment="addComment"/>
        <CommentsList
            :commentList="commentList"
            :added_comment="added_comment"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentWriteView from '@/components/CommentWriteView'
import CommentsList from '@/components/CommentsList'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'JournalDetailView',
    data(){
        return{
            journal: null,
            added_comment: null,
            commentList:[],
            user_id: null,
        }
    }, 
    components:{
        CommentWriteView,
        CommentsList,
    },
    methods: {
        // 게시글 detail 불러오기
        getJournal(){
            axios({
                method:'GET',
                url: `${API_URL}/journals/${this.$route.params.journal_id}/detail`,
            })
            .then((response) => {
                this.journal = response.data
                this.$store.commit('GET_JOURNAL', response.data)
            })
            .catch((error) => {
                console.log(error)
            })
        },
        // 게시글 삭제
        deletePost(){   
            const local = localStorage.getItem('vuex')
            const user = JSON.parse(local)
            axios({
                method: 'DELETE',
                url: `${API_URL}/journals/${this.$route.params.journal_id}/detail`,
                headers:{
                    'Authorization' : `Token ${user.token}`
                },
                data:{
                    id: this.journal?.id
                }
            })
            .then((response) => {
                console.log(response)
                console.log('삭제되었습니다.')
                this.$router.push({ name : 'journal'})
            })
            .catch((error) => {
                console.log(error)
            })
        },
        // journal 수정페이지로 가기
        gotoEditPostPage(){
            this.$router.push({ name : 'updateJournal' , params: {'journal_id' : this.journal.id}})
        },
        // TODO comment 작성
        addComment(added_comment){
            this.added_comment = added_comment
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
      movieData() {
        console.log(this.$store.getters.movieData)
        return this.$store.getters.movieData
      }
    },
    created(){
        this.$store.dispatch('isLogin')
        this.getJournal()
        const id = this.$store.getters.userData.user_id
        this.user_id = id
    },
    mounted(){
    },
    
}
</script>

<style>
.JournalDetailView{
    text-align: start;
}
#journal-title-h1{
    font-family: 'Do Hyeon';
}
.delete-update-btn{
    display: flex;
    margin-bottom: 10px;
}
</style>