color: black;
<template>
  <div class="create-journal-view">
    <h2>Add My Movie Moment</h2>
    <div class="journal-form">
        <form @submit.prevent="addJournal" >
            <div class="content-div">
                <label for="journal_title" style="margin-right:10px;">제목: </label>
                <input 
                    id="journal_title" type="text" 
                    v-model="journal_title"
                    placeholder="글 제목을 입력해주세요">
            </div>
            <div class="content-div">
                <label for="movie_title" style="margin-right:10px;">영화 제목: </label>
                <input 
                    id="movie_title"
                    type="text" v-model="movie_title" placeholder="영화제목을 선택해주세요">
            </div>
            <div class="content-div">
                <label for="journal_date" style="margin-right:10px;">날짜: </label>
                <input
                    id="journal_date" 
                    type="date" v-model="journal_date">
            </div>
            <div class="content-div">
                <label for="journal_content" style="margin-right:10px;">글 내용</label>
                <div class="form-floating">
                    <textarea class="form-control" 
                    v-model="journal_content"
                    placeholder="공유하고 싶은 내용을 입력해주세요" id="floatingTextarea2" style="height: 100px"></textarea>
                    <label for="floatingTextarea2">Content</label>
                </div>
                <!-- <div>
                    <textarea
                        id="journal_content"
                        v-model="journal_content"
                        placeholder="공유하고 싶은 내용을 입력해주세요"></textarea>
                </div> -->
            </div>
            <div class="content-div">
                <label for="setImg" style="margin-right:10px;">이미지: </label>
                <input 
                    id="setImg"
                    type="file"  
                    @change="encodeFileToBase64"
                    style="width:170px">
                <div id="imgPreview-box" v-if="{uploadPreview}">
                    <img :src="uploadPreview" id="imgPreview">
                </div>
            </div>
            <input type="submit" value="전송">
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
            uploadPreview:null,
        }
    },
    methods:{
        addJournal(){
            const movie_title = this.movie_title
            const journal_title = this.journal_title
            const journal_content = this.journal_content
            const journal_date = this.journal_date
            const journal_img = this.journal_img
            const data = {
                movie_title : movie_title,
                journal_title : journal_title,
                journal_content : journal_content,
                journal_date : journal_date,
                journal_img : journal_img,
            }
            this.$store.dispatch('addJournal', data)
        },
        encodeFileToBase64 (e){
            const reader = new FileReader()
            const file = (e.target.files[0])
            this.journal_img = e.target.files[0]
            reader.readAsDataURL(file);
            return new Promise (() => {
                reader.onload = () => {
                    this.uploadPreview = reader.result;
                }
            })
        },
        
    },
    mounted(){
      var now_utc = Date.now()
      var timeOff = new Date().getTimezoneOffset()*60000;
      var today = new Date(now_utc-timeOff).toISOString().split("T")[0];
      document.getElementById("journal_date").setAttribute("max", today);
        }
}
</script>

<style>
.create-journal-view{
    font-family: 'Do Hyeon';
}
.journal-form{
    max-width: 500px;
    margin: 10px auto;
}
.content-div{
    margin: 5px auto;
    width: 100%;
    text-align: start;
}
.content-div input{
    width: 80%;
}
.content-div label{
    width: 16%;
}
.content-div textarea{
    width: 100%;
    min-height: 100px;
}
#imgPreview{
    width: 100%;
    height: auto;
    margin: 0px auto;
}
</style>