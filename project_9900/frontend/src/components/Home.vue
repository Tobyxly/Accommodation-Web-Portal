
  <template>
    <div>
      <el-row>
        <el-col :span="24" style="margin-top: 20px">
          <div class="grid-content bg-purple-dark">
          <el-carousel :interval="5000" arrow="always" height="500px">
          <el-carousel-item v-for="item in banners" :key="item.imgURL">
            <img :src="item.imgURL">
          </el-carousel-item>
        </el-carousel>
        </div></el-col>
      </el-row>

      <el-row>
        <el-col :span="16">
            <el-form ref="form" :model="form" label-width="80px">
              <el-form-item label="State/City">
                <el-cascader
                  placeholder="please select"
                  expand-trigger="hover"
                  :options="options"
                  v-model="form.selectedOptions"
                  >
                </el-cascader>
              </el-form-item>
              <!--<el-form-item label="address">-->
                <!--<el-input v-model="form.address"></el-input>-->
              <!--</el-form-item>-->

              <div>
                <el-row>
                  <el-col :span="8">
                    <el-button @click="showBtn()" v-show="show2" style="margin: 10px 10px" size="mini">More detail</el-button >
                  </el-col>
                </el-row>
                <div >
                  <el-collapse-transition>
                    <div v-show="show3">
                      <div class="transition-box">
                        <el-form-item label="type">
                          <el-select v-model="form.property_type" placeholder="please select type">
                            <el-option label="apartment" value="apartment"></el-option>
                            <el-option label="unit" value="unit"></el-option>
                            <el-option label="house" value="house"></el-option>
                            <el-option label="studio" value="studio"></el-option>
                            <el-option label="mansion" value="mansion"></el-option>
                          </el-select>
                        </el-form-item>
                        <el-form-item label="duration">
                          <el-col :span="11">
                            <el-date-picker type="date" placeholder="start date" value-format="yyyy-MM-dd" v-model="form.start_date" style="width: 100%;"></el-date-picker>
                          </el-col>
                          <el-col class="line" :span="2">-</el-col>
                          <el-col :span="11">
                            <el-date-picker type="date" placeholder="end date" value-format="yyyy-MM-dd" v-model="form.end_date" style="width: 100%;"></el-date-picker>
                          </el-col>
                        </el-form-item>
                        <!--<el-form-item label="Pets ?">-->
                          <!--<el-switch v-model="form.pets" active-text="Yes" inactive-text="No"></el-switch>-->
                        <!--</el-form-item >-->
                        <el-col :span="8">
                          <el-form-item label="Pets ?">
                            <el-switch
                              v-model="form.pets"
                              active-text="Yes"
                              inactive-text="No">
                            </el-switch>
                          </el-form-item>
                        </el-col>

                        <el-col :span="8">
                          <el-form-item label="Wifi ?">
                            <el-switch
                              v-model="form.wifi"
                              active-text="Yes"
                              inactive-text="No">
                            </el-switch>
                          </el-form-item>
                        </el-col>

                        <el-col :span="8">
                          <el-form-item label="Fitness ?">
                            <el-switch
                              v-model="form.fitness"
                              active-text="Yes"
                              inactive-text="No">
                            </el-switch>
                          </el-form-item>
                        </el-col>

                        <el-col :span="8">
                          <el-form-item label="Bedroom">
                        <el-input-number v-model="form.num_bedroom"  :min="0" :max="10" size="mini"></el-input-number>
                          </el-form-item>
                        </el-col>

                        <el-col :span="8">
                        <el-form-item label="Bathroom">
                            <el-input-number v-model="form.num_bathroom"  :min="0" :max="10" size="mini"></el-input-number>
                        </el-form-item>
                        </el-col>
                        <el-col :span="8">
                        <el-form-item label="Parking">
                          <el-input-number v-model="form.num_parking"  :min="0" :max="10" size="mini"></el-input-number>
                        </el-form-item>
                        </el-col>
                      </div>
                    </div>
                  </el-collapse-transition>
                </div>
              </div>
              <el-button @click="showBtn()" v-if="!show2" style="margin: 10px 10px" size="mini">less detail</el-button >

          <el-col>
                <el-form-item>
                <el-button type="primary" @click="onSubmit">search</el-button>
                <el-button>cancel</el-button>
              </el-form-item>
        </el-col>
            </el-form>
        </el-col>
      </el-row>

      <div>
        <h3
          style="font-family: 'Righteous',cursive;font-size: 2.5em;
          text-transform: capitalize;text-align: center;color: #000">
          Properties we recommend to you </h3>
        <el-row>
          <el-col :span="6" v-for="item in recommend_item" :key="item.img_url" style="margin: 30px 40px" >
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
                    <el-tag size="mini" type="danger">{{item.parking}} Parking</el-tag>
                  </div>
                  <el-button type="text" class="button" style="margin-bottom: 10px"><a :href="'/detail?order_id='+item.order_id">More details...</a></el-button>

                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <br><br>
      </div>

      <div>
        <h3
          style="font-family: 'Righteous',cursive;font-size: 2.5em;
          text-transform: capitalize; text-align: center;color: #000">
          We are Offering the Best Real Estate Deals</h3>
        <el-row>
          <el-col :span="6" v-for="item in property_item1" :key="item.img_url" style="margin: 30px 40px" >
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
                    <el-tag size="mini" type="danger">{{item.parking}} Parking</el-tag>
                  </div>
                  <el-button type="text" class="button" style="margin-bottom: 10px"><a :href="'/detail?order_id='+item.order_id">More details...</a></el-button>

                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>

        <el-row align="middle" style="padding-left: auto;padding-right: auto">
          <el-col :offset="8">
            <el-pagination
              @current-change="handleCurrentChange"
              :current-page="currentPage"
              :page-size="6"
              layout="total, prev, pager, next, jumper"
              :total="property_item.length">
            </el-pagination>

          </el-col>

        </el-row>




      </div>





    </div>
  </template>



