<template>
  <div class="home">
    <!-- 영화 페이지 -->
    <RecommendView/>
    <!-- <MusicRecommendView /> -->
    <MovieListView/>
  </div>
</template>

<script>
// @ is an alias to /src
import RecommendView from '@/components/RecommendView'
// import MusicRecommendView from '@/components/MusicRecommendView'
import MovieListView from '@/components/MovieListView'

export default {
  name: 'HomeView',
  components: {
    RecommendView,
    // MusicRecommendView,
    MovieListView,
  }
}
</script>
