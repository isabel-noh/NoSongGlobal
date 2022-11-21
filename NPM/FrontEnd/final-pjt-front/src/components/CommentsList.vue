<template>
  <div class="comment-list">
    <div>
        <CommentItem v-for="comment in commentList" 
            :key="comment.comment_id"
            :comment="comment"/>
    </div>
  </div>
</template>

<script>
import CommentItem from '@/components/CommentItem'

export default {
    name: 'CommentList',
    components: {
        CommentItem,
    },
    data(){
        return{
            commentsList = [],
        }
    },
    props:{
        added_comment:Object,
        commentList:Array,
    },

    watch:{
        comments(){
            this.commentsList = this.commentList
        }
    }
}
</script>

<style>

</style>