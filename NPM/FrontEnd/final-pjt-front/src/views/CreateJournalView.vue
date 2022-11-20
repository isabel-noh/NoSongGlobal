<template>
  <div class="create-journal-view">
    <h2>Add My Movie Moment</h2>
    <div class="journal-form">
        <form @submit.prevent="addJournal">
            <div class="content-div">
                <label for="journal_title">제목: </label>
                <input 
                    id="journal_title" type="text" 
                    v-model="journal_title"
                    placeholder="글 제목을 입력해주세요">
            </div>
            <div class="content-div">
                <label for="movie_title">영화 제목: </label>
                <input 
                    id="movie_title"
                    type="text" v-model="movie_title" placeholder="영화제목을 선택해주세요">
            </div>
            <div class="content-div">
                <label for="journal_date">날짜: </label>
                <input
                    id="journal_date" 
                    type="date" v-model="journal_date">
            </div>
            <div class="content-div">
                <label for="journal_content">글 내용</label>
                <div>
                    <textarea
                        id="journal_content"
                        v-model="journal_content"
                        placeholder="공유하고 싶은 내용을 입력해주세요"></textarea>
                </div>
            </div>
            <div class="content-div">
                <label for="setImg">이미지: </label>
                <input 
                    id="setImg"
                    type="file" @change="setImgUrl">

            </div>
        </form>
    </div>
  </div>
</template>

<script>
export default {
    name: 'CreateJournalView',
    data(){
        return{
            movie_title:null,
            journal_title:null,
            journal_content:null,
            journal_date:null,
            journal_img:null,
        }
    },
    methods:{
        addJournal(){

        },
        setImgUrl(ab){
            console.log(ab.target.value)
        }
    }
}
</script>

<style>
.create-journal-view{
    font-family: 'Do Hyeon';
}
.journal-form{
    width: 100%;
    margin: auto;
}
.content-div{
    margin: 10px auto;
}
</style>