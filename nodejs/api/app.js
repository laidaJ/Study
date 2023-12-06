//导入express
const express = require('express');
//创建服务器
const app = express()

//导入并配置cors
const cors = require('cors');
app.use(cors())

//配置解析表单数据中间件
app.use(express.urlencoded({ extended: false }))

//启动服务器
app.listen(3007, () => {
    console.log('api server running at http://127.0.0.1:3007');
})