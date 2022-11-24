<template>
  <div class="home">
    <!-- 영화 페이지 -->
    <RecommendView :nickname="getNickname"/>
    <MovieListView/>
  </div>
</template>

<script>
// @ is an alias to /src
import RecommendView from '@/components/RecommendView'
import MovieListView from '@/components/MovieListView'

export default {
  name: 'HomeView',
  components: {
    RecommendView,
    MovieListView,
  },
  computed:{
    getNickname(){
      const nickname = this.$store.getters.userData.nickname
      return nickname
    }
  }

}
</script>
