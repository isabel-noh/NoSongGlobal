<template>
  <div class="MovieListView">
    <div style="display: flex">
        <div class="select_genre" style="margin-right:10px;">
            <select class="form-select form-select-sm" aria-label=".form-select-sm example">
            <option selected>GENRE</option>
            <option value="genre1">Romance</option>
            <option value="genre2">Action</option>
            <option value="genre3">Drama</option>
            <option value="genre4">Documentary</option>
            <option value="genre5">Children</option>
            <option value="genre6">Comedy</option>
            <option value="genre7">Horror</option>
            </select>
        </div>
        <div class="select_sorting">
            <select class="form-select form-select-sm" aria-label=".form-select-sm example">
            <option selected>Sort by</option>
            <option value="new">New</option>
            <option value="old">Old</option>
            <option value="high">Rated(Ascending)</option>
            <option value="low">Rated(Descending)</option>
            <option value="high_views">Views(Ascending)</option>
            <option value="low_views">Views(Descending)</option>
            </select>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name:'MovieListView',
    data(){
        return {
            movieList:[],
        }
    },
    methods:{
        getMovieList(){

        }
    },
    mounted(){
        this.getMovieList()
    }

}
</script>

<style>

</style>