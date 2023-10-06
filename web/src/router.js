import Vue from'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import Layout from '@/views/layout'//导入布局组件
//定义路由表
export const constantRouters = [
    {
        path:'/',//定义路由指向根路径
        component: Layout,
        redirect:'./person',
        children:[
            {
                path:'yuyuecode',
                component:()=>import('@/views/yuyuecode'),
                name:'yuyuecode',
                meta:{title:'预约二维码',icon:'el-icon-s-grid'}
            },
            {
                path:'person',
                component:()=>import('@/views/person'),
                name:'yuyuecode',
                meta:{title:'预约信息查询',icon:'dashboard'}
            },
            {
                path:'checkin',
                component:()=>import('@/views/checkin'),
                name:'yuyuecode',
                meta:{title:'登记信息查询',icon:'dashboard'}
            },
        ]
    },
    {
        path:'/login',
        component:()=>import('@/views/login'),
    },
]
const createRouter =()=>new VueRouter({
    scrollBehavior:()=>({y:0}),
    routes:constantRouters
})
//创建路由实例
const router = createRouter()
export function resetRouter(){
    const newRouter = createRouter()
    router.matcher = newRouter.matcher
}
export default router