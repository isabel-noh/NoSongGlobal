<template>
  <div class="MovieListView">
    <div style="display: flex; margin-bottom: 10px;">
        <div class="select_genre" style="margin-right:10px;">
            <select class="form-select form-select-sm" aria-label=".form-select-sm example" v-model="selected_genre" @change="getFilteredMovies">
            <option selected value="0">전체</option>
            <option value="12">모험</option>
            <option value="14">판타지</option>
            <option value="16">애니메이션</option>
            <option value="18">드라마</option>
            <option value="27">공포</option>
            <option value="28">액션</option>
            <option value="53">스릴러</option>
            <option value="80">범죄</option>
            <option value="99">다큐멘터리</option>
            <option value="878">SF</option>
            <option value="9648">다큐멘터리</option>
            <option value="10402">음악</option>
            <option value="10749">로맨스</option>
            <option value="10751">가족</option>
            <option value="10752">전쟁</option>
            <option value="10770">TV 영화</option>
            </select>
        </div>
        <div class="select_sorting">
            <select class="form-select form-select-sm" aria-label=".form-select-sm example"
            @change="getFilteredMovies" v-model="sorted_option">
            <option selected value="0">정렬</option>
            <option value="1">최신</option>
            <option value="2">오래된</option>
            <option value="3">평점(높은순)</option>
            <option value="4">평점(낮은순)</option>
            <option value="5">인기도(높은순)</option>
            <option value="6">인기도(낮은순)</option>
            </select>
        </div>
    </div>
    <div class="row row-cols-1 row-cols-md-4">
        <div class="col"
            style="cursor : pointer;" 
            v-for="(movie) in movieList" 
            :key="movie?.movie_id">
            <router-link :to="{ name : 'movieDetail', params: { movie_id: movie.movie_id}}">
            <!-- @click="getDetailMovie(movie?.movie_id)"> -->
            <div class="card h-100" style="border:none;">
                <figure>
                    <img :src="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`" class="card-img"/>
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
            </router-link>
        </div>
        
    </div>
  </div>
</template>

<script>
export default {
    name:'MovieListView',
    data(){
        return {
            selected_genre: "0",
            sorted_option: "0",
            movieList: [],
        }
    },
    
    methods:{
        // TODO 영화 전체 리스트 가져오기
        getMovieList(){
          this.$store.dispatch('loadMovieData')
          console.log(this.$store.state.movieList)
        },
        //영화 장르별/정렬 리스트 가져오기
        getFilteredMovies(){
          // console.log(this.selected_genre, this.sorted_option)
          if (this.selected_genre === "0") {
            this.movieList = this.movieData
          }
          else {
            this.movieList = this.movieData.filter((movie) => {
              return movie.genre_id.includes(Number(this.selected_genre))
            })
          }
          if (["1", "2"].includes(this.sorted_option)) {
            this.movieList = this.movieList.sort((a,b) => {
              const date1 = new Date(a.release_date).getTime()
              const date2 = new Date(b.release_date).getTime()
              if (this.sorted_option === "1") return date2 - date1
              else return date1 - date2
            })
          }
          else if (["3", "4"].includes(this.sorted_option)) {
            this.movieList = this.movieList.sort((a,b) => {
              if (this.sorted_option === "3") return Number(b.vote_average) - Number(a.vote_average)
              else return Number(a.vote_average) - Number(b.vote_average)
            })
          }
          else if (["5", "6"].includes(this.sorted_option)) {
            this.movieList = this.movieList.sort((a,b) => {
              if (this.sorted_option === "5") return Number(b.revenue) - Number(a.revenue)
              else return Number(a.revenue) - Number(b.revenue)
            })
          }
        },
    },
    created(){
      // TODO 페이지 생성 시 영화 데이터 가져오기
        this.getMovieList()
        this.movieList = this.movieData
    },
    computed: {
      // TODO 영화 데이터 state에서 getters로 가져오기
      movieData() {
        return this.$store.getters.movieData
      }
    }

}
</script>

<style>
h4 {
    text-decoration: none;
    color: transparent;
}
.card figure img {
  opacity: 1;
  -webkit-transition: .3s ease-in-out;
  transition: .3s ease-in-out;
}
.card:hover img{
    opacity: .3;
}
.card:hover h4{
    color: black;
}
</style>