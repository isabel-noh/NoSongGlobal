<template>
  <div>
    <h1 class="m-5">회원정보 수정</h1>
    <div class="d-flex w-100 align-items-center">
      <label class="inputbox" for="nickname ">닉네임</label>
      <input class="form-control" 
        style="width:20rem;"
      v-model="nickname" id="nickname" type="text"><br>
      <button @click.prevent="updateNickname" class="btn btn-light" type="submit">수정</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NicknameChange.vue',
  data() {
    return{
      nickname:null,
    }
  },
  methods:{
    updateNickname() {
      this.$store.dispatch('updateNickname', this.nickname)
    }
  }
}
</script>

<style>
.inputbox {
  margin-left:16rem;
}
</style>