<template>
  <div class="row mt-3">
    <div class="col-md-12 col-lg-12">
      <div class="card">
        <div class="card-body">
          <img class="mx-auto d-block" src="../assets/icon.png">
          <form @submit.prevent="onSubmit">
            <div class="form-group">
              <label for="account">Username</label>
              <input type="text" class="form-control" v-model="username"/>
            </div>
            <div class="form-group">
              <label for="email">Email</label>
              <input type="email" class="form-control" v-model="email"/>
            </div>
            <div class="form-group">
              <label for="password">Password</label>
              <input type="password" class="form-control" v-model="password"/>
            </div>
            <div class="form-group">
              <label for="confirm-password">Confirm Password</label>
              <input type="password" class="form-control" v-model="confirmPassword"/>
            </div>
            <div class="form-group">
              <label for="phone">Phone</label>
              <input type="text" class="form-control" v-model="phone"/>
            </div>
            <div class="form-group">
              <label for="firstName">First Name</label>
              <input type="text" class="form-control" v-model="firstName"/>
            </div>
            <div class="form-group">
              <label for="lastName">Last name</label>
              <input type="text" class="form-control" v-model="lastName"/>
            </div>
            <div class="form-group">
              <label for="sex">Gender:</label>
              <select class="c-select" v-model="gender">
                <option disabled value="">Gender</option>
                <option>male</option>
                <option>female</option>
              </select>
            </div>
            <button type="submit" class="btn btn-block btn-success">Register</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
    export default {
        name: "Register",
        data(){
          return{
            username:'',
            email:'',
            password:'',
            confirmPassword:'',
            phone:'',
            firstName:'',
            lastName:'',
            gender:''
          }
        },
        methods:{
          onSubmit(){
            if(this.password === this.confirmPassword){
              const formData={
                username:this.username,
                email:this.email,
                password:this.password,
                confirmPassword: this.confirmPassword,
                phone:this.phone,
                firstName: this.firstName,
                lastName: this.lastName,
                gender: this.gender
              };
              // console.log(formData)

              if(formData.username === ''){
                this.$alert('Username can not be null',{confirmButtonText:'Continue',center: true});
              }else if(formData.email === ''){
                this.$alert('Email can not be null',{confirmButtonText:'Continue',center: true});
              }else if(formData.password === ''){
                this.$alert('Password can not be null',{confirmButtonText:'Continue',center: true});
              }else{
                axios.post('http://127.0.0.1:5000/register',formData)
                  .then(res=>{
                    // console.log(res.data);
                    // console.log(res.status);
                    if(res.data.code === 200){
                      this.$alert(res.data.message,{confirmButtonText:'Continue',center: true});
                      this.$router.push('/login')
                    }else if(res.data.code === 400){
                      this.$alert(res.data.message,{confirmButtonText:'Continue',center: true});
                      this.$router.push('/register')
                    }
                  })
              }
            }else{
              this.$alert("The confirmed password is inconsistent!",{confirmButtonText:'Continue',center: true});
            }

          }
        }
    }
</script>

<style scoped>

</style>
