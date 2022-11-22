<template>
  <div class="music-recommend-box">
    <h5 id="music-recommend-title">오늘의 추천 사운드 트랙</h5>
    <div style="display:flex;">
        <div style="background-color:grey; width:50%; height: 200px; margin-right:20px;">hello</div>
        <div style="background-color:grey; width:50%; height: 200px; ">hello</div>
    </div>
    <!-- <p v-for="(video) in videoList" :key="video.id.videoId">{{video.snippet.title}}</p> -->
    <p>{{videoList[0]?.snippet.title}}</p>
    <iframe style="display:none;" id="ytplayer" type="text/html" width="720" height="405" :src="videoUrl" frameborder="0" allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' ></iframe>
  </div>
</template>

<script>
import axios from 'axios';

const youtubeURL = 'https://www.googleapis.com/youtube/v3/search'
export default {
    name: 'MusicRecommendView',
    data(){
        return {
            videoList : [],
            videoUrl: null,
            isPlay: false,
        }
    },
    methods: {
        playMusic(){
            this.isPlay = !this.isPlay;
            if (this.isPlay) {
            document
                .querySelector('#ytVideo')
                .contentWindow.postMessage(
                '{"event":"command","func":"' + 'playVideo' + '","args":""}',
                '*',
                );
            } else {
            document
                .querySelector('#ytVideo')
                .contentWindow.postMessage(
                '{"event":"command","func":"' + 'pauseVideo' + '","args":""}',
                '*',
                );
            }
        },
        getMusicList(){
            axios({
                method: 'GET',
                url: `${youtubeURL}/`,
                params:{
                    //key 가리기
                    key: 'AIzaSyBBpJBc12qN_3M1eS_gZE_nY8XMpKwfw4I',
                    part: 'snippet',
                    chart: 'mostPopular',
                    maxResults: 10,
                    order: 'viewCount',
                    q: 'blank panther, official, soundtrack',
                    type: 'video',
                    duration: 'short',
                }
            })
            .then((response) => {
                this.videoList = response.data.items
                this.videoUrl = 'https://www.youtube.com/embed/' + this.videoList[0]?.id.videoId + "?autohide='2'&modestbranding=1&enablejsapi=1&version=3&playerapiid=ytplayer"

            })
            .catch((err) => {
                console.log(err)
            })
        }
    }, 
    mounted(){
        // this.getMusicList()
    }
}
</script>

<style>
#music-recommend-title{
    text-align: initial;
}
h5{
    font-family: 'Do Hyeon';
}
select, option{
    font-family: 'Do Hyeon';
}
</style>