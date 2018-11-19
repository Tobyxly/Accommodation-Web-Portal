<template>
  <div>
    <el-table
      :data="tableData3"
      style="width: 100%"
    >
      <el-table-column
        fixed
        prop="order_id"
        label="order_id"
        width="120">
      </el-table-column>
      <el-table-column
        prop="owner"
        label="owner"
        width="120">
      </el-table-column>
      <el-table-column
        prop="start_date"
        label="start_date"
        width="120">
      </el-table-column>
      <el-table-column
        prop="end_date"
        label="end_date"
        width="120">
      </el-table-column>
      <el-table-column
        prop="price"
        label="price"
        width="120">
      </el-table-column>
      <el-table-column
        prop="city"
        label="city"
        width="120">
      </el-table-column>
      <el-table-column
        prop="address"
        label="address"
        width="200">
      </el-table-column>

      <el-table-column label="Operation">
        <template slot-scope="scope">
          <el-button type="primary" plain @click="handleEdit(scope.$index, scope.row)">Review</el-button>
        </template>
      </el-table-column>
    </el-table>

    <div class="row" style="margin-top: 50px">
      <div class="col-4">
        <img src="src/assets/p.png">
        <br><br>
        <h4>Search From Anywhere</h4>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis egestas rhoncus. Donec facilisis fermentum sem, ac viverra ante luctus vel.</p>
      </div>
      <div class="col-4">
        <img src="src/assets/p1.png">
        <br><br>
        <h4>Friendly Agents</h4>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis egestas rhoncus. Donec facilisis fermentum sem, ac viverra ante luctus vel.</p>
      </div>
      <div class="col-4">
        <img src="src/assets/p2.png">
        <br><br>
        <h4>Buy or Rent</h4>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis egestas rhoncus. Donec facilisis fermentum sem, ac viverra ante luctus vel.</p>
      </div>
    </div>
  </div>




</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        tableData3: []
      }
    },
    methods: {
      handleEdit(index, row) {
        this.$router.push(`/review?order_id=${this.tableData3[index].order_id}`)
      },
      GMTToStr(time){
        let date = new Date(time)
        let Str=date.getFullYear() + '-' +
          (date.getMonth() + 1) + '-' +
          date.getDate()
        return Str
      },
      fetchData(){
        axios.post('http://127.0.0.1:5000/my_order',{'username':sessionStorage.getItem('username')})
          .then(res=>{
            for(let i=0;i<res.data.order_item.length;i++){
              res.data.order_item[i].start_date = this.GMTToStr(res.data.order_item[i].start_date);
              res.data.order_item[i].end_date = this.GMTToStr(res.data.order_item[i].end_date);
              res.data.order_item[i].price = res.data.order_item[i].price + ' $'
            }
            this.tableData3 = res.data.order_item;
          })
      }
    },
    beforeRouteEnter(to,from,next){
      if(sessionStorage.hasOwnProperty("username") === false){
        // this.$alert('Please log in !',{confirmButtonText:'Continue',center: true});
        next(vm=> {
          vm.$alert('Please log in !', {confirmButtonText: 'Continue', center: true});
          vm.$router.push('/login')
        })
      }else{
        next()
      }
    },
    created(){
      this.fetchData()
    }
  }
</script>

<style scoped>

</style>
