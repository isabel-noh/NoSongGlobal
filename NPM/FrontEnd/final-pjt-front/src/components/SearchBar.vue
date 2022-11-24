<template>
  <div class="searchBar align-items-center">
    <div class="m-auto"
    style="width:65%"
    >
        <input class="search-input rounded-3" type="text" @input="searchKeyword">    
      <div v-show="keyword" class="row row-cols-1 row-cols-md-3"
      style="margin-top:2rem; margin-left:0.3rem; margin-right:0.3rem;"  
      >
      <div class="col"
      style="cursor : pointer;" 
      v-for="(movie) in result" 
      @click="reloadPage(movie.id)" 
      :key="movie?.movie_id">
      <!-- :to="{ name : 'movieDetail', params: { movie_id: movie.id}}" -->
      <!-- @click="getDetailMovie(movie?.movie_id)"> -->
      <div class="card h-100" style="border:none;">
        <figure>
          <img :src="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`" class="card-img" style="height:40vh;"/>
        </figure>
        <div class="card-img-overlay" style="top: 50%; right: 0px; left: 0px;margin:0px; padding:0px;">
          <div class="movie-title-and-movie-genre">
            <h4 style="font-family:'Do Hyeon';" class="card-title">{{movie?.title}}</h4>
            <!-- 장르 -->
            <!-- <p class="card-text">{{movie?.genre}}</p> -->
          </div>
          <!-- <p class="card-text">{{movie?.release_date}}</p> -->
        </div>
      </div>
    </div>   
  </div>    
</div>
</div>
</template>

<script>
export default {
    name: 'SearchBar',
    data() {
        return {
            keyword: null,
            result: null,
        }
    },
    methods: {
        searchKeyword(event){
          this.keyword = event.target.value
          if (this.keyword) {
            this.result = this.movieList.filter((movie) => {
              return movie.title.includes(this.keyword)
            })
          }
          this.result = this.result.slice(0,9)
            // this.$store.dispatch('search', this.keyword)
            // this.keyword = null
        },
        reloadPage(id) {
          this.$router.push({name: 'movieDetail', params: { movie_id: id}})
          this.$router.go(this.$router.currentRoute)
        }
    },
    // 처음 main 페이지로 오면 전체 영화 list, recommended 리스트 보여줌 
    // 로그인하고 오면 영화 전체 리스트, 그 고객에 맞는 리스트 보여줌
    // 어디페이지에서든지 검색하고 온 거면, 새로 Movie List를 전체를 받아오지 않고 검색한 리스트 보여줌 
    computed: {
      movieList() {
        console.log(this.$store.getters.movieData)
        return this.$store.getters.movieData
      }
    }
}
</script>

<style>
.searchBar {
    padding: 20px;
    border-top: 1px solid lightgrey;
    border-bottom: 1px solid lightgrey;
    margin-bottom: 15px;
}
.search-input {
    border: 1px solid lightgrey;
    height: 50px;
    margin-right: 10px;
    width:80%;
}
</style>