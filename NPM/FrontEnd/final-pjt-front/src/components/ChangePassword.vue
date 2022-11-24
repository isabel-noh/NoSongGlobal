<template>
  <div>
    <h1>회원정보 수정</h1>
    <form>
      <!-- <label for="nickname">닉네임</label>
      <input class="form-control w-50 m-auto" v-model="nickname" id="nickname" type="text"><br> -->
      <!-- <label for="currentPassword">현재 비밀번호</label>
      <input class="form-control w-50 m-auto" v-model="currentPassword" id="currentPassword" type="password"><br> -->
      <label for="changePassword1">변경할 비밀번호</label>
      <input class="form-control w-50 m-auto" v-model="changePassword1" id="changePassword1" type="password"><br>
      <label for="changePassword2">비밀번호 확인</label>
      <input class="form-control w-50 m-auto" v-model="changePassword2" id="changePassword2" type="password"><br>
      <button class="btn btn-primary" type="submit" @click.prevent="changeProfile">수정 완료</button>
    </form>
    <br><br><br><br>
    
    <a @click.prevent="check" class="btn btn-danger" href="">회원 탈퇴</a><br>
    <span class="border border-danger m-auto rounded-2 text-danger ospanacity-50">회원탈퇴시 모든 정보가 삭제되니 신중하게 선택하세요.</span>
  </div>
</template>

<script>
export default {
  name: 'ChangeProfile',
  data() {
    return {
      nickname: '',
      currentPassword: '',
      changePassword1: '',
      changePassword2: '',
    }
  },
  methods: {
    changeProfile() {
      console.log(this.changePassword1)
      if (this.changePassword1 && this.changePassword2 && (this.changePassword1 === this.changePassword2)) {
        console.log(this.changePassword2)
        const newPassword = {
          new_password1 : this.changePassword1,
          new_password2 : this.changePassword2,
        }
        this.$store.dispatch('changePassword', newPassword)
      } else {
        alert('비밀번호 수정에 실패하였습니다!')
      }
      // if (this.nickname) {
      //   this.$store.dispatch('changeNickname', this.nickname)
      // }
    },
    check(){
      if (confirm("정말 탈퇴하시겠습니까??") == true){    //확인
        this.$store.dispatch('deleteUser')
        this.$store.dispatch('logout')
        alert('회원탈퇴 완료')
      }else{   //취소
        return
      }
    }
  }
}
</script>

<style>

</style>