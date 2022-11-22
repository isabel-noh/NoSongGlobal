<template>
  <div class="signUp">
    <div id="signup-logo">
        <h2>회원가입</h2>
    </div>
    <div v-if="!second_page">
        <form @submit.prevent="signup">
            <div class="signup-form">
                <p>
                    <label for="email">이메일: </label>  
                    <input id="email" type="email" v-model="email" autocomplete="off" required>
                </p>
                <p>
                    <label for="password1">비밀번호: </label> 
                    <input id="password1" type="password" v-model="password1" autocomplete="off" required>
                </p>
                <p>
                    <label for="password2">비밀번호 확인: </label> 
                    <input id="password2" type="password" v-model="password2" autocomplete="off" required>
                </p>
            </div>
            
            <input type="submit" value="다음으로">
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
                        type="file" style="margin:20px auto; display: none;"/>
                </div>
                <p>
                    <label for="name">성함: </label>  
                    <input id="name" type="name" v-model="name" autocomplete="off" required>
                </p>
                <p>
                    <label for="nickname">닉네임: </label> 
                    <input id="nickname" type="nickname" v-model="nickname" autocomplete="off" required>
                </p>
                <div>
                    <p>좋아하는 음악 장르를 선택해주세요. (최대 3개)</p>
                    <input type="checkbox" name="check" value="genre_1" @click="clickBox">
                    <label for="genre_1">OST</label>
                    <input type="checkbox" name="check" value="genre_2" @click="clickBox">
                    <label for="genre_2">발라드</label>
                    <input type="checkbox" name="check" value="genre_3" @click="clickBox">
                    <label for="genre_3">재즈</label>
                    <input type="checkbox" name="check" value="genre_4" @click="clickBox">
                    <label for="genre_4">pop</label>
                    <input type="checkbox" name="check" value="genre_5" @click="clickBox">
                    <label for="genre_5">힙합</label>
                    <input type="checkbox" name="check" value="genre_6" @click="clickBox">
                    <label for="genre_6">클래식</label>
                    <input type="checkbox" name="check" value="genre_7" @click="clickBox">
                    <label for="genre_7">트로트</label>
                    <input type="checkbox" name="check" value="genre_8" @click="clickBox">
                    <label for="genre_8">뮤지컬</label>
                    <input type="checkbox" name="check" value="genre_9" @click="clickBox">
                    <label for="genre_9">락</label>
                </div>
            </div>
            
            <input type="submit" value="가입하기">
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
            this.second_page = true
            // this.$store.dispatch('signUp', payload)
            
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
            }).
            catch((error) => {
                console.log(error)
            })
            
        },
        addUserData(){
            //`/addfields/`
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
                url: `${API_URL}/useraddfields/`,
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
.signup-form {
    width: 50% ;
    margin: 20px auto 30px auto;
    text-align: left ;
}
.signup-form p {
    border-bottom: 1px solid black;
}
.signup-form input {
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
}
#password1, #password2 {
    width: 60%;
    color: black;
}
.signup-form input[type=submit] {
    border: 1px solid black;
    margin: auto;
}
</style>