<template>
  <div class="info">
    <nav>
      <h4>INTRODUCTION</h4>
      <a href="#team">Team</a>
      <a href="#service">Service</a>
      <a href="#contact">Contact us</a>
    </nav>
    <div class="info-body">
      <h4 id="team">Team</h4>
      <div class="team-desc">
        <div class="member" style="margin-right: 10px;">
          <h5 style="text-align:center;">노현정</h5>
          <p>멤버 설명</p>
        </div>
        <div class="member">
          <h5 style="text-align:center;">송진주</h5>
          <p>멤버 설명</p>
        </div>
      </div>
      <h4 id="service">Service</h4>
      <div class="service-desc">
        <h5>Service online desc</h5>
        <p>service description</p>
      </div>
      <h4 id="contact">Contact us</h4>
      <div class="contact">
        <h5>github repo:</h5>
        <p style="margin: 2px;">노현정 email : <a href="mailto:nohhyunjeong93@gmail.com">nohhyunjeong93@gmail.com</a></p>
        <p style="margin: 2px;">송진주 email : <a href="mailto:@gmail.com">@gmail.com</a></p>
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
  border: 1px dotted black;
  width: 50%;
  height: 200px;
  margin-bottom: 10px;
}
.service-desc, .contact {
  margin-bottom: 10px;
  padding: 10px;
  border: 1px dotted black;
  height: 200px;
}
a{
  text-decoration: none;
  color: black;
}
</style>