<template>
  <div>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="state_city"
        label="state/city"
        width="120">
      </el-table-column>
      <el-table-column
        prop="address"
        label="address"
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
        prop="type"
        label="type"
        width="120">
      </el-table-column>
      <el-table-column
        prop="status"
        label="status"
        width="250">
      </el-table-column>

      <el-table-column label="Operation">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleEdit(scope.$index, scope.row)">View</el-button>
          <!--<el-button-->
            <!--size="mini"-->
            <!--type="danger"-->
            <!--@click="handleDelete(scope.$index, scope.row)">Delete</el-button>-->

          <el-button type="danger" size="mini" @click="centerDialogVisible = true">Delete</el-button>

          <el-dialog
            title="Tips"
            :visible.sync="centerDialogVisible"
            width="30%"
            center>
            <span>Are you sure you want to delete this property ？</span>
            <span slot="footer" class="dialog-footer">
              <el-button @click="centerDialogVisible = false">Cancel</el-button>
              <el-button type="primary" @click="handleDelete(scope.$index, scope.row)">Confirm</el-button>
            </span>
          </el-dialog>


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
        name: "checkRelease",
        data(){
          return{
            centerDialogVisible: false,
            tableData: []
          }
        },
        methods: {
          handleEdit(index, row) {
            console.log(index, row);
            this.$router.push(`/detail?order_id=${this.tableData[index].order_id}`)
          },
          handleDelete(index, row) {
            axios.post('http://127.0.0.1:5000/delete_order',{'order_id':this.tableData[index].order_id})
              .then(res=>{
                this.$alert(res.data.message, {confirmButtonText: 'Continue', center: true});
                this.$router.go(0)
              });
            console.log(index, row);
          },
          GMTToStr(time){
            let date = new Date(time)
            let Str=date.getFullYear() + '-' +
              (date.getMonth() + 1) + '-' +
              date.getDate()
            return Str
          },
          fetchData(){
            axios.post('http://127.0.0.1:5000/my_house',{'username':sessionStorage.getItem('username')})
              .then(res=>{
                for(let i=0;i<res.data.house_item.length;i++){
                  res.data.house_item[i].start_date = this.GMTToStr(res.data.house_item[i].start_date);
                  res.data.house_item[i].end_date = this.GMTToStr(res.data.house_item[i].end_date);
                  res.data.house_item[i].price = res.data.house_item[i].price + ' $'
                }
                this.tableData = res.data.house_item;
                console.log(this.tableData)
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
