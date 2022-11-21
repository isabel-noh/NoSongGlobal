<template>
  <div class="JournalDetailView">
    <h1>JournalDetailView</h1>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'JournalDetailView',
    data(){
        return{
            journal: null,
        }
    }, 
    methods: {
        getJournal(){
            axios({
                method:'GET',
                url: `${API_URL}/journal`,
                params:{
                    journal_id:this.$route.params.journal_id
                }
            })
            .then((response) => {
                this.journal = response.data
                console.log(this.journal)
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created(){
        this.getJournal()
    }
}
</script>

<style>

</style>