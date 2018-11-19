<template>
  <div>
    <el-row  style="margin-top: 30px">
      <el-col :span="24">
        <h3>{{property_item.address}}</h3>
      </el-col>
      <el-col :span="24">
        <p>Peoperty owner: {{property_item.owner}}</p>
      </el-col>
      <el-col :span="12">
        <img :src="property_item.img_url" style="width: 500px;height: 400px">
      </el-col>
      <el-col :span="12">
        <!--<img :src="property_item.img_url" style="width: 500px;height: 400px">-->
      </el-col>
    </el-row>
    <el-row>
      <el-col>
        <pre><h4 style="margin-bottom: 20px">Price: {{property_item.price}} $/day              Available Date:   <span style="color: #4cae4c">{{property_item.start_date}}</span>   ~  <span style="color: #4cae4c">{{property_item.end_date}}</span></h4></pre>

        <h4>Description:</h4>
        <p>{{property_item.desc}}</p>
        <el-tag  style="margin-top: 5px; margin-right: 20px"> Bedrooms: {{property_item.bedroom}}</el-tag>
        <el-tag  type="success" style="margin-right: 20px"> Bathrooms: {{property_item.bathroom}}</el-tag>
        <el-tag  type="info" style="margin-right: 20px"> Parking: {{property_item.parking}}</el-tag>
        <el-tag type="warning" style="margin-right: 20px">Pets: {{property_item.pets}}</el-tag>
        <el-tag type="danger" style="margin-right: 20px">Fitness: {{property_item.fitness}}</el-tag>
        <el-tag  style="margin-right: 20px;color: #606266">Wifi: {{property_item.wifi}}</el-tag>

      </el-col>
    </el-row>
    <!--<div style="margin-left: 90px;margin-top: 30px;margin-bottom: 300px">-->

    <!--<el-button type="primary" round="" @click="centerDialogVisible = true">Booking Now !</el-button>-->

    <!--<el-dialog-->
    <!--title="Tips"-->
    <!--:visible.sync="centerDialogVisible"-->
    <!--width="30%"-->
    <!--center>-->
    <!--<span>Are you sure you want to book this property ？</span>-->
    <!--<span slot="footer" class="dialog-footer">-->
    <!--<el-button @click="centerDialogVisible = false">Cancel</el-button>-->
    <!--<el-button type="primary" @click="confirmOrder">Confirm</el-button>-->
    <!--</span>-->
    <!--</el-dialog>-->


    <!--</div>-->
    <el-row>
      <el-col :span="8">

        <h4>Start Date:</h4>
        <el-date-picker type="date" placeholder="Select your start date" value-format="yyyy-MM-dd" v-model="start_date_user" style="width: 100%;"></el-date-picker>

      </el-col>
      <el-col :span="8" style="margin-left: 100px">
        <h4>End Date:</h4>
        <el-date-picker type="date" placeholder="Select your end date" value-format="yyyy-MM-dd" v-model="end_date_user" style="width: 100%;"></el-date-picker>
      </el-col>
      <el-col>
        <div style="margin-top: 30px;margin-bottom: 300px">

          <el-button type="primary" round="" @click="centerDialogVisible = true">Booking Now !</el-button>

          <el-dialog
            title="Tips"
            :visible.sync="centerDialogVisible"
            width="30%"
            center>
            <span>Are you sure you want to book this property ？</span>
            <span slot="footer" class="dialog-footer">
              <el-button @click="centerDialogVisible = false">Cancel</el-button>
              <el-button type="primary" @click="confirmOrder">Confirm</el-button>
            </span>
          </el-dialog>


        </div>
      </el-col>
    </el-row>


  </div>

</template>

<script>
  import axios from 'axios'
  export default {
    name: "propertyDetail",
    data(){
      return{
        centerDialogVisible: false,
        property_item:'',
        start_date_user:'',
        end_date_user:''
      }
    },
    created(){
      // console.log(this.$route.query.order_id);
      this.fetchData()
    },

    methods:{
      confirmOrder(){
        console.log(this.start_date_user,this.end_date_user);
        console.log(this.$route.query.order_id);
        const formatData ={
          "username":sessionStorage.getItem("username"),
          "order_id":this.$route.query.order_id,
          "start_date_user":this.start_date_user,
          "end_date_user":this.end_date_user
        };
        if(sessionStorage.hasOwnProperty("username")){
          if(formatData.start_date_user === '' || formatData.end_date_user === ''){
            this.$alert("Please select date you wanna order !", {confirmButtonText: 'Continue', center: true});
            this.centerDialogVisible = false;
          }else{
            axios.post("http://127.0.0.1:5000/new_order",formatData)
              .then(res=>{
                if(res.data.code === 200){
                  this.$alert(res.data.message, {confirmButtonText: 'Continue', center: true});
                  this.$router.push('/order')
                }else{
                  this.$alert(res.data.message, {confirmButtonText: 'Continue', center: true});
                  this.centerDialogVisible = false
                }

              });
          }
        }else{
          this.$alert("Please login first!", {confirmButtonText: 'Continue', center: true});
          this.$router.push('/login')
        }

        // this.centerDialogVisible = false;

      },
      GMTToStr(time){
        let date = new Date(time)
        let Str=date.getFullYear() + '-' +
          (date.getMonth() + 1) + '-' +
          date.getDate()
        return Str
      },
      fetchData(){
        axios.get(`http://127.0.0.1:5000/detail?order_id=${this.$route.query.order_id}`)
          .then(res=>{
            this.property_item = res.data.property_item;
            let start = this.GMTToStr(this.property_item.start_date);
            let end = this.GMTToStr(this.property_item.end_date);
            this.property_item.start_date = start;
            this.property_item.end_date = end;
            // console.log(this.property_item)
          })
      }
    }
  }
</script>

<style scoped>
  h3 {
    font-size: 2.5em;
    font-family: 'Righteous', cursive;
    color: #000;
  }
  p {
    font-size: 1em;
    color: #777;
    /*padding: 1em 0;*/
    line-height: 1.8em;
  }
  img {
    margin-bottom: 20px;
  }
  h4 {
    font-size: 1.5em;
    font-family: 'Righteous', cursive;
    color: #000;
  }
  .el-row {
    margin-bottom: 20px;
  &:last-child {
     margin-bottom: 0;
   }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  /*.bg-purple-light {*/
  /*background: #e5e9f2;*/
  /*}*/
  img{ width:50%;height:50%; }
</style>
