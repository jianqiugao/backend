import request from '@/request'
import qs from 'qs'

//登录函数

export function login(data){
  return request({
    url:'/auth/login',
    method:'post',
    headers:{'Content-Type':'application/x-www-form-urlencoded'},
    data:qs.stringify(data)
  })
}
//获取预约信息函数
export function getPersonList(params){
  return request({
    url:'/person/list',
    method:'get',
    params
  })
}

//获取登记信息列表函数
export function getCheckinList(params){
  return request({
    url:'/checkin/list',
    method:'get',
    params
  })
}