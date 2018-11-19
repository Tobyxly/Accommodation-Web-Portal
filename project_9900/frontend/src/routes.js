import Home from './components/Home'
import myRelease from './components/myRelease'
import myOrders from './components/myOrders'
import About from './components/about/About'
import Login from './components/Login'
import Register from './components/Register'
import Profile from './components/Profile'
import searchedPage from './components/searchedPage'
import propertyDetail from './components/propertyDetail'
import Review from './components/Review'
import checkRelease from './components/checkRelease'
import Map from './components/map'

//二级路由
import History from './components/about/History'
import Contact from './components/about/Contact'


export const routes = [
  {
    path:'/',
    name:"homeLink",
    component:Home
  },
  {
    path:'/release',
    name:"releaseLink",
    component:myRelease,

  },
  {
    path:'/order',
    name:"orderLink",
    component:myOrders
  },
  {
    path:'/about',
    name:"aboutLink",
    component:About,
    children:[
      {
        path:'/history',
        name:"historyLink",
        component:History
      },
      {
        path:'/contact',
        name:"contactLink",
        component:Contact
      }
    ]
  },
  {
    path:'/register',
    name:"registerLink",
    component:Register
  },
  {
    path:'/login',
    name:"loginLink",
    component:Login
  },
  {
    path:'/myProfile',
    name:"profileLink",
    component:Profile
  },
  {
    path:'/searched',
    name:"searchedLink",
    component:searchedPage
  },
  {
    path:'/detail',
    name:'detailLink',
    component:propertyDetail
  },
  {
    path:'/review',
    name:'reviewLink',
    component:Review
  },
  {
    path:'/my_release',
    name:'myReleaseLink',
    component:checkRelease
  },
  {
    path:'/map',
    name:'myMap',
    component:Map
  },
  {
    path:'*',
    redirect:'/'
  }

]
