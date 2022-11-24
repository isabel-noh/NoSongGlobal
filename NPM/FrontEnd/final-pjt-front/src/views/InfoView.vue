<template>
  <div class="info">
    <nav>
      <h4>INTRODUCTION</h4>
      <a href="#team">Team</a>
      <a href="#service">Service</a>
      <a href="#contact">Contact us</a>
    </nav>
    <div class="info-body">
      <hr>
      <h4 id="team" style="color:black;">Team</h4>
      <div class="team-desc">
        <div class="member" style="margin-right: 10px; padding: 20px;">
          <h5 style="color:navy;">노현정</h5>
          <p>재촉왕</p>
          <p style="font-weight:bold">FrontEnd</p>
          <p>자주하는 말 : “이거 했어?”</p>
        </div>
        <div class="member" style="margin-right: 10px; padding: 20px;">
          <h5 style="color:navy;">안준홍</h5>
          <p>現 SSAFY 8기 6반 회장</p>
          <p style="font-weight:bold">FrontEnd / BackEnd</p>
          <p>자주하는 말 : “이거 왜 이렇게 했어?”</p>
        </div>
        <div class="member" style="padding: 20px;">
          <h5 style="color:navy;">송진주</h5>
          <p>긍정녀 예쓰걸</p>
            <p style="font-weight:bold">BackEnd</p>
            <p >자주하는 말 : “이거 해도 돼?”</p>
        </div>
      </div>
      <hr>
      <h4 id="service" style="color:black;">Service</h4>
      <div class="service-desc">
        <h4 style="color:black">npm - new perspective of movie</h4>
        <b>당신의 소중한 추억을 나눌수록 당신의 영화 취향이 또렷해져요 !</b>
        <p>여러분의 영화 취향을 남겨주세요.<br> 
        우리가 여러분의 취향과 비슷한 취향을 가진 유저들이 좋아하는 영화들로 추천해 줄 거에요!
        <br>영화만 보세요! 계산과 추천은 저희가 할테니😉</p>
      </div>
      <hr>
      <h4 id="contact" style="color:black;">Contact us</h4>
      <div class="contact">
        <p>서비스를 이용하시면서 궁금하신 점이나 불편하셨던 점이 있다면 언제든 연락주세요!</p>
        <h5>Github repo: <a href="https://github.com/isabel-noh/NoSongGlobal">https://github.com/isabel-noh/NoSongGlobal</a></h5>
        <p style="margin: 2px;">노현정 email : <a href="mailto:nohhyunjeong93@gmail.com">nohhyunjeong93@gmail.com</a></p>
        <p style="margin: 2px;">송진주 email : <a href="mailto:ddelsen3130@gmail.com">ddelsen3130@gmail.com</a></p>
        <p style="margin: 2px;">안준홍 email : <a href="mailto:junhong625@gmail.com">junhong625@gmail.com</a></p>
      </div>
    </div>
  </div>
</template>

<script>
  export default {  
    name:'InfoView',

  }
</script>

<style>
h4{
  font-family: 'Do Hyeon';
  font-weight: bold;
}
.info-body{
  text-align: start;
  margin-bottom: 20rem;
}
.team-desc{
  display: flex;
}
.member{
  /* border: 1px dotted black; */
  width: 50%;
  height: 200px;
  margin-bottom: 10px;
}
.service-desc, .contact {
  margin-bottom: 10px;
  padding: 10px;
  /* border: 1px dotted black; */
  height: 200px;
}
a{
  text-decoration: none;
  color: black;
}
</style>