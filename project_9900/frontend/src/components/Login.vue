<template>
  <div class="row mt-3">
    <div class="col-md-12 col-lg-12">
      <div class="card">
        <div class="card-body">
          <img class="mx-auto d-block" src="../assets/icon.png">
          <form @submit.prevent="onSubmit">
            <div class="form-group">
              <label for="username">Username</label>
              <input type="text" class="form-control" v-model="username"/>
            </div>
            <div class="form-group">
              <label for="password">Password</label>
              <input type="password" class="form-control" v-model="password"/>
            </div>
            <div class="form-group">
              <label for="option">Options:</label><br><br>
              <el-radio v-model="radio" label="tenant">Login as tenant</el-radio>
              <el-radio v-model="radio" label="landlord">Login as landlord</el-radio>
            </div>
            <button type="submit" class="btn btn-block btn-success">Login</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
    export default {
        name: "Login",
        data(){
          return{
            username:'',
            password:'',
            radio:'tenant',
          }
        },
        methods:{
          onSubmit(){
            const Dataform = {
              username:this.username,
              password: this.password
            };
            if(Dataform.username === '') {
              this.$alert('Username can not be null', {confirmButtonText: 'Continue', center: true});
            }else if(Dataform.password === ''){
              this.$alert('Password can not be null', {confirmButtonText: 'Continue', center: true});
            }else{
              axios.post('http://127.0.0.1:5000/login',Dataform)
                .then(res=>{
                  if(res.data.code === 200){
                    this.$root._data.showName = true;
                    this.$root._data.username = res.data.username;
                    sessionStorage.setItem('username', res.data.username);
                    sessionStorage.setItem('user_type',this.radio)
                    console.log(this.$root._data.username);
                    this.$alert(res.data.message,{
                      confirmButtonText:'Continue',
                      center: true,
                      callback:action=>{
                        this.$router.push('/')
                        this.$router.go(0);
                      }});
                  }else if(res.data.code === 400){
                    this.$alert(res.data.message,{confirmButtonText:'Continue',center: true});
                    this.$router.push('/login')
                  }
                })
            }
          }
        }
    }
</script>

<style scoped>

</style>
