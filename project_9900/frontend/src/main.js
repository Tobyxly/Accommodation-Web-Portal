import Vue from 'vue'
import VueRouter from 'vue-router'
import  {routes} from './routes'
import App from './App.vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import enLocale from 'element-ui/lib/locale/lang/en';
import * as VueGoogleMaps from 'vue2-google-maps'

import axios from 'axios'
// axios.defaults.withCredentials=true;

Vue.use(VueRouter);
Vue.use(ElementUI,{enLocale});
// Vue.use(VueGoogleMaps,{load:{key:"AIzaSyDS-dDteE7EY2QbgpUcI4mn6DA_HcJV_DU",libraries: "places"}});



const router = new VueRouter({
  routes,
  mode:'history'
});

new Vue({
  el: '#app',
  router,
  data(){
    return{
      showName:'',
      username:'',
      searchedData:{

      }
    }
  },
  created:function(){ /*页面刷新前先执行函数,根据是否有session数据来渲染页面 */
    if (sessionStorage.length !== 0){
      this.showName = true;
      this.username = sessionStorage.username
    }else {
      this.showName = false
    }
  },
  render: h => h(App)
});


