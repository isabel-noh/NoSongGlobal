<template>
  <div class="MyPageHeader">
    MyPageHeader
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name:'MyPageHeader',
    data(){
      return{
        user:null,
      }
    },
    methods:{
      getProfile(){
        axios({
          method:'GET',
          url: `${API_URL}/`
        })
      }
    },
    created(){
      // this.getProfile()
    },
    updated(){
      // this.getProfile()
    }
}
</script>

<style>

</style>