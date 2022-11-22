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
            journal: null,
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
                url: `${API_URL}/journals/${this.$route.params.journal_id}/detail`,
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