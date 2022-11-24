<template>
  <div class="recommend">
    <!-- 로그인유저 -->
    <div v-if="nickname">
        <h4 id="recommend-title">Recommendation for <span class="btn">{{nickname}}</span></h4>
        <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="false">
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
            <div class="carousel-item rounded-4 active"
                style="height:40vw;"
                :style="{ 
                    backgroundImage:`linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), url(${imgUrl}${movieList[recommendMovieList[0]].backdrop_path})` ,
                    backgroundSize: 'cover'}">
                <div class="d-flex align-items-center border border-0 bg-white rounded-4"
                    style="height:fit-content; width:fit-content; margin:4vw auto;"
                    @click="goToDetailMovie(movieList[recommendMovieList[0]].id)">
                    <img :src="imgUrl + movieList[recommendMovieList[0]].poster_path"
                    style="height:25vw; width:100%; cursor:pointer;"
                    :alt="`${movieList[recommendMovieList[0]].title}`">
                    <div
                        v-if="movieList[recommendMovieList[0]].overview"
                        style="background-color: transparent;
                                position: absolute;
                                bottom: 10%;
                                left: 0;
                                right: 0;">
                        <h5 style="font-family: 'Do Hyeon">{{movieList[recommendMovieList[0]].title}}</h5>
                        <p>{{movieList[recommendMovieList[0]].overview}}</p>
                    </div>
                    <div
                        v-else
                        style="background-color: transparent;
                                position: absolute;
                                bottom: 15%;
                                left: 0;
                                right: 0;">
                        <h5 style="font-family: 'Do Hyeon">{{movieList[recommendMovieList[0]].title}}</h5>
                    </div>
                </div>
            </div>
            <div class="carousel-item rounded-4"
                style="height:40vw;"
                :style="{ backgroundImage:`linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), 
                url(${imgUrl}${movieList[recommendMovieList[1]].backdrop_path})` ,
                backgroundSize: 'cover'}">
            <div class="d-flex align-items-center border border-0 bg-white rounded-4"
                style="height:fit-content; width:fit-content; margin:4vw auto;"
                @click="goToDetailMovie(movieList[recommendMovieList[1]].id)">
                <img :src="imgUrl + movieList[recommendMovieList[1]].poster_path"
                style="height:25vw; width:100%; cursor:pointer;"
                :alt="`${movieList[recommendMovieList[1]].title}`">
                <div
                    v-if="movieList[recommendMovieList[1]].overview"
                    style="background-color: transparent;
                            position: absolute;
                            bottom: 10%;
                            left: 0;
                            right: 0;">
                    <h5 style="font-family: 'Do Hyeon">{{movieList[recommendMovieList[1]].title}}</h5>
                    <p>{{movieList[recommendMovieList[1]].overview}}</p>
                </div>
                <div
                    v-else
                    style="background-color: transparent;
                            position: absolute;
                            bottom: 15%;
                            left: 0;
                            right: 0;">
                    <h5 style="font-family: 'Do Hyeon">{{movieList[recommendMovieList[1]].title}}</h5>
                </div>
            </div>
            </div>
            <div class="carousel-item rounded-4"
                style="height:40vw;"
                :style="{ backgroundImage:`linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), 
                url(${imgUrl}${movieList[recommendMovieList[2]].backdrop_path})` ,
                backgroundSize: 'cover'}">
            <div class="d-flex align-items-center border border-0 bg-white rounded-4"
                style="height:fit-content; width:fit-content; margin:4vw auto;"
                @click="goToDetailMovie(movieList[recommendMovieList[2]].id)">
                <img :src="imgUrl + movieList[recommendMovieList[2]].poster_path"
                style="height:25vw; width:100%; cursor:pointer;"
                :alt="`${movieList[recommendMovieList[2]].title}`">
                <div
                    v-if="movieList[recommendMovieList[2]].overview"
                    style="background-color: transparent;
                            position: absolute;
                            bottom: 10%;
                            left: 0;
                            right: 0;">
                    <h5 style="font-family: 'Do Hyeon">{{movieList[recommendMovieList[2]].title}}</h5>
                    <p>{{movieList[recommendMovieList[2]].overview}}</p>
                </div>
                <div
                    v-else
                    style="background-color: transparent;
                            position: absolute;
                            bottom: 15%;
                            left: 0;
                            right: 0;">
                    <h5 style="font-family: 'Do Hyeon">{{movieList[recommendMovieList[2]].title}}</h5>
                </div>
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
        <h4 id="recommend-title">Movie for Today</h4>
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
                    <div class="carousel-item rounded-4 active"
                        style="height: 40vw;"
                        :style="{ 
                            backgroundImage: `linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), 
                            url(${recommend_movieList[0].backdrop_path})`, 
                            backgroundSize: 'cover'}">
                        <div 
                            class="d-flex align-items-center border border-0 bg-white rounded-4"
                            style="height:fit-content; width:fit-content; margin:4vw auto; "
                            @click="goToDetailMovie(recommend_movieList[0].id)">
                            <img :src="`${recommend_movieList[0].poster_path}`" 
                                style="height:25vw; width:100%; cursor:pointer;"
                                :alt="`${recommend_movieList[0].title}`">
                        </div>
                        <div 
                            v-if="recommend_movieList[0].overview"
                            style="background-color: transparent;
                                position: absolute;
                                bottom: 8%;
                                left: 0;
                                right: 0;">
                            <h5 style="font-family: 'Do Hyeon">{{recommend_movieList[0].title}}</h5>
                            <p>{{recommend_movieList[0].overview}}</p>
                        </div>
                        <div 
                            v-else
                            style="background-color: transparent;
                                position: absolute;
                                bottom: 15%;
                                left: 0;
                                right: 0;">
                            <h5 style="font-family: 'Do Hyeon">{{recommend_movieList[0].title}}</h5>
                        </div>
                    </div>
                    <div class="carousel-item rounded-4" 
                        v-for=" item in recommend_movieList.slice(1,9)" :key="item?.id"
                        style="height: 40vw;"
                        :style="{ 
                            backgroundImage: `linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), 
                            url(${item?.backdrop_path})`, 
                            backgroundSize: 'cover'}">
                        <div
                            class="d-flex align-items-center border border-0 bg-white rounded-4"
                            style="height:fit-content; width:fit-content; margin:4vw auto; cursor:pointer;"
                            @click="goToDetailMovie(recommend_movieList[0].id)">
                            <img :src="`${item?.poster_path}`" 
                                style="height:25vw; width:100%; cursor:pointer;"
                                :alt="`${item?.title}`">
                        </div>
                        <div style="background-color: transparent;
                                position: absolute;
                                bottom: 10%;
                                left: 0;
                                right: 0;">
                            <h5 style="font-family: 'Do Hyeon">{{item?.title}}</h5>
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
                j.backdrop_path = 'https://image.tmdb.org/t/p/w500' + j.backdrop_path
                j.poster_path = 'https://image.tmdb.org/t/p/w500' + j.poster_path
                let temp = j.overview.split(' ')
                temp = temp.slice(0, 3)
                j.overview = temp.join(' ')
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
      nickname() {
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