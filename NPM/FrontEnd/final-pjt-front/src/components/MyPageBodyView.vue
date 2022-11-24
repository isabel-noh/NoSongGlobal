<template>
  <div class="MyPageBodyView">
    <div v-for="journal in userJournalList"
      :key="journal.id"
    >
      <p>{{journal}}</p>
    </div>
  </div>
</template>

<script>
// const API_URL = 'http://127.0.0.1:8000'

export default {
    name:'MyPageBodyView',
    components: {
    },
    methods:{
    },
    created() {
    },
    props: {
      userJournalList:Array
    }
}
</script>

<style>

</style>