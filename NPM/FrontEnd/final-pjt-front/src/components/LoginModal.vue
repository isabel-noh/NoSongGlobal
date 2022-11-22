<template>
  <div class="loginModal" @click="closeModal">
    <div id="login-div">
      <form id="login-form" @submit.prevent="login" @click.stop=''>
        <div id="input-div">
          <h4 style="margin-top:10px; color: whitesmoke;">Login</h4>
          <div class="user-info-box">
            <label for="username" style="margin-right: 8px;">이메일: </label>
            <input type="email" v-model="username"
              style="padding-left: 8px;"/>
          </div>
          <div class="user-info-box">
            <label for="password" style="margin-right: 8px;">비밀번호: </label>
            <input type="password" v-model="password"
              style="padding-left: 8px;"/>
          </div>
        </div>
        <button type="submit" class="btn btn-dark">로그인하기</button>
      </form>
      <div style="padding: 10px 0px;">
        <p style="margin:0px;">회원이 아니신가요? 
          <router-link 
            id="goToSignUp"
            @click.native="closeModal"
            :to="{name: 'signUp'}" >회원가입하러 가기</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'LoginModal',
    data(){
      return {
        username: null,
        password: null,
      }
    },
    methods: {
      login(){
        const username = this.username
        const password = this.password
        
        if (!username.trim) {
          alert('이메일을 입력해주세요.')
        }
        if (!password.trim) {
          alert('비밀번호를 입력해주세요.')
        }

        const payload = {
          username: username,
          password: password,
        }
        // console.log(payload)
        this.$store.dispatch('logIn', payload)
        this.$emit('closeModal')
      },
      closeModal(){
        this.$emit('closeModal')
      },

    }
}
</script>

<style>
.loginModal {
  align-items: center;
  justify-content: center;
  position: fixed;
  z-index: 30;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
}

@media (max-width: 900px) {
  #login-div {
    width: 400px;
  }
}
.user-info-box{
  margin: 0px auto 10px auto;
}
#login-div{
  padding-top: 2px;
  max-width: 300px;
  margin: 20% auto 2% auto;
  height: auto;
  border-radius: 10px;
  background-color: black;
  color: white;
}
#login-div input[type=email], input[type=password]{
  background-color: transparent;
  border: none;
  border-bottom: 1px solid white;
  color: white;
}
#input-div{
  margin: 4%;
}
#login-form input {
  margin: 4px auto;
}
#goToSignUp{
  color: aliceblue;
}
#goToSignUp:hover{
  color: blanchedalmond;
}
</style>