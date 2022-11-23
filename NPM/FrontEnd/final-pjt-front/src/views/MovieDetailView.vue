<template>
  <div class="movie-detail-view">
    <div class="movie-data">
      <div class="img-box">
        <img :src="`https://image.tmdb.org/t/p/w300/${movie?.poster_path}`">
      </div>
      <div class="content-box">
        <h2>{{movie?.title}}</h2>
        <button class="btn btn-light" style="margin-bottom:10px;">좋아요</button>
        <p>개봉일: {{movie?.release_date}}</p>
        <p>장르: {{genres}}</p>
        <p>평점: {{movie?.vote_average}}</p>
        <p>러닝타임: {{runtime}}</p>
      </div>
    </div>
    <div class="movie-overview">
      <h4>영화 소개 / 줄거리</h4>
      <p>{{movie?.overview}}</p>
    </div>
    <hr>
    <div class="movie-ost">
      <h4>영화 OST</h4>
      <div class="movie-ost-list">

      </div>
    </div>
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
        imgUrl:null,
      }
    },
    methods: {
      getMovieDetail(){
        axios({
          method:'GET',
          url: `${API_URL}/movies/`+`${this.$route.params.movie_id}`,
        })
        .then((response) => {
          this.movie = response.data
          this.imgUrl = 'https://image.tmdb.org/t/p/w500' + response.data.poster_path
        })
        .catch((error) => {
          console.log(error)
        })
      }
    },
    created(){
      this.getMovieDetail()
    },
    computed: {
      genres() {
        let genres = ""
        for (const idx in this.movie?.genre_text){
          if (idx === "0") {
            genres = genres + `${this.movie?.genre_text[idx]}`
          }
          else {
            genres = genres + `, ${this.movie?.genre_text[idx]}`
          }
        }
        return genres
      },
      runtime(){
        const r = this.movie?.runtime
        let hour = 0
        let minute = 0
        if (r >= 60){
          hour = parseInt(r / 60)
          minute = r - (hour * 60)
        }
        return `${hour}시간 ${minute}분`
      }
    }
}
</script>

<style>
.movie-detail-view{
  font-family: 'Do Hyeon';
}
.movie-data{
  display: flex;
  margin: 20px 0px;
}
.img-box{
  width: 100%;
}
img{
  width: 90%;
  margin: auto;
  border-radius: 10px;
}
.content-box{
  width: 100%;
  padding: 1rem;
  text-align: start;
}
.content-box > h2 {
  text-align: center;
}
.movie-overview{
  margin: 10px;
  text-align: start;
}
.movie-ost{
  text-align: start;
  margin: 10px;
}
</style>