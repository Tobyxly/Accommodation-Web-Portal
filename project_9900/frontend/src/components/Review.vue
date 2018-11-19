<template>
  <el-form>

    <div>
      <el-row  style="margin-top: 30px">
        <el-col :span="24">
          <!--<div  class="grid-content bg-white" style="margin:30px 100px 10px;">-->
          <h3>{{property_item.address}}</h3>
          <p>January 05, 2016 / John Doe / Uncategorized / 0 Comments</p >
          <img :src="property_item.img_url">
          <pre><h4 style="margin-bottom: 20px">Price: {{property_item.price}}               Available Date:   <span style="color: #4cae4c">{{property_item.start_date}}</span>   ~  <span style="color: #4cae4c">{{property_item.end_date}}</span></h4></pre>
          <h4>Description:</h4>
          <p>{{property_item.desc}}</p >
          <el-tag  style="margin-top: 5px; margin-right: 20px"> Bedrooms: {{property_item.bedroom}}</el-tag>
          <el-tag  type="success" style="margin-right: 20px"> Bathrooms: {{property_item.bathroom}}</el-tag>
          <el-tag  type="info" style="margin-right: 20px"> Parking: {{property_item.parking}}</el-tag>
          <el-tag type="warning" style="margin-right: 20px">Pets: {{property_item.pets}}</el-tag>
          <el-tag type="danger" style="margin-right: 20px">Fitness: {{property_item.fitness}}</el-tag>
          <el-tag  style="margin-right: 20px;color: #606266">Wifi: {{property_item.wifi}}</el-tag>
          <!--</div>-->
          <!--<div style="margin-left: 90px;margin-top: 30px;margin-bottom: 300px">-->
          <!---->

          <!--</div>-->

        </el-col>

      </el-row>

    </div>

    <div class="block" style="margin: 20px">
      <span class="demonstration" style="margin-up: 20px">Your mark:</span>
      <el-rate
        v-model="value2"
        :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
      </el-rate>
    </div>

    <el-col :span="12" style="margin-bottom: 20px">
      <el-input
        type="textarea"
        :autosize="{ minRows: 8, maxRows: 12}"
        placeholder="Please input your review."
        v-model="review1" style="margin-bottom: 20px">
      </el-input>
    </el-col>

    <el-col :span="24" style="margin-bottom: 20px">
      <el-form-item>
        <el-button type="primary" @click="confirmOrder">Review Now!</el-button>
        <el-button>Cancel</el-button>
      </el-form-item>
    </el-col>

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



  </el-form>
</template>

<script>
  import axios from 'axios'
  export default {
    name: "Review",
    data(){
      return{
        centerDialogVisible: false,
        property_item:'',
        value2:null,
        review1:''
      }
    },
    created(){
      // console.log(this.$route.query.order_id);
      this.fetchData()
    },
    methods:{
      confirmOrder(){
        console.log(this.$route.query.order_id);
        const formatData ={
          "username":sessionStorage.getItem("username"),
          "order_id":this.$route.query.order_id,
          "review":this.review1,
          "rating":this.value2
        };
        console.log(formatData);

        axios.post("http://127.0.0.1:5000/new_review",formatData)
          .then(res=>{
            this.$alert(res.data.message, {
              confirmButtonText: 'Continue',
              center: true,
              callback:action=> {
                this.$router.go(-1);
            }});
          });
        this.centerDialogVisible = false
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
