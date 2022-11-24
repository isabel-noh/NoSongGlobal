<template>
  <div class="MyPageTabbar">
    <nav class="border-bottom p-1 mt-5">
      <span class="btn" @click="changeComponent(1)">내가 남긴 기록</span>
      <span class="btn" @click="changeComponent(2)">좋아요한 기록</span>
      <span class="btn" @click="changeComponent(3)">환경설정</span>
    </nav>
  </div>
</template>

<script>

export default {
    name:'MyPageTabbar',
    components: {
    },
    methods:{
      changeComponent(num){
        this.$emit('changeComponent', num)
      }
    }
}
</script>

<style>

</style>