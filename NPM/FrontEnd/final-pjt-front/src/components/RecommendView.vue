<template>
  <div class="recommend">
    <!-- 로그인유저 -->
    <div v-if="nickname">
        <h4 id="recommend-title"><span class="btn">{{username}}</span>님을 위한 추천 영화</h4>
        <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="false">
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
            <div class="carousel-item rounded-4 active"
            style="height:40vw;"
            :style="{ backgroundImage:`linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), url(${imgUrl}${movieList[recommendMovieList[0]].backdrop_path})` ,
            backgroundSize: 'cover'}"
            >
            <div class="d-flex align-items-center border border-0 bg-white rounded-4"
                style="height:25vw; width:40vw; margin-top:7vw; margin-left:15vw;"
            >
                <img :src="imgUrl + movieList[recommendMovieList[0]].poster_path"
                style="height:25vw;"
                alt="..."
                
                >
                <!-- style="margin-right:40vw; margin-top:7vw" -->
                <div>
                <h5>{{movieList[recommendMovieList[0]].title}}</h5>
                <p>{{movieList[recommendMovieList[0]].overview}}</p>
                </div>
                <!-- <div class="carousel-caption d-none d-md-block">
                <h5>{{movieList[recommendMovieList[0]].title}}</h5>
                <p>Some representative placeholder content for the first slide.</p>
                </div> -->
            </div>
            </div>
            <div class="carousel-item rounded-4"
            style="height:40vw;"
            :style="{ backgroundImage:`linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), url(${imgUrl}${movieList[recommendMovieList[1]].backdrop_path})` ,
            backgroundSize: 'cover'}"
            >
            <div class="d-flex align-items-center border border-0 bg-white rounded-4"
                style="height:25vw; width:40vw; margin-top:7vw; margin-left:15vw;"
            >
                <img :src="imgUrl + movieList[recommendMovieList[1]].poster_path"
                style="height:25vw;"
                alt="..."
                
                >
                <!-- style="margin-right:40vw; margin-top:7vw" -->
                <div>
                <h5>{{movieList[recommendMovieList[1]].title}}</h5>
                <p>{{movieList[recommendMovieList[1]].overview}}</p>
                </div>
                <!-- <div class="carousel-caption d-none d-md-block">
                <h5>{{movieList[recommendMovieList[0]].title}}</h5>
                <p>Some representative placeholder content for the first slide.</p>
                </div> -->
            </div>
            </div>
            <div class="carousel-item rounded-4"
            style="height:40vw;"
            :style="{ backgroundImage:`linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), url(${imgUrl}${movieList[recommendMovieList[2]].backdrop_path})` ,
            backgroundSize: 'cover'}"
            >
            <div class="d-flex align-items-center border border-0 bg-white rounded-4"
                style="height:25vw; width:40vw; margin-top:7vw; margin-left:15vw;"
            >
                <img :src="imgUrl + movieList[recommendMovieList[2]].poster_path"
                style="height:25vw;"
                alt="..."
                
                >
                <!-- style="margin-right:40vw; margin-top:7vw" -->
                <div>
                <h5>{{movieList[recommendMovieList[2]].title}}</h5>
                <p>{{movieList[recommendMovieList[2]].overview}}</p>
                </div>
                <!-- <div class="carousel-caption d-none d-md-block">
                <h5>{{movieList[recommendMovieList[0]].title}}</h5>
                <p>Some representative placeholder content for the first slide.</p>
                </div> -->
            </div>
            </div>
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
            <!-- <div>
            <b-carousel
            id="carousel-1"
            v-model="slide"
            :interval="4000"
            controls
            indicators
            background="#ababab"
            img-width="1024"
            img-height="480"
            style="text-shadow: 1px 1px 2px #333;"
            @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
            >
            <b-carousel-slide
                caption="First slide"
                text="Nulla vitae elit libero, a pharetra augue mollis interdum."
                :img-src="imgUrl + movieList[recommendMovieList[0]].poster_path"
            ></b-carousel-slide>

            <b-carousel-slide :img-src="imgUrl + movieList[recommendMovieList[1]].poster_path">
                <h1>Hello world!</h1>
            </b-carousel-slide>

            <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>

            <b-carousel-slide>
                <template #img>
                <img
                    class="d-block img-fluid w-100"
                    width="1024"
                    height="480"
                    src="https://picsum.photos/1024/480/?image=55"
                    alt="image slot"
                >
                </template>
            </b-carousel-slide>

            <b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">
                <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eros felis, tincidunt
                a tincidunt eget, convallis vel est. Ut pellentesque ut lacus vel interdum.
                </p>
            </b-carousel-slide>
            </b-carousel>

            <p class="mt-4">
            Slide #: {{ slide }}<br>
            Sliding: {{ sliding }}
            </p>
        </div> -->
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
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="3" aria-label="Slide 4"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="4" aria-label="Slide 5"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="5" aria-label="Slide 6"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="6" aria-label="Slide 7"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="7" aria-label="Slide 8"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="8" aria-label="Slide 9"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="9" aria-label="Slide 10"></button>
                </div>
                <div class="carousel-inner">
                    <!-- <div class="carousel-item active" v-for=" item in recommend_movieList" :key="item?.id"> -->
                    <div class="carousel-item active">
                        <!-- ${movieList[recommendMovieList[1]].backdrop_path -->
                        <img :src="`${recommend_movieList[0].poster_path}`" 
                            class="d-block w-100"
                            style="heigh : 10px;" 
                            :alt="`${recommend_movieList[0].title}`">
                        <div class="carousel-caption d-none d-md-block">
                            <h5>{{recommend_movieList[0].title}}</h5>
                            <p>{{recommend_movieList[0].overview}}</p>
                        </div>
                    </div>
                    <div class="carousel-item" 
                        v-for=" item in recommend_movieList" :key="item?.id">
                        <img :src="`${item?.poster_path}`" 
                            class="d-block w-100"
                            style="heigh : 10px;" 
                            :alt="`${item?.title}`">
                        <div class="carousel-caption d-none d-md-block">
                            <h5>{{item?.title}}</h5>
                            <p>{{item?.overview}}</p>
                        </div>
                    </div>
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

    data() {
      return {
        recommend_movieList:[],
        slide: 0,
        sliding: null,
        imgUrl: 'https://image.tmdb.org/t/p/w500'
      }
    },
    methods: {
      onSlideStart(slide) {
        console.log(slide)
        this.sliding = true
      },
      onSlideEnd(slide){
        console.log(slide)
        this.sliding = false
      },
      recommend_arr_general(){
            let movieList = this.$store.getters.movieData
            movieList = _.sampleSize(movieList, 10)
            for(const j of movieList) {
                j.poster_path = 'https://image.tmdb.org/t/p/w500' + j.poster_path
            }
            this.recommend_movieList = movieList
            console.log(this.recommend_movieList)
      },
      goToDetailMovie(id){
          this.$router.push({ name : 'movieDetail', params: { movie_id: id }})
      }
    },
    computed: {
      isLogin(){
        return this.$store.getters.isLogin
      },
      username() {
        return this.$store.getters.userData.nickname
      },
      movieList() {
        return this.$store.getters.movieData
      },
      recommendMovieList(){
        return this.$store.getters.getRecommendMovieList
      },
      // imgUrl(imgPath){
      //   console.log(`${this.imgUrl}${imgPath}`)
      //   return `${this.imgUrl}${imgPath}`
      // }
    },
    created() {
        this.recommend_arr_general()
        this.$store.dispatch('recommendMovie')
    },
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