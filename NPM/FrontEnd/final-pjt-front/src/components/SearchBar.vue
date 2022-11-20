<template>
  <div class="searchBar">
    <form @submit.prevent="searchKeyword">
        <input class="search-input" type="text" v-model="keyword">    
        <button type="submit" class="btn btn-light" value="검색">검색</button>
    </form>    
  </div>
</template>

<script>
export default {
    name: 'SearchBar',
    data() {
        return {
            keyword: null,
        }
    },
    methods: {
        searchKeyword(){
            console.log(this.keyword)
            const keyword = this.keyword
            this.$store.dispatch('search', keyword)
            this.keyword = null
        }
    },
    // 처음 main 페이지로 오면 전체 영화 list, recommended 리스트 보여줌 
    // 로그인하고 오면 영화 전체 리스트, 그 고객에 맞는 리스트 보여줌
    // 어디페이지에서든지 검색하고 온 거면, 새로 Movie List를 전체를 받아오지 않고 검색한 리스트 보여줌 
    computed: {

    }
}
</script>

<style>
.searchBar {
    padding: 10px;
    border-top: 1px solid lightgrey;
    border-bottom: 1px solid lightgrey;
}
.search-input {
    width: 50%;
    border: none;
    height: 50px;
    margin-right: 10px;
}
</style>