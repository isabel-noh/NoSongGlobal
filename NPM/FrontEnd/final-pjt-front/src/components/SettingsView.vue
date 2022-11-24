<template>
  <div class="setting" >
    <h3>개인정보변경</h3>
    <div
        v-if="comp_n === 0" 
        class="mt-3 mb-3 row" style="margin: auto; width: 100%">
        <label for="inputPassword" class="col-sm-2 col-form-label">Password</label>
        <input 
            type="password" 
            class="form-control" 
            id="inputPassword" 
            v-model="inputPassword"
            placeholder="비밀번호를 입력해주세요.">
        <div class="mt-3">
            <input type="button" @click="checkPassword" value="개인정보 수정" >
        </div>
    </div>
    <div
        v-if="comp_n === 1">
        <div class="mt-3">
            <input type="button" @click="changePasswordView" value="비밀번호 수정하기">
        </div>
        <div class="mt-3">
            <input type="button" @click="changeNicknameView" value="닉네임 수정하기">        
        </div>
    </div>
    <div
        v-if="comp_n === 2"
        class="mt-3 mb-3 row" style="margin: auto; width: 100%"
        >
        <label for="nickname" class="col-sm-2 col-form-label">Nickname</label>
        <input type="text" id="nickname" v-model="nickname" class="form-control" placeholder="닉네임을 입력해주세요">
        <input style="margin-top:10px;" type="button" value="닉네임 변경" @click="changeNickname">
    </div>
    <div
        v-else
        class="mt-3 mb-3 row" style="margin: auto; width: 100%"
        >
            <label for="new_password" class="col-sm-2 col-form-label">new password</label>
            <input type="password" id="new_password" v-model="new_password" class="form-control" placeholder="비밀번호를 입력해주세요">
            <label for="new_password2" class="col-sm-2 col-form-label">new password check</label>
            <input type="password" id="new_password2" v-model="new_password2" class="form-control" placeholder="비밀번호를 다시 입력해주세요">
            <input style="margin-top:10px;" type="button" value="비밀번호 변경" @click="changePassword">
    </div>
        <!-- <div  class="mt-3 mb-3 row" style="margin: auto; width: 100%">
            <label for="nickname" class="col-sm-2 col-form-label">Nickname</label>
            <input type="text" id="nickname" v-model="nickname.trim" class="form-control" placeholder="닉네임을 입력해주세요">
        </div>
        <div  class="mt-3 mb-3 row" style="margin: auto; width: 100%">
            <label for="new_password" class="col-sm-2 col-form-label">new password</label>
            <input type="password" id="new_password" v-model="new_password.trim" class="form-control" placeholder="비밀번호를 입력해주세요">
        </div>
        <div  class="mt-3 mb-3 row" style="margin: auto; width: 100%">
            <label for="new_password2" class="col-sm-2 col-form-label">new password check</label>
            <input type="password" id="new_password2" v-model="new_password2.trim" class="form-control" placeholder="비밀번호를 다시 입력해주세요">
        </div> -->

    <!-- </div> -->
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
            user: null,
            nickname: null,
            new_password: null,
            new_password2: null,
        }
    },
    methods: {
        checkPassword(){
            const local = localStorage.getItem('vuex')
            const user = JSON.parse(local)
            axios({
                method: 'GET',
                url: `${API_URL}/auth/mypage/`,
                headers:{
                    'Authorization': `Token ${user.token}`
                },
                data: {
                    password: this.inputPassword
                }
            })
            .then ((response) => {
                this.$store.commit('MY_PAGE_COMPONENT', 1)
                this.user = response.data
            })
            .catch((err) => {
                console.log(err)
            })
        },
        changeNicknameView(){
            this.$store.commit('MY_PAGE_COMPONENT', 2)
        },
        changePasswordView(){
            this.$store.commit('MY_PAGE_COMPONENT', 3)
        },
        changeNickname(){
            const local = localStorage.getItem('vuex')
            const user = JSON.parse(local)
            axios({
                method: 'PUT',
                url: `${API_URL}/auth/mypage/`,
                headers:{
                    'Authorization': `Token ${user.token}`
                },
                data: {
                    password: this.new_password,
                    password2: this.new_password2,
                }
            })
            .then (() => {
                alert('비밀번호가 변경되었습니다.')
                this.$router.push({ name : 'home' })
            })
            .catch((err) => {
                console.log(err)
            })
        },
        changePassword(){
            const local = localStorage.getItem('vuex')
            const user = JSON.parse(local)
            axios({
                method: 'PUT',
                url: `${API_URL}/auth/mypage/`,
                headers:{
                    'Authorization': `Token ${user.token}`
                },
                data: {
                    nickname: this.nickname
                }
            })
            .then (() => {
                alert('닉네임이 변경되었습니다.')
                this.$router.push({ name : 'home' })
            })
            .catch((err) => {
                console.log(err)
            })
        }
    },
    computed:{
        comp_n() {
            return this.$store.getters.myPageComponent
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