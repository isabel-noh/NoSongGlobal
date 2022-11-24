<template>
  <div>
    <form>
      <p>회원정보 수정을 위해 비밀번호를 입력하세요.</p>
      <label for="password">비밀번호</label>
      <input v-model="password" id="password" type="password">
      <button @click.prevent="moveToProfile" type="submit">입력</button>
    </form>
  </div>
</template>

<script>
// import axios from 'axios'
export default {
  name: 'ChangeProfileView',
  data() {
    return {
      password : ''
    }
  },
  methods: {
    moveToProfile() {
      const payload = {
        username : this.$store.getters.userData.username ,
        password : this.password,
      }
      console.log(payload)
      this.$store.dispatch('logIn', payload)
      
      // if (this.$store.dispatch('login', payload)) {
      //   this.$router.push({
      //     name: 'change-profile'
      //   })
      // }
      // else {
      //   alert('비밀번호 오류입니다.')
      // }
    }
  }
}
</script>

<style>

</style>
