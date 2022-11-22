<template>
  <div class="myPage">
    <MyPageHeader/>
    <MyPageTabbar/>
    <MyPageBodyView/>
  </div>
</template>

<script>
import MyPageHeader from '@/components/MyPageHeader'
import MyPageTabbar from '@/components/MyPageTabbar'
import MyPageBodyView from '@/components/MyPageBodyView'

export default {
    name:'MyPageView',
    components: {
      MyPageHeader,
      MyPageTabbar,
      MyPageBodyView,
    }
}
</script>

<style>

</style>