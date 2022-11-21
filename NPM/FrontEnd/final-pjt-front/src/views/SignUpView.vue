<template>
  <div class="signUp">
    <div id="signup-logo">
        <!-- <h2>New<br/>
        Perspective<br/>
        of<br/>
        Movie</h2> -->
        <h2>회원가입</h2>
    </div>
    <form @submit.prevent="signup">
        <div class="signup-form">
            <p>
                <label for="name">이름: </label>
                <input id="name" type="text" v-model="name" autocomplete="off" required minlength="2" maxlength="4">
            </p>
            <p>
                <label for="nickname">닉네임: </label> 
                <input id="nickname" type="text" v-model="nickname" autocomplete="off" required minlength="2" maxlength="8">
            </p>
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
            <div>
                <p>좋아하는 음악 장르를 선택해주세요. (최대 3개)</p>
                <input type="checkbox" name="check" value="genre_1" @click="clickBox"><label for="genre_1">OST</label>
                <input type="checkbox" name="check" value="genre_2" @click="clickBox"><label for="genre_2">발라드</label>
                <input type="checkbox" name="check" value="genre_3" @click="clickBox"><label for="genre_3">재즈</label>
                <input type="checkbox" name="check" value="genre_4" @click="clickBox"><label for="genre_4">pop</label>
                <input type="checkbox" name="check" value="genre_5" @click="clickBox"><label for="genre_5">힙합</label>
                <input type="checkbox" name="check" value="genre_6" @click="clickBox"><label for="genre_6">클래식</label>
                <input type="checkbox" name="check" value="genre_7" @click="clickBox"><label for="genre_7">트로트</label>
                <input type="checkbox" name="check" value="genre_8" @click="clickBox"><label for="genre_8">뮤지컬</label>
                <input type="checkbox" name="check" value="genre_9" @click="clickBox"><label for="genre_9">락</label>
            </div>
        </div>
        
        <input type="submit" value="가입하기">
    </form>
  </div>
</template>

<script>

export default {
    name: 'SignUpView',
    data() {
        return {
            name: null,
            nickname: null,
            email: null,
            password1: null, 
            password2: null,
            preferMusicGenre: [],
        }
    },
    components: {
    },
    methods: {
        signup(){ 
            const name = this.name;
            const nickname = this.nickname;
            const email = this.email;
            const password1 = this.password1;
            const password2 = this.password2;
            const preferMusicGenre = this.preferMusicGenre;

            const payload = {
                name: name,
                nickname: nickname,
                email: email,
                password1: password1,
                password2: password2,
                preferMusicGenre: preferMusicGenre,
            }

            if (this.password1 != this.password2) {
                alert('비밀번호가 일치하지 않습니다.')
            }
            if (!this.name.trim) {
                alert('성함을 입력해주세요.')
            }
            if (!this.nickname.trim) {
                alert('별명을 입력해주세요.')
            }
            if (!this.email.trim) {
                alert('이메일을 입력해주세요.')
            }
            if (!this.preferMusicGenre) {
                alert('좋아하시는 음악 장르를 선택해주세요.')
            }
            this.$store.dispatch('signUp', payload)

        },
        // 3개 이상 클릭하면 alert뜨고 전 선택 취소되게 하기
        // 선택했던 것은 취소되게 하기
        clickBox(event){
            if (!event.target.checked) {
                this.preferMusicGenre = this.preferMusicGenre.filter((el) => el != event.target.value)
            } else {
                if (this.preferMusicGenre.length > 2) {
                    alert('최대 3개까지 선택하실 수 있습니다.');
                    event.target.checked = false
                } else {
                    this.preferMusicGenre.push(event.target.value)
                }
            }
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
.signup-form input[type=text], input[type=email] {
    width: 70%;
    color: black;
}
#password1, #password2 {
    width: 70%;
    color: black;
}
.signup-form input[type=submit] {
    border: 1px solid black;
    margin: auto;
}
</style>