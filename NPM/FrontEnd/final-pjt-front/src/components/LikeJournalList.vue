<template>
  <div class="journal-lists" style="margin-bottom: 10rem;">
    <div class="row row-cols-1 row-cols-md-5">
    <div class="col" 
      @click="goToDetailPage(journal?.id)"
      v-for="journal in journalList" 
      :key="journal.pk" style="margin-bottom:10px;">
        <div class="container">        
          <div class="item front" v-if="journal?.journal_image">
            <div
              class="card-img-top item front rounded-2"
              :style="{ backgroundImage:`url(${journal?.journal_image})`,
                        backgroundSize: 'cover', 
                        backgroundPosition: 'center'}">
            </div>  
          </div>
          <div class="item front" 
            v-else
            style="margin-bottom:10px;">
            <div
              class="card-img-top item front rounded-2"
              :style="{ backgroundImage:`url(https://image.tmdb.org/t/p/w500${journal?.poster_path})`, backgroundSize:'cover'}">
            </div>
          </div>
          <div class="card item back">
            <div class="card-body">
              <h5 class="card-title">{{journal.title}}</h5>
              <p class="card-text">{{journal.movieTitle}}</p>
            </div>
            <div class="card-footer">
              <small class="text-muted">
                date: {{journal.watched_at}}
              </small>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LikeJournalList',
  computed:{
    journalList() {
        return this.$store.getters.likeJournalList
      },
  },
  methods:{
    goToDetailPage(id){
      this.$router.push({name : 'journalDetail', params:{journal_id :id}})
    },
  },
}
</script>

<style>

</style>