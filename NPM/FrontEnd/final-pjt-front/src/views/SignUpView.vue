<template>
  <div class="signUp" style="padding:0px; margin:0px;">
    <div v-if="!second_page" class="form">
        <div id="signup-logo">
            <h2>회원가입</h2>
        </div>
        <form
            @submit.prevent="signup"
            class="form__content">
            <div class="form__box">
                <input class="form__input" id="email" type="email" v-model="email" autocomplete="off" required>
                <label class="form__label" for="email">이메일: </label>  
                <div class="form__shadow"></div>
            </div>
            <div class="form__box">
                <input class="form__input" id="password1" type="password" v-model="password1" autocomplete="off" required>
                <label class="form__label" for="password1">비밀번호: </label> 
                <div class="form__shadow"></div>
            </div>
            <div class="form__box">
                <input class="form__input" id="password2" type="password" v-model="password2" autocomplete="off" required>
                <label class="form__label" for="password2">비밀번호 확인: </label> 
                <div class="form__shadow"></div>
            </div>
            <div class="form__button">
                <input type="submit" class="form__submit" value="다음으로">
            </div>
        </form>
    </div>
    <!-- second page - 프로필 이미지 설정, 닉네임, 성함, 좋아하는 장르 -->
    <div v-if="second_page">
        <form @submit.prevent="addUserData">
            <div class="signup-form">
                <div class="img-div" style="text-align:center;">
                    <img 
                        style="width: 150px; height: 150px; border-radius: 100px;  margin: 20px auto;"
                        v-if="preview"    
                        @click="handleClick"
                        :src="preview">
                    <img 
                        v-if="!preview"
                        @click="handleClick"
                        src="../assets/profile_img.png"
                        style="width: 150px; height: 150px; border-radius: 100px; margin: 20px auto;"/>
                    <input
                        @change="encodeFileToBase64"
                        ref="profile_img"
                        type="file" 
                        style="margin:20px auto; display: none; 
                        color: transparent; text-shadow: 0 0 0 #2196f3;"/>
                </div>
                <div>
                    <label class="form__label" for="name">성함: </label>  
                    <input class="form__input" id="name" type="name" v-model="name" autocomplete="off" required>
                    <div class="form__shadow"></div>
                </div>
                <div>
                    <label class="form__label" for="nickname">닉네임: </label> 
                    <input class="form__input" id="nickname" type="nickname" v-model="nickname" autocomplete="off" required>
                    <div class="form__shadow"></div>
                </div>
            </div>
            <div class="form__button">
                <input class="form__submit" type="submit" value="가입하기">
                <div class="form__shadow"></div>
            </div>
        </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'SignUpView',
    data() {
        return {
            user: null,
            email: null,
            password1: null, 
            password2: null,
            second_page: false, 
            name: null,
            nickname: null,
            profile_image: null,
            preview: null,
            like_ost_genre: [],
        }
    },
    methods: {
        signup(){ 
            const email = this.email;
            const password1 = this.password1;
            const password2 = this.password2;

            if (this.password1 != this.password2) {
                alert('비밀번호가 일치하지 않습니다.')
            }
            if (!this.email.trim) {
                alert('이메일을 입력해주세요.')
            }
            if(this.password1.length < 8){
                alert('비밀번호가 너무 짧습니다.')
            }
            
            axios({
                method: 'POST',
                url: `${API_URL}/accounts/signup/`,
                data: {
                    username: email,
                    email: email,
                    password1: password1,
                    password2: password2,
                }
            }).
            then((response) => {
                localStorage.setItem('token', response.data.key)
                this.second_page = true
            }).
            catch((error) => {
                if(error.response.data.username[0] === '해당 사용자 이름은 이미 존재합니다.'){
                    alert('중복된 이메일입니다.')
                }
            })
            
        },
        addUserData(){
            const name = this.name;
            const nickname = this.nickname;
            const profile_image = this.profile_image;
            const like_ost_genre = this.like_ost_genre;

            
            if (!this.name.trim) {
                alert('성함을 입력해주세요.')
            }
            if (!this.nickname.trim) {
                alert('닉네임을 입력해주세요.')
            }
            const formdata = new FormData()
            formdata.append('name', name)
            formdata.append('nickname', nickname)
            formdata.append('profile_image', profile_image)
            formdata.append('like_ost_genre', like_ost_genre)
            
            const user = localStorage.getItem('token')
            axios({
                method: 'POST',
                url: `${API_URL}/auth/`,
                headers:{
                    'Content-Type': 'multipart/form-data',
                    'Authorization' : `Token ${user}`,
                },
                data: formdata,
            }).
            then(() => {
                localStorage.removeItem('token')
                this.$router.push({ name : 'home' })
            }).
            catch((error) => {
                alert('회원가입을 다시 진행해주세요.')
                console.log(error)
            })

        },
        // 3개 이상 클릭하면 alert뜨고 전 선택 취소되게 하기
        // 선택했던 것은 취소되게 하기
        clickBox(event){
            if (!event.target.checked) {
                this.like_ost_genre = this.like_ost_genre.filter((el) => el != event.target.value)
            } else {
                if (this.like_ost_genre.length > 2) {
                    alert('최대 3개까지 선택하실 수 있습니다.');
                    event.target.checked = false
                } else {
                    this.like_ost_genre.push(event.target.value)
                }
            }
        },
        encodeFileToBase64 (e){
            console.log(e)
            const reader = new FileReader()
            const file = (e.target.files[0])
            this.profile_image = e.target.files[0]
            reader.readAsDataURL(file);
            return new Promise (() => {
                reader.onload = () => {
                    this.preview = reader.result;
                }
            })
        },
        // 원 클릭시 파일 선택
        handleClick(){
            this.$refs.profile_img.click()
        }
    },
    created(){
        
    },
    updated(){
    }


}
</script>

