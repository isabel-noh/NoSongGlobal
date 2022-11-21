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
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name:'MovieListView',
    data(){
        return {
            movieList:[],
            selected_genre: "0",
            sorted_option: "0",
        }
    },
    
    methods:{
        //영화 전체 리스트 가져오기
        getMovieList(){
            axios({
                method:'GET',
                url: `${API_URL}/movies/movieList/`
            })
            .then((response) => {
                this.movieList = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
        //영화 장르별/정렬 리스트 가져오기
        getFilteredMovies(){
            console.log(this.selected_genre, this.sorted_option)
            axios({
                method:'GET',
                url: `${API_URL}/movieList`,
                params: {
                    genre_id:this.selected_genre,
                    sort_criteria: this.sorted_option
                }
            })
            .then((response) => {
                this.movieList = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
    },
    created(){
        this.getMovieList()
    },

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