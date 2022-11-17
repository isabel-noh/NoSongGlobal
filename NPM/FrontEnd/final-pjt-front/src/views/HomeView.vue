<template>
  <div class="home">
    <!-- 영화 페이지 -->
    <RecommendView/>
  </div>
</template>

<script>
// @ is an alias to /src
import RecommendView from '@/components/RecommendView'
export default {
  name: 'HomeView',
  components: {
    RecommendView,
  }
}
</script>
