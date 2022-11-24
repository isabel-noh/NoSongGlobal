<template>
  <div class="home">
    <!-- 영화 페이지 -->
    <RecommendView/>
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
  }

}
</script>
