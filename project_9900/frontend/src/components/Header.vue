<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="py-2" href="/">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="d-block mx-auto"><circle cx="12" cy="12" r="10"></circle><line x1="14.31" y1="8" x2="20.05" y2="17.94"></line><line x1="9.69" y1="8" x2="21.17" y2="8"></line><line x1="7.38" y1="12" x2="13.12" y2="2.06"></line><line x1="9.69" y1="16" x2="3.95" y2="6.06"></line><line x1="14.31" y1="16" x2="2.83" y2="16"></line><line x1="16.62" y1="12" x2="10.88" y2="21.94"></line></svg>
      </a>
      <a href="/" class="navbar-brand" style="font-family:'Arial Rounded MT Bold',cursive">iHome Find what you want!</a>
      <ul class="navbar-nav">
        <!--<li><router-link :to="homeLink" class="nav-link">主页</router-link></li>-->
        <li><router-link :to="{name:'homeLink'}" class="nav-link">Home</router-link></li>
        <li v-if="user_type === 'landlord' || user_type==='noLogin'"><router-link :to="{name:'releaseLink'}" class="nav-link">Release property</router-link></li>
        <li v-if="user_type === 'tenant' || user_type==='noLogin'"><router-link :to="{name:'orderLink'}" class="nav-link">My orders</router-link></li>
        <li v-if="user_type === 'landlord' || user_type==='noLogin'"><router-link :to="{name:'myReleaseLink'}" class="nav-link">My releases</router-link></li>
        <li><router-link :to="{name:'aboutLink'}" class="nav-link">About us</router-link></li>
      </ul>

      <ul class="navbar-nav ml-auto">
        <li v-if="!$root._data.showName"><router-link :to="{name:'loginLink'}" class="nav-link">Login</router-link></li>
        <li v-if="!$root._data.showName"><router-link :to="{name:'registerLink'}" class="nav-link">Register</router-link></li>
        <li v-if="$root._data.showName"><router-link :to="{name:'profileLink'}" class="nav-link"><img src="../assets/profile.png" style="height: 30px;width: 30px;"></router-link></li>
        <li v-if="$root._data.showName"><router-link :to="{name:'homeLink'}" class="nav-link"><span style="font-size: smaller">Welcome:{{$root._data.username}}</span></router-link></li>
        <li v-if="$root._data.showName"><el-button @click="logout()" icon="el-icon-back">logout</el-button></li>
      </ul>

    </nav>
  </header>
</template>

<script>

    export default {
        name: "Header",
        data(){
          return{
            user_type:''
          }
        },
        created(){
          if(sessionStorage.hasOwnProperty("user_type")){
            this.user_type = sessionStorage.getItem("user_type")
          }else{
            this.user_type = 'noLogin'
          }
        },
        methods:{
            logout(){
              this.$root._data.showName = false;
              sessionStorage.removeItem('username');
              sessionStorage.removeItem('property_item');
              sessionStorage.removeItem('user_type');
              this.$router.go(0);
              this.$router.push('/')
            }
        }

    }
</script>

<style scoped>

</style>