<style>
#signup-logo{
    width: 40% ;
    margin: auto  ;
    /* text-align: left ; */
}
.form{
    height: 60vh;
    display: grid;
    place-items: center;
    margin: 0 1.5rem;
}

.form__content{
    display: grid;
    row-gap: 1rem;
}
.form__box {
    width: 312px;
    height: 59px;
    position: relative;
}
.form__input, 
.form__label, 
.form__submit{
    border: 0;
    outline: none;
}
.form__shadow{
    position: absolute;
    widows: 100%;
    height: 100%;
    background-color: black;
}
.form__input{
    /* position: absolute; */
    border: 2.5px solid black;
    background-color: white;
    width: 100%;
    height: 100%;
    z-index: 10;
    padding: 18px;
    transition: transform .3s;
}

.form__input::placeholder{
    transition: opacity .5s;;
}

.form__label{
    z-index: 100;
    position: absolute;
    top: 10px;
    left: 20px;
    font-size: .8rem;
    transition: .2s;
    pointer-events: none;
    opacity: 0;
}

.form__button{
    justify-self: flex-end;
    background-color: black;
}
.form__submit{
    padding: .875rem 1.5rem;
    color: black;
    background-color: rgb(242, 160, 3);
    cursor: pointer;
    transition: transform .3s;
}
.form__submit:hover{
    transform: translate(-6px, -6px);
}
.form__input:focus::placeholder{
    opacity: 0;
    transition: .3s;
}
.form__input:focus,
.form__input:not(:placeholder-shown).form__input:not(:focus){
    transform: translate(-8px, -8px);
    padding: 28px 18px 18px;
    animation: input-animation .5s;
}
.form__input:focus + .form__label,
.form__input:not(:placeholder-shown).form__input:not(:focus) + .form__label{
    opacity: 1;
    top: 0px;
    left: 12px;
    transition: .3s;
}
@keyframes input-animation {
    0%{
        transform: translate(0);
    }
    40%{
        transform: translate(-9px, -9px);
    }
    60%{
        transform: translate(-7px, -7px);
    }
}

/* .signup-form input {
    margin: 0px 1rem; 
    background-color: transparent;
    border: none;
}
.signup-form > input[type=text] {
    width: 100%;
    color: black;
}
.signup-form input[type=email]{
    width: 70%;
    color: black;
} */
/* #password1, #password2 {
    width: 60%;
    color: black;
}
.signup-form input[type=submit] {
    border: 1px solid black;
    margin: auto;
} */
</style>