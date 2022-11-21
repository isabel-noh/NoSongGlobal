<template>
  <div class="JournalDetailView">
    <h1 id="journal-title-h1">Remember Movie Moment</h1>
    <div style="max-height:300px; box-sizing:content-box; overflow:hidden;">
        <img :src="journal?.journal_image" style="border-radius: 0px; ">
    </div>
    <div class="youtube_music_player"></div>
    <div class="journal_content">
        <h5>{{journal.movie_title}}</h5>
        <p>{{journal.watched_at}}</p>
        <p>{{journal.title}}<span> {{journal.like_cnt}} </span><button>좋아요</button></p>
        <p>{{journal.content}}</p>
        <hr>
    </div>
    <div class="comment-div">
        <CommentWriteView 
            :journal_id="journal.journal_id"
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
            // journal: null,
            // 가라 데이터
            journal: {
                journal_id: 1,
                title: '바보야',
                content: '나는 바보인 것이다',
                watched_at: '2022-01-22',
                movie_title: '아바타',
                poster_path: 'https://image.tmdb.org/t/p/w500//zygmx5abXeDpr3fWYX4jlXFZ1wh.jpg',
                comment_set:[],
                comment_cnt:0,
                like_cnt:0,
            },
            added_comment: null,
            commentList:[],
        }
    }, 
    components:{
        CommentWriteView,
        CommentsList,
    },
    methods: {
        getJournal(){
            axios({
                method:'GET',
                url: `${API_URL}/journal/${this.$route.params.journal_id}`,
            })
            .then((response) => {
                this.journal = response.data
                console.log(this.journal)
            })
            .catch((error) => {
                console.log(error)
            })
        },
        addComment(added_comment){
            console.log(added_comment)
            this.added_comment = added_comment
        }
    },
    created(){
        this.getJournal()
    }
}
</script>

<style>
#journal-title-h1{
    font-family: 'Do Hyeon';
}
</style>