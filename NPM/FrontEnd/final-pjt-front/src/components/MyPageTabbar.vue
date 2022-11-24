<template>
  <div class="MyPageTabbar">
    <nav class="border-bottom p-1 mt-5 d-flex justify-content-around">
      <span @click="tab1" class="btn">내가 남긴 기록</span>
      <span @click="tab2" class="btn">좋아요한 기록</span>
      <span @click="tab3" class="btn">환경설정</span>
    </nav>
  </div>
</template>

<script>

export default {
    name:'MyPageTabbar',
    methods: {
      tab1() {
        this.$store.commit('TAB_NUM', 1)
      },
      tab2() {
        this.$store.commit('TAB_NUM', 2)
      },
      tab3() {
        this.$store.commit('TAB_NUM', 3)
        this.$store.commit('MY_PAGE_COMPONENT', 0)
      },
    }
}
</script>

<style>

</style>