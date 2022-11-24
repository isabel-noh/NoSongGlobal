<template>
  <div class="comment-write-box">
    <form @submit.prevent="addComment">
        <input 
            type="text" 
            placeholder="댓글을 입력해주세요"
            v-model.trim="commentData">
        <button type="submit" class="btn btn-bright">댓글달기</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'CommentWriteView',
    data(){
        return{
            commentData:'',
        }
    },
    props: {
        journal_id: Number,
    },
    methods: {
        addComment(){
            const local = localStorage.getItem('vuex')
            const user = JSON.parse(local)
            const comment = this?.commentData
            if(comment === ''){
                alert('댓글을 입력해주세요.')
            }
            console.log('댓글 달기')
            console.log('->', user.user)
            console.log('-->', user.token)
            axios({
                method: 'POST',
                url: `${API_URL}/journals/${this.$route.params.journal_id}/comment/create/`,
                headers:{
                    'Authorization': `Token ${user.token}`
                },
                data: {
                    comment,
                }
            })
            .then((response) => {
                console.log(response.data)
                this.$emit('addComment', response.data)
                this.commentData = ''
            })
            .catch((error) => {
                console.log(error)
            })
        }
    }

}
</script>

<style>

</style>