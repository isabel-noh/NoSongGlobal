<template>
  <div class="movie-detail-view">

  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'MovieDetailView',
    data(){
      return{
        movie:null,
      }
    },
    methods: {
      getMovieDetail(){
        axios({
          method:'GET',
          url: `${API_URL}/movies/movieList`,
          params: {
            movie_id: this.$route.params.movie_id
          }
        })
        .then((response) => {
          console.log(response.data)
        })
        .catch((error) => {
          console.log(error)
        })
      }
    },
    created(){
      this.getMovieDetail()
    }
}
</script>

<style>

</style>