<script>
    import axios from 'axios'
    export default {
        name: "Home",
      data(){
          return{
              currentPage:1,
              pageSize:6,
              show2:true,
              show3:false,
              property_item:[],
              property_item1:[],
              recommend_item:[],

            banners:[
              {imgURL:'src/assets/bnr1.jpg'},
              {imgURL:'src/assets/bnr2.jpg'},
              {imgURL:'src/assets/bnr3.jpg'},
            ],
            form: {
              selectedOptions:[],
              address: '',
              property_type: '',
              start_date: '',
              end_date: '',
              pets: false,
              wifi: false,
              fitness: false,
              num_bedroom: 0,
              num_bathroom: 0,
              num_parking: 0,
              resource: '',
              desc: ''
            },
            options: [{
              value: 'NSW',
              label: 'NSW',
              children: [{
                value: 'Sydney',
                label: 'Sydney'
              },
                {
                  value: 'Albury',
                  label: 'Albury'
                },
                {
                  value: 'Griffith',
                  label: 'Griffith'
                },
                {
                  value: 'Newcastle',
                  label: 'Newcastle'
                },
                {
                  value: 'Orange',
                  label: 'Orange'
                },
                {
                  value: 'Wollongong',
                  label: 'Wollongong'
                }]
            },
              {
                value: 'ACT',
                label: 'ACT',
                children: [{
                  value: 'Canberra',
                  label: 'Canberra'
                }]
              },
              {
                value: 'VIC',
                label: 'VIC',
                children: [{
                  value: 'Melbourne',
                  label: 'Melbourne'
                },{
                  value: 'Bendigo',
                  label: 'Bendigo'
                },{
                  value: 'Geelong',
                  label: 'Geelong'
                },{
                  value: 'Swan Hill',
                  label: 'Swan Hill'
                },{
                  value: 'Maryborough',
                  label: 'Maryborough'
                }]
              },
              {
                value: 'QLD',
                label: 'QLD',
                children: [{
                  value: 'Brisbane',
                  label: 'Brisbane'
                },{
                  value: 'Cairns',
                  label: 'Cairns'
                },{
                  value: 'Gold Coast region',
                  label: 'Gold Coast region'
                },{
                  value: 'Southport',
                  label: 'Southport'
                },{
                  value: 'Sunshine Coast region',
                  label: 'Sunshine Coast region'
                }]
              },
              {
                value: 'WA',
                label: 'WA',
                children: [{
                  value: 'Perth',
                  label: 'Perth'
                },{
                  value: 'Albany',
                  label: 'Albany'
                },{
                  value: 'Bunbury',
                  label: 'Bunbury'
                },{
                  value: 'Kalgoorlie',
                  label: 'Kalgoorlie'
                },{
                  value: 'Mandurah',
                  label: 'Mandurah'
                }]
              },
              {
                value: 'SA',
                label: 'SA',
                children: [{
                  value: 'Adelaide',
                  label: 'Adelaide'
                },{
                  value: 'Port Augusta',
                  label: 'Port Augusta'
                },{
                  value: 'Port Lincoln',
                  label: 'Port Lincoln'
                }]
              },
              {
                value: 'TAS',
                label: 'TAS',
                children: [{
                  value: 'Hobart',
                  label: 'Hobart'
                },{
                  value: 'Burnie',
                  label: 'Burnie'
                },{
                  value: 'Devonport',
                  label: 'Devonport'
                },{
                  value: 'Launceston',
                  label: 'Launceston'
                },{
                  value: 'Ross',
                  label: 'Ross'
                }]
              },
              {
                value: 'NT',
                label: 'NT',
                children: [{
                  value: 'Darwin',
                  label: 'Darwin'
                },{
                  value: 'Alice Springs',
                  label: 'Alice Springs'
                },{
                  value: 'Catherine',
                  label: 'Catherine'
                },{
                  value: 'Palmerston',
                  label: 'Palmerston'
                }]
              }]
          }
      },
      created(){
        this.fetchData()
      },
      methods: {
        handleCurrentChange(currentPage){
          this.currentPage = currentPage;
          this.property_item1 = this.property_item.slice((this.currentPage-1)*this.pageSize,this.currentPage*this.pageSize);
          console.log(this.property_item1)
        },
        onSubmit(){
          const formData = {
            owner: sessionStorage.getItem('username'),
            state:this.form.selectedOptions[0],
            city:this.form.selectedOptions[1],
            address:this.form.address,
            start_date:this.form.start_date,
            end_date:this.form.end_date,
            pets:this.form.pets,
            wifi:this.form.wifi,
            fitness: this.form.fitness,
            property_type:this.form.property_type,
            price: this.form.price,
            num_bedroom:this.form.num_bedroom,
            num_bathroom: this.form.num_bathroom,
            num_parking: this.form.num_parking,
          };
          // this.$root._data.searchedData = {};
          // console.log(formData);
          axios.post('http://127.0.0.1:5000/search',formData)
            .then(res=>{
              // console.log(res.data.property_item)
              sessionStorage.setItem('property_item', JSON.stringify(res.data.property_item));
              // this.$root._data.searchedData = res.data.property_item;
              console.log(sessionStorage);
              this.$router.push('/searched');
            });


        },
        showBtn(){
          this.show2 = !this.show2;
          this.show3 = !this.show3;
        },
        fetchData(){
          axios.get('http://127.0.0.1:5000/properties')
            .then(res=>{

              this.property_item = res.data.property_item;
              this.property_item1 = this.property_item.slice((this.currentPage-1)*this.pageSize,this.currentPage*this.pageSize);
              console.log(this.property_item);
              console.log(this.recommend_item)
            });
          axios.post('http://127.0.0.1:5000/recommend',{"username":sessionStorage.getItem("username")})
            .then(res=>{
              this.recommend_item = res.data.recommend_item;
            })
        },

       }
    }
</script>

<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 400px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
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

