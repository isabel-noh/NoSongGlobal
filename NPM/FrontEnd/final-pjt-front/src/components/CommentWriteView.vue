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
            const payload = {
                comment: comment
            }
            axios({
                method: 'POST',
                url: `${API_URL}/journal/comment/create`,
                headers:{
                    'Authorization': `${user.token}`
                },
                params: {
                    journal_id:this?.journal_id,
                },
                data: payload,
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