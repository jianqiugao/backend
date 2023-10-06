// import './assets/main.css'

// import { createApp } from 'vue'
// import App from './App.vue'
// import router from './router'

// const app = createApp(App)

// app.use(router)

// app.mount('#app')
import Vue from'vue'
import ElementUI from 'element-plus';
import 'element-plus/theme-chalk/index.css';
import App from './App.vue'
import moment from 'moment'
import router from './router'

const whiteList =['/login']
//定义路由守卫，在未登录时将页面跳转到登录页面
router.beforeEach(async(to,from,next)=>{
    const hasToken = window.sessionStorage.getItem('Authorization')
    //consol.log(hasToken)
    if (hasToken){
        if(to.path==='/login'){
            next({path:'/'})
        }else{next()}
    }else{
        if(whiteList.indexOf(to.path)!=-1){
            next()
        }else{
            next('/login')
        }
    }
})
//初始化vue配置项
Vue.config.productionTip = false
Vue.prototype.$moment=moment
// 启用Elenment框架
Vue.use(ElementUI)
new Vue({
    el:'#app',
    router:router,
    render:h=>h(App),
})