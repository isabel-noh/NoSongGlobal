<template>
  <div class="recommend">
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
</template>

<script>
export default {
    name: 'RecommendView',
    data() {
      return {
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
      }
    },
    computed: {
      username() {
        return this.$store.state.user.nickname
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
      this.$store.dispatch('recommendMovie')
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