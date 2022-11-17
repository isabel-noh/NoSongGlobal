<template>
  <div id="app">
    <nav>
      <div class="nav1">
        <router-link :to="{ name : 'home' }" > 
          <span id="logo" @click="hideSearchBar">npm</span> 
          <span id="logo_desc" @click="hideSearchBar">new perspective of movie</span>
        </router-link>
      </div>
      <div class="nav2">
        <router-link :to="{ name : 'info' }" @click.native="hideSearchBar">Info</router-link> |
        <!-- 검색 기능 -->
        <a @click="showSearchBar = !showSearchBar">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
          </svg> |
        </a>
        <router-link @click.native="hideSearchBar" :to="{ name : 'journal' }">Journal</router-link> | 
        <!-- user정보에 따라 바뀜 -->
        <button v-if="!isLogin" @click="openModal = !openModal, hideSearchBar()" >Login</button>
        <div class="btn-group" v-if="isLogin">
          <button type="button" class="btn btn-white dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
            Action
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" @click="logOut">sign out</a></li>
            <li><router-link class="dropdown-item" :to="{ name : 'myPage' }" >MyPage</router-link></li>
          </ul>
        </div>
      </div>
    </nav>
    <Transition>
      <SearchBar v-if="showSearchBar"/>
    </Transition>
    <Transition>
      <LoginModal v-if="openModal" @closeModal="closeModal"/>
    </Transition>
    <router-view/>
  </div>
</template>

<script>
import LoginModal from '@/components/LoginModal'
import SearchBar from '@/components/SearchBar'

export default {
  name: 'App',
  components: {
    LoginModal,
    SearchBar
  },
  data(){
    return {
      isLogin : false,
      openModal: false,
      showSearchBar: false,
    }
  },
  methods: {
    isLoggedIn(){
      this.isLogin = this.$store.getters.isLogin
    },
    closeModal(){
      this.openModal = false
    },
    hideSearchBar(){
      this.showSearchBar = false
    },
    logOut(){
      this.$store.dispatch('logOut')
    }
  },
  mounted(){
    this.isLoggedIn()
  },
  updated(){
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
