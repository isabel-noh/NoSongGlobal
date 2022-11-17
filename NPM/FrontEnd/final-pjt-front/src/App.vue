<template>
  <div id="app">
    <nav>
      <div class="nav1">
        <router-link :to="{ name : 'home' }"> <span id="logo">npm</span>  <span id="logo_desc">new perspective of movie</span></router-link>
      </div>
      <div class="nav2">
        <router-link :to="{ name : 'info' }">Info</router-link> |
        <!-- 검색 기능 -->
        <router-link :to="{ name : 'journal' }">Journal</router-link> | 
        <!-- user정보에 따라 바뀜 -->
        <button v-if="!isLogin" @click="openModal = !openModal">Login</button>
        <router-link  v-if="isLogin" :to="{ name : 'myPage' }">MyPage</router-link>
      </div>
    </nav>
    <Transition>
      <LoginModal v-if="openModal" @closeModal="closeModal"/>
    </Transition>
    <router-view/>
  </div>
</template>

<script>
import LoginModal from '@/components/LoginModal'
export default {
  name: 'App',
  components: {
    LoginModal
  },
  data(){
    return {
      isLogin : false,
      openModal: false,
    }
  },
  methods: {
    isLoggedIn(){
      this.isLogin = this.$store.getters.isLogin()
    },
    closeModal(){
      this.openModal = false
    }
  },
  create(){
    this.isLoggedIn()
  }
}
</script>


<style>
.v-application {
  font-family: 'Hannah', sans-serif !important;
}
@font-face {
  font-family: "Hannah";
  font-style: normal;
  src: url('./fonts/BMHANNA_11yrs_ttf.ttf') format("tff");
  font-weight: 400;
}

#app {
  font-family: "Hannah", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
  padding: 0px 15%;
  background-color: #fff;
  /* background-color: #2c3e50; */
}

nav {
  font-family: 'Hannah';
  padding: 30px 0px;
  display: flex;
  justify-content: space-between;
}

nav a {
  font-family: "Hannah";
  font-weight: bold;
  color: black;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #202945;
}

#logo {
  font-size: 2rem;
  color: #202945;
  text-decoration: none;
}

a #logo_desc {
  font-size: 1rem;
  color: lightgray;
  text-decoration: none;
}

.nav2{
  margin: auto 0px;
}
/* input 기본 스타일 초기화 */
/* input {
    -webkit-appearance: none;
       -moz-appearance: none;
            appearance: none;
} */

/* input type number 에서 화살표 제거 */
/* input[type='number']::-webkit-inner-spin-button,
input[type='number']::-webkit-outer-spin-button {
    -webkit-appearance: none;
       -moz-appearance: none;
            appearance: none;
} */
/* Select box 스타일 초기화 */ 
/* select {
    -webkit-appearance: none;
       -moz-appearance: none;
            appearance: none;
} */
</style>
