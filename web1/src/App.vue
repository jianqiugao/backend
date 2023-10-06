<template>
  <div>
    <!-- 页面顶部 -->
    <el-card :body-style="{padding:'2px'}">
    <h1>预约信息查询</h1>
    </el-card>
    <!-- 页面主体 -->
    <el-card class="=box">
      <!-- 查询框部分 -->
      <div style="display: flex;padding-bottom: 12px;">
        <div style="margin-right: 10px;">
          <span style="width: 50px;margin-right: 10px;">姓名</span>
          <el-input size="mini" v-model="search.xm" style="width: 100px;"/>
        </div>
        <div style="margin-right: 10px;">
          <span style="width: 50px;margin-right: 10px;">联系电话</span>
          <el-input size="mini" v-model="search.lxdh" style="width: 100px;"/>
        </div>
        <div style="margin-right: 10px;">
          <span style="width: 50px;margin-right: 10px;">居住地址</span>
          <el-input size="mini" v-model="search.jzdz" style="width: 100px;"/>
        </div>
        <div>
          <el-button type="primary" size="mini" @click="doLoad">查询</el-button>
        </div>
      </div>
  <!-- 数据列表部分 -->
  <el-table :data="list" border>
    <el-table-column label="编号" prop="id"/>
    <el-table-column label="登记日期" prop="djrq" width="160px">
    <!-- 自定义列表显示内容，格式化登记日期 -->
    <template slot-scope="scop">
      {{ $moment(scope.row.djrq).format('YYY 年M 月D 日 HH:mm') }}
      </template>
    </el-table-column>
    <el-table-column label="姓名" prop="xm"/>
    <el-table-column label="性别" prop="xb">
    <!-- 自定义列表显示内容，格式化登记日期 -->
    <template slot-scope="scop">
      {{ getXb(scope.row.xb)}}
      </template>
    </el-table-column>
    <el-table-column label="年龄" prop="nl"/>
    <el-table-column label="出生日期" prop="csrq" width="120px">
    <!-- 自定义列表显示内容，格式化登记日期 -->
    <template slot-scope="scope.row.csrq">
      <span v-if ="scope">
      {{ $moment(scope.row.csrq).format('YYY 年M 月D 日 HH:mm') }}
      </span>
      </template>
    </el-table-column>
    <el-table-column label="居住地址" prop="jzdz"/>  
    <el-table-column label="联系电话" prop="lxdh"/>  
    <el-table-column label="身份证号" prop="lxdh"/>  
  </el-table>
  <!-- 分页组件 -->
  <el-pagination
  @size-change="handleSizeChange"
  @current-change="handleCurrentChange"
  :current-page.sync="pager.page"
  :page-szie="10"
  layout="total,prev,pager,next"
  :total="page.count">
  </el-pagination>
  </el-card>
  </div>
  </template>
  
  <script>
  import {getPersonList} from '@/api'
  export default{
    name:'Person',
    data(){
      return{
        list:[],
        search:{
          xm:'',
          lxdh:'',
          jzdz:''
        },
        pager:{
          count:0,
          page:1,
          size:10,
        }
      }
    },
    mounted(){
      this.doLoad()
    },
    methods:{
      doLoad(){
        getPersonList(Object.assign(this.search,this.page))
        .then(res=>{
          this.list =res.list
          this.pager.count=res.count
        })
      },
      getXb(v){
        if(v=='1'){return '男'}
        else if(v=='2'){return '女'}
        else{return '未知'}
      },
      handleSizeChange(v){
        this.pager.size=v;
        this.pager.page =1;
        this.doLoad()},
      handleCurrentChange(v){
      this.pager.page=v;
      this.doLoad()},
    }
  }
  </script>
  
  
  <style scoped>
  .box{
    margin-top: 10px;
  }
  
  </style>