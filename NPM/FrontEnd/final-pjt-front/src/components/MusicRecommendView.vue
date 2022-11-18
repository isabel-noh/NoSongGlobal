<template>
  <div class="music-recommend-box">

  </div>
</template>

<script>
const YoutubeMusicAPI = require('youtube-music-api')
export default {
    name: 'MusicRecommendView',
    data(){
        return {
            musicList : [],
        }
    },
    method: {
        getMusicList(){
        }
    }
}
</script>

<style>

</style>