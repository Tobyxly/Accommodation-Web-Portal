<template>
  <el-row>
    <el-row id="banner">
      <!--<div id="banner_slogan">-->
        <!--<h2>Let's Release!</h2>-->
      <!--</div>-->
    </el-row>
    <el-row :gutter="20">
      <el-col :span="14" >
        <el-form ref="form" :model="form" label-width="110px">
          <el-form-item label="State/City:">

            <el-cascader
              placeholder="please select"
              expand-trigger="hover"
              :options="area_options"
              v-model="form.selectedOptions"
              >
            </el-cascader>
          </el-form-item>

          <el-form-item label="Address:">
            <el-input v-model="form.address" placeholder="Please input your detailed address"></el-input>
          </el-form-item>

          <el-form-item label="Available Time:">
            <el-col :span="11">
              <el-date-picker type="date" placeholder="Select your start date" value-format="yyyy-MM-dd" v-model="form.start_date" style="width: 100%;"></el-date-picker>
            </el-col>
            <el-col class="line" :span="2">-</el-col>
            <el-col :span="11">
              <el-date-picker type="date" placeholder="Select your end date" value-format="yyyy-MM-dd" v-model="form.end_date" style="width: 100%;"></el-date-picker>
            </el-col>
          </el-form-item>

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




          <el-col :span="12">
            <el-form-item label="Type:">
              <el-select v-model="form.property_type" placeholder="Please select">
                <el-option
                  v-for="item in type_options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item label="Price($):">
              <el-input
                placeholder="Please input your price!"
                type="number"
                v-model="form.price"
                clearable>
              </el-input>
            </el-form-item>
          </el-col>


          <el-col :span="8">
            <el-form-item label="Bedroom:">
              <el-input-number v-model="form.num_bedroom"  type="number" :min="0" :max="10" size="mini"></el-input-number>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="Bathroom:">
              <el-input-number v-model="form.num_bathroom" type="number" :min="0" :max="10" size="mini"></el-input-number>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="Parking:">
              <el-input-number v-model="form.num_parking" type="number" :min="0" :max="10" size="mini"></el-input-number>
            </el-form-item>
          </el-col>

          <el-col :span="24">
            <el-form-item label="upload image:">

              <el-upload
                action="http://127.0.0.1:5000/upload"
                list-type="picture-card"
                :limit=1
                :on-success="handleAvatarSuccess"
                :on-preview="handlePictureCardPreview"
                :on-remove="handleRemove">
                <i class="el-icon-plus"></i>
              </el-upload>
              <el-dialog :visible.sync="dialogVisible">
                <img width="100%" :src="dialogImageUrl" alt="">
              </el-dialog>
            </el-form-item>

          </el-col>

          <el-col :span="24">
            <el-form-item label="Description:">
              <el-input type="textarea" v-model="form.desc"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item>
              <el-button type="primary" @click="onSubmit">Release Now!</el-button>
              <el-button>Cancel</el-button>
            </el-form-item>
          </el-col>

        </el-form>
      </el-col>
    </el-row>
  </el-row>

</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        img_name:'',
        dialogImageUrl: '',
        dialogVisible: false,
        form: {
          address: '',
          start_date: '',
          end_date: '',
          pets: false,
          wifi: false,
          fitness: false,
          property_type:'',
          price:'',
          num_bedroom: 0,
          num_bathroom: 0,
          num_parking: 0,
          desc: '',
          selectedOptions:[],
        },
        type_options: [{
          value: 'apartment',
          label: 'Apartment'
        }, {
          value: 'unit',
          label: 'Unit'
        }, {
          value: 'house',
          label: 'House'
        }, {
          value: 'studio',
          label: 'Studio'
        }, {
          value: 'mansion',
          label: 'Mansion'
        }],
        area_options: [{
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
    methods: {
      handleRemove(file) {
        axios.post('http://127.0.0.1:5000/delete_img',{filename: file.name})
        // console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        // console.log(this.dialogImageUrl);
        this.dialogVisible = true;
      },
      handleAvatarSuccess(res,file){
        this.img_name = file.name;
        console.log(this.img_name)
      },
      onSubmit() {
        const formData={
          owner: sessionStorage.getItem('username'),
          selectedOptions:this.form.selectedOptions,
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
          desc:this.form.desc,
          img_name: this.img_name
        };
        // console.log(formData.start_date<formData.end_date);
        if(formData.selectedOptions.length === 0){
          this.$alert('Please select your State/City',{confirmButtonText:'Continue',center: true});
        }else if(formData.address === ''){
          this.$alert('Please input your detailed address',{confirmButtonText:'Continue',center: true});
        }else if(formData.start_date === ''){
          this.$alert('Please select your start date',{confirmButtonText:'Continue',center: true});
        }else if(formData.end_date === ''){
          this.$alert('Please select your end date',{confirmButtonText:'Continue',center: true});
        }else if(formData.start_date >= formData.end_date){
          this.$alert('End date must larger than start date!',{confirmButtonText:'Continue',center: true});
        }else if(formData.property_type ==='') {
          this.$alert('Please select your property type', {confirmButtonText: 'Continue', center: true});
        }else if(formData.price ===''){
            this.$alert('Please input your price',{confirmButtonText:'Continue',center: true});
        }else{
          console.log(formData);
          axios.post('http://127.0.0.1:5000/release',formData)
            .then(res=>{
              if(res.data.code === 200){
                this.$alert(res.data.message,{confirmButtonText:'Continue',center: true});
                this.$router.push('/')
                this.$router.go(0);
              }else{
                this.$alert('Release failed, please try again',{confirmButtonText:'Continue',center: true});
              }
            })
        }


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
    }
  }
</script>

<style scoped>
  #banner_slogan{
    background: #eee;
    opacity: 0.8;
    max-width: 70vw;
    margin: auto auto;
    padding: 20px 0;
  }
  #banner{
    background: url("../assets/banner.jpg");
    height:30vh;
  }
  .el-row {
    margin-top: 10px;
    margin-bottom: 20px;
  &:last-child {
     margin-bottom: 0;
   }
  }
  .el-col {
    border-radius: 4px;
  }

  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }

</style>
