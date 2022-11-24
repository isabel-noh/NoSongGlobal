<template>
  <div class="comment-list">
    <div v-for="comment in commentList"
    :key="comment?.comment_id"
    >
    <!-- {{ comment }} -->
    {{ comment[0] }} - {{ comment[1] }}
        <!-- <CommentItem v-for="comment in commentsList" 
            :key="comment?.comment_id"
            :comment="comment"/> -->
    </div>
  </div>
</template>
<script>
// import CommentItem from '@/components/CommentItem'
export default {
    name: 'CommentList',
    // components: {
    //     CommentItem,
    // },
    data(){
        return{
            commentsList : [],
        }
    },
    props:{
        // added_comment:String,
        commentList: Array,
    },

    watch:{
        comments(){
            this.commentsList = this?.commentList
        }
    }
}
</script>

<style>

</style>