<template>
  <div>
    <h3
      style="font-family: 'Righteous',cursive;font-size: 2.5em;
          text-transform: capitalize; text-align: center;color: #000">
      We are Offering the Best Real Estate Deals</h3>
    <el-col :span="6" v-for="item in property_item" :key="item.img_url" style="margin: 30px 40px" >
      <el-card :body-style="{ padding: '0px' }">
        <img :src="item.img_url" class="image">
        <div style="padding: 14px; height: 100px">
          <div style="height: 40px">
            <span>{{item.state}}-{{item.city}}-{{item.address}}</span>
          </div>
          <div class="bottom clearfix">
            <time class="time"> price: {{ item.price }}$</time>
            <time class="time" style="margin-left: 70px"> status: {{ item.status }}</time>
            <div style="margin-bottom: 10px;margin-top: 10px">
              <el-tag size="mini" style="margin-top: 5px">{{item.bedroom}} Bedrooms</el-tag>
              <el-tag size="mini" type="success">{{item.bathroom}} Bathrooms</el-tag>
              <el-tag size="mini" type="info">{{item.parking}} Parking</el-tag>
            </div>
            <el-button type="text" class="button" style="margin-bottom: 10px"><a :href="'/detail?order_id='+item.order_id">More details...</a></el-button>

          </div>
        </div>
      </el-card>
    </el-col>
  </div>


</template>

<script>
  import axios from 'axios'
  export default {
    name: "searchedPage",
    data(){
      return{
        property_item:''
      }
    },
    created(){
      // this.property_item = '';
      console.log(sessionStorage);
      if(sessionStorage.getItem("property_item") === "undefined"){
        this.$alert('No any results..Please search again', {confirmButtonText: 'Continue', center: true});
        this.$router.push('/')
      }else{
        this.property_item=JSON.parse(sessionStorage.getItem("property_item"));
      }


      console.log(this.property_item)
    },
  }


</script>

<style scoped>
  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }
</style>
