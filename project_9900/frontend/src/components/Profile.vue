<template>
    <el-row style="margin-top: 50px">
      <el-col :span="12">
        <el-form ref="form" :model="form" label-width="150px">
          <el-form-item label="Username:">
            <el-input v-model="form.username" :disabled="true" style="width: 200px"></el-input>
          </el-form-item>

          <el-form-item label="Password:">
            <el-button  @click="dialogFormVisible = true" type="primary" plain>Change password</el-button>
            <el-dialog title="Change password" :visible.sync="dialogFormVisible">
              <el-form :model="form1">
                <el-form-item label="New password:" label-width="200px">
                  <el-input type="password" v-model="form1.password" style="width: 200px"></el-input>
                </el-form-item>
                <el-form-item label="Confirm new password:" label-width="200px" style="margin-top: 10px">
                  <el-input type="password" v-model="form1.confirmedPassword" style="width: 200px"></el-input>
                </el-form-item>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">Cancel</el-button>
                <el-button type="primary" @click="changePassword()">Save</el-button>
              </div>
            </el-dialog>
          </el-form-item>

          <el-form-item label="Email:">
            <input type="email" class="form-control" v-model="form.email" style="width: 200px"/>
          </el-form-item>

          <el-form-item label="First name:">
            <el-input v-model="form.firstName" style="width: 200px"></el-input>
          </el-form-item>

          <el-form-item label="Last name:">
            <el-input v-model="form.lastName" style="width: 200px"></el-input>
          </el-form-item>

          <el-form-item label="Phone:">
            <el-input v-model="form.phone" style="width: 200px"></el-input>
          </el-form-item>

          <el-form-item label="Gender:">
            <el-radio v-model="form.gender" label="male">Male</el-radio>
            <el-radio v-model="form.gender" label="female">Female</el-radio>
          </el-form-item>

          <el-form-item label="Hobby:">
            <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 4}" v-model="form.hobby"></el-input>
          </el-form-item>



          <el-form-item>
            <el-button type="primary" @click="onSubmit">Save</el-button>

          </el-form-item>



        </el-form>
      </el-col>
    </el-row>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        dialogImageUrl: '',
        dialogVisible: false,
        form: {
          username: sessionStorage.username,
          gender: '',
          hobby: '',
          email:'',
          firstName:'',
          lastName:'',
          phone:''
        },
        form1: {
          password:'',
          confirmedPassword:'',
        },
        dialogFormVisible: false,

      }
    },
    created(){
      this.fetchData()
    },
    methods: {
      onSubmit() {
        console.log('submit!');
        const formData={
          username: sessionStorage.username,
          gender: this.form.gender,
          hobby: this.form.hobby,
          email: this.form.email,
          firstName: this.form.firstName,
          lastName: this.form.lastName,
          phone: this.form.phone
        };

        axios.post(`http://127.0.0.1:5000/profile/${sessionStorage.username}`,formData)
          .then(res=>{

              if(res.data.code === 200){
                this.$alert(res.data.message,{confirmButtonText:'Continue',center: true});
              }else{
                this.$alert(res.data.message,{confirmButtonText:'Continue',center: true});
              }
          })
      },
      changePassword(){
        if(this.form1.password === this.form1.confirmedPassword){
          const formData1 = {
            password: this.form1.password,
            confirmedPassword: this.form1.confirmedPassword
          }

          axios.post(`http://127.0.0.1:5000/change_password/${sessionStorage.username}`,formData1)
            .then(res=>{
                if(res.data.code === 200){
                  this.$alert(res.data.message,{confirmButtonText:'Continue',center: true});
                }else{
                  this.$alert(res.data.message,{confirmButtonText:'Continue',center: true});
                }
            })
        }else{
          this.$alert('The confirmed password is inconsistent, please try again.',{confirmButtonText:'Continue',center: true});
        }


        // this.$alert('Release failed, please try again',{confirmButtonText:'Continue',center: true});
        this.dialogFormVisible = false;
      },
      fetchData(){
        axios.get(`http://127.0.0.1:5000/profile/${sessionStorage.username}`)
          .then(res=>{
              this.form.gender = res.data.data.gender;
              this.form.hobby = res.data.data.hobby;
              this.form.email = res.data.data.email;
              this.form.firstName = res.data.data.first_name;
              this.form.lastName = res.data.data.last_name;
              this.form.phone = res.data.data.phone;
          })
      },
      handleRemove(file, fileList) {
        axios.post('http://127.0.0.1:5000/delete_img',{filename: file.name})
        // console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        // console.log(this.dialogImageUrl);
        this.dialogVisible = true;
      },
      handleAvatarSuccess(res,file,fileList){
        console.log(res,file,fileList)
      }
    }
  }
</script>

<style scoped>

</style>
