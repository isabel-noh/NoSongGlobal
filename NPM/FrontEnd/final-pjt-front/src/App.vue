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
        <!-- 비로그인 -->
        <button class="btn btn-light" 
        v-if="!isLogin" 
        @click="openModal = !openModal, hideSearchBar()" >Login</button>
        <!-- 로그인 -->
        <div class="btn-group" v-if="isLogin">
          <!-- 여기 아래 username 들어가야함 -->
          <button
            v-if="nickname" 
            type="button" 
            class="btn btn-light dropdown-toggle" 
            style="font-family:'Do Hyeon'; font-weight: bold;" 
            data-bs-toggle="dropdown" aria-expanded="false">
            {{nickname}}
          </button>
          <button
            v-else 
            type="button"
            class="btn btn-light dropdown-toggle" 
            style="font-family:'Do Hyeon'; font-weight: bold;" 
            data-bs-toggle="dropdown" aria-expanded="false">
            사용자님
          </button>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" @click="logOut">LogOut</a></li>
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
    SearchBar,
  },
  data(){
    return {
      // nickname: null,
      // isLogin : false,
      openModal: false,
      showSearchBar: false,
    }
  },
  methods: {
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
  computed:{
    isLogin(){
      return this.$store.getters.isLogin
    },
    nickname(){
      return this.$store.getters.userData.nickname
    }
  },
  created(){
    this.$store.dispatch('loadMovieData')
  }
}
</script>


<style>
#app {
  min-width: 672px;
  /* font-family:Helvetica, Arial, sans-serif; */
  font-family: 'Roboto', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
  padding: 0px 15%;
  background-color: #fff;
  /* background-color: #2c3e50; */
}

nav {
  font-family: 'Do Hyeon';
  padding: 20px 0px;
  display: flex;
  justify-content: space-between;
}

nav a {
  font-family: 'Do Hyeon';
  font-weight: bold;
  color: black;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #202945;
}

#logo {
  font-size: 4rem;
  color: #202945;
  text-decoration: none;
}

@media (max-width: 900px) {
  #logo {
    font-size: 2rem;
  }
}

a #logo_desc {
  font-size: 1.5rem;
  color: lightgray;
  text-decoration: none;
}

@media (max-width: 900px) {
  a #logo_desc {
    font-size: 1rem;
  }
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
