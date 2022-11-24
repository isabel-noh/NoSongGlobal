<!-- 
  - journal detail 이동 오류 수정
  - 페이지 새로고침 시 이미지 로드 되지 않는 오류 수정
-->

<template>
  <div class="MyPageBodyView">
    <div class="journal-lists" style="margin-bottom: 10rem;">
        <div class="row row-cols-1 row-cols-md-5">
          <!-- 아래 반복 -->
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
                v-if="journal?.isActive_url"
                style="margin-bottom:10px;">
                <div
                  class="card-img-top item front rounded-2"
                  :style="{ backgroundImage:`url(https://image.tmdb.org/t/p/w500/${journal?.poster_path})`,
                          backgroundSize: 'cover'}">
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
      this.$store.commit('USER_JOURNAL_LIST', this.userJournalList)
    },
    props: {
      userJournalList:Array
    },
    computed: {
      journalList() {
        return this.$store.getters.userJournalList
      }
    }
}
</script>

<style>

</style>