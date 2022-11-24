<template>
  <div class="JournalDetailView">
    <h1 id="journal-title-h1">Remember Movie Moment</h1>
    <div 
        style="max-height:300px; 
        box-sizing:content-box; 
        overflow:hidden; 
        margin-bottom: 10px;">
        <div v-if="journal?.journal_image" 
            :style="`borderRadius:0px; 
            backgroundImage:url(${url_formatting});
            width: 100%;
            height: 300px;
            background-size: contain;
            margin: auto;
            background-repeat: no-repeat;
            }`">
        </div>
    </div>
    <div class="journal_content">
        <h6>{{journal?.movie_title}}</h6>
        <p>{{journal?.watched_at}}</p>
        <h5>{{journal?.title}}<span> {{journal?.like_cnt}} </span>
            <button class="btn btn-primary"
                @click="likeJournal"
            >좋아요</button>
            <span
                v-if="like_count"
            > {{ like_count }} </span>
        </h5>
        <p v-if="journal?.rank === 1">
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star"></i>
            <i class="bi bi-star"></i>
            <i class="bi bi-star"></i>
            <i class="bi bi-star"></i>
        </p>
        <p v-if="journal?.rank === 2">
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star"></i>
            <i class="bi bi-star"></i>
            <i class="bi bi-star"></i>
        </p>
        <p v-if="journal?.rank === 3">
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star"></i>
            <i class="bi bi-star"></i>
        </p>
        <p v-if="journal?.rank === 4">
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star"></i>
        </p>
        <p v-if="journal?.rank === 5">
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star-fill"></i>
            <i class="bi bi-star-fill"></i>
        </p>
        <p>{{journal?.content}}</p>
    </div>
    <div class="delete-update-btn">
        <div 
            class="update-post-btn"
            v-if="journal?.user === user_id">
            <button class="btn btn-bright" @click="gotoEditPostPage">수정하기</button>
        </div>
        <div 
            class="delete-post-btn"
            v-if="journal?.user === user_id">
            <button class="btn btn-bright" @click="deletePost">삭제하기</button>
        </div>
    </div>
    <hr>
    <div class="comment-div">
        <CommentWriteView 
            :journal_id="journal?.journal_id"
            @addComment="addComment"/>
        <CommentsList
            :commentList="commentList"/>
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
            commentList: [],
            user_id: null,
            like_count: 0,
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
                url: `${API_URL}/journals/${this.$route.params.journal_id}/detail/`,
            })
            .then((response) => {
                this.journal = response.data
                console.log(this.journal)
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
                url: `${API_URL}/journals/${this.$route.params.journal_id}/detail/`,
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
            const local = localStorage.getItem('vuex')
            const user = JSON.parse(local)
            this.added_comment = added_comment.content
            const nickname = user.user.nickname
            // this.nickname_comment[nickname] = this.added_comment
            // console.log('###', this.nickname_comment)
            this.commentList.push([nickname, this.added_comment])
        },
        likeJournal(){
            const local = localStorage.getItem('vuex')
            const user = JSON.parse(local)
            axios({
                method: 'POST',
                url: `${API_URL}/journals/${this.$route.params.journal_id}/like/`,
                headers:{
                    'Authorization' : `Token ${user.token}`
                },
                data:{
                    id: this.journal?.id
                }
            })
            .then((response) => {
                const is_Liked = response.data.is_Liked
                if (is_Liked === true) {
                    this.like_count = response.data.like_count
                } else {
                    this.like_count = response.data.like_count
                } 
            })
        },
        getCommentsAll() {
            axios({
                method: 'GET',
                url: `${API_URL}/journals/${this.$route.params.journal_id}/comment/all/`,
            })
            .then((response) => {
                console.log(response)
            })
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
    justify-content: end;
    display: flex;
    margin-bottom: 10px;
}
.bi-star{
    color: rgb(242, 160, 3);
}
.bi-star-fill{
    color: rgb(242, 160, 3);
}
</style>