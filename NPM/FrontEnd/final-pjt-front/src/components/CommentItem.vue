<template>
  <div class="comment-item">
    <p>
        <span>username</span> - 
        <span>comment</span>
    </p>
  </div>
</template>

<script>

export default {
    name: 'CommentItem',
    props: {
        comment:Object,
    },
}
</script>

<style>

</style>