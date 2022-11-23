<template>
  <div class="recommend">
    <!-- 로그인유저 -->
    <div v-if="nickname">
        <h4 id="recommend-title">{{nickname}}님을 위한 추천 영화</h4>
        <div class="card text-bg-dartk" style="position: relative; width: 100%; max-height: 300px;overflow: hidden;border: none;">
            <img src="@/assets/example1.jpeg" class="card-img" alt="#">
            <div style="position:absolute; bottom: 3%; left: 2%; text-align:left;">
                <h5 class="card-title">Movie title</h5>
                <p class="card-text"
                    style="margin-bottom:10px">Movie description</p>
                <button type="button" class="btn btn-dark"
                    @click="goToDetailMovie">상세정보</button>
            </div>
        </div>
    </div>
    <!-- 비로그인 유저 -->
    <div v-else>
        <h4 id="recommend-title">오늘의 추천 영화</h4>
        <!-- <div class="card text-bg-dartk" style="position: relative; width: 100%; max-height: 300px;overflow: hidden;border: none;"> -->
        <div>
            <!-- <span v-for=" item in recommend_movieList" :key="item?.id">{{item?.title}}</span> -->
            <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="false">
                <div class="carousel-indicators">
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
                </div>
                <div class="carousel-inner">
                    <!-- <div class="carousel-item active" v-for=" item in recommend_movieList" :key="item?.id"> -->
                    <!-- <div class="carousel-item active" v-for=" item in recommend_movieList" :key="item?.id">
                        <img :src="`https://image.tmdb.org/t/p/w500/${item?.poster_path}`" 
                            class="d-block w-100" 
                            style="height: 500px;"
                            :alt="`${item?.title}`">
                        <div class="carousel-caption d-none d-md-block">
                            <h5>{{item.title}}</h5>
                            <p>{{item.overview}}</p>
                        </div>
                    </div> -->
                    <div class="carousel-item active">
                        <img :src="recommend_movieList[0]?.poster_path" 
                            class="d-block w-100" 
                            style="height: 500px;"
                            :alt="`${recommend_movieList[0]?.title}`">
                        <div class="carousel-caption d-none d-md-block">
                            <h5>{{recommend_movieList[0]?.title}}</h5>
                            <p>{{recommend_movieList[0]?.overview}}</p>
                        </div>
                    </div>
                    <!-- <div class="carousel-item">
                        <img :src="recommend_movieList[1]?.poster_path" 
                            class="d-block w-100" 
                            style="height: 500px;"
                            :alt="`${item?.title}`">
                        <div class="carousel-caption d-none d-md-block">
                            <h5>{{item.title}}</h5>
                            <p>{{item.overview}}</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img :src="recommend_movieList[2]?.poster_path" 
                            class="d-block w-100" 
                            style="height: 500px;"
                            :alt="`${item?.title}`">
                        <div class="carousel-caption d-none d-md-block">
                            <h5>{{item.title}}</h5>
                            <p>{{item.overview}}</p>
                        </div>
                    </div> -->
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
                </div>
            <!-- <img src="@/assets/example1.jpeg" class="card-img" alt="#"> -->
            <!-- <div style="position:absolute; bottom: 3%; left: 2%; text-align:left;">
                <h5 class="card-title">Movie title</h5>
                <p class="card-text"
                    style="margin-bottom:10px">Movie description</p>
                <button type="button" class="btn btn-dark"
                    @click="goToDetailMovie(movie?.id)">상세정보</button> -->
            <!-- </div> -->
        </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'RecommendView',
    data(){
        return {
            recommend_movieList:[],
        }
    },
    props:{
        nickname:String,
    },
    computed:{
    },
    methods:{
        recommend_arr_general(){
            let movieList = this.$store.getters.movieData
            movieList = _.sampleSize(movieList, 10)
            
            for (const j of movieList){
            if(j.poster_url !== null){
              j.poster_url = 'https://image.tmdb.org/t/p/w500/' + j.poster_url
            }
            this.movieList.push(j)
          }
            this.recommend_movieList = movieList
            console.log(this.recommend_movieList)
        },
        goToDetailMovie(id){
            this.$router.push({ name : 'movieDetail', params: { movie_id: id }})
        }
    },
    created(){
        this.recommend_arr_general()
    }

}
</script>

<style>
.recommend {
    padding-bottom: 10px;
}
#recommend-title{
    text-align: initial;
    font-family: "Do Hyeon", sans-serif;
    color: black;
    padding: 10px 0px;
}
img {
  max-width: 100%;
}
button {
    margin-right: 5px;
}
</style>