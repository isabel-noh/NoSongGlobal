<template>
  <div class="setting" >
    <h3>개인정보변경</h3>
    <div
        v-if="!passed" 
        class="mt-3 mb-3 row" style="margin: auto; width: 100%">
        <label for="inputPassword" class="col-sm-2 col-form-label">Password</label>
        <input 
            type="password" 
            class="form-control" 
            id="inputPassword" 
            v-model="inputPassword"
            placeholder="비밀번호를 입력해주세요.">
        <div class="mt-3">
            <input type="button" value="개인정보 수정" >
        </div>
    </div>
    <div
        v-if="passed">
        오호

    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name : 'SettingView',
    data(){
        return{
            inputPassword: null,
            passed : false,
        }
    },
    methods: {
        checkPassword(){
            axios({
                method: 'GET',
                url: `${API_URL}/auth/mypage/`
            })
            this.inputPassword
        }
    }
}
</script>

<style>
.setting{
    margin: 10px auto;
    width: 30vw;
}
</style>