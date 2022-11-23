<template>
  <div class="recommend">
    <h4 id="recommend-title">{{nickname}}님을 위한 추천 영화</h4>
    <div class="card text-bg-dartk" style="position: relative; width: 100%; max-height: 300px;overflow: hidden;border: none;">
        <img src="@/assets/example1.jpeg" class="card-img" alt="...">
        <div style="position:absolute; bottom: 3%; left: 2%; text-align:left;">
            <h5 class="card-title">Movie title</h5>
            <p class="card-text"
                style="margin-bottom:10px">Movie description</p>
            <button type="button" class="btn btn-dark">상세정보</button>
            <button type="button" class="btn btn-dark">좋아요</button>
        </div>
        <!-- <div class="card-img-overlay" style="bottom: 0; left: 0; text-align:left;">
            
        </div> -->
    </div>
  </div>
</template>

<script>
export default {
    name: 'RecommendView',
    props:{
        nickname:String,
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