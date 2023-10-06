import axios from 'axios'
const service =axios.create({
    timeout:5000,
    baseURL:process.env.VUE_APP_BASE_API,
})
//请求拦截器
service.interceptors.request.use(
    config=>{
        window.sessionStorage.getItem('Authorization')//获取认证信息
        if(token){
            config.headers['Authorization']='Bearer'+token
        }
        return config
},
error=>{
    console.log('req',error)
    return Promise.reject(error)
}
)

//响应拦截器
service.interceptors.response.use(
    response=>{
        const res =response.data//获取认证信息
        return res
},
error=>{
    console.log('err',error)
    return Promise.reject(error)
}
)
export default service