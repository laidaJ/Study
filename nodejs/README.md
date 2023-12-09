# Node.js

nodejs是JavaScript的运行环境,现在借用Nodejs可以让JavaScript在浏览器和客户端都能使用;等于用JavaScript语言可以同时开发前端和后端

## 安装

下载网址<https://nodejs.org/>

- LTS为最近的稳定版本(建议下载)
- Current为当前版本

打开终端

```sh
$ node -v
v21.4.0
```

## 内置module

### fs

使用fs对文件进行读取写入

```js
const fs = require('fs');

// Blocking, synchronous way同步的
const textIn = fs.readFileSync('./txt/input.txt', 'utf-8');
console.log(textIn);
const textOut = `This is what we know about the avocado: ${textIn}.\nCreate on ${Date.now()}`;
fs.writeFileSync('./txt/output.txt', textOut);
console.log('File wirtten!');

// Non-blocking, asynchronous way异步的
fs.readFile('./txt/read-this.txt', 'utf-8', (err, data) => { // 后台读取文件
    console.log(data);
})
console.log('Will read file!') // 优先显示这条
```

## http模块

创建web服务器

```js
1. 导入http模块
const http = require('http')
2. 创建web服务器实例
const server = http.createServer()
3. 为服务器实例绑定request事件,监听客户端的请求
server.on('request' (req,res) =>{
    //req.url 是客户端请求的url地址
    const url = req.url
    //req.method 是客户端请求的method类型
    const method = req.method
    const str = 'your request url is ${url}, and request method is ${method}'
    //为了防止中文出现乱码,需要设置响应头 Content-Type 的值为text/html; charset=utf-8
    res.setHeader('Content-Type', 'text/html; charset=utf-8')
    res.end(str)
    console.log(str)
    console.log('someone visit our web server')
})
4. 启动服务器
server.listen(3000, () => {
    console.log('http server running at http://127.0.0.1')
})
```

根据不同的url响应不同的html内容

1. 获取请求的url地址
2. 设置默认的响应内容为404
3. 判断用户的请求是否为/或/index.html
4. 判断用户的请求是否为/about.html
5. 设置Content-Type,解决中文乱码
6. 使用res.end()把内容响应给客户端

```js
server.on('request',(req,res) => {
    const url = req.url
    let content = '<h1>404 Not found</h1>'
    if (url === `/` || url === `/index.html`) {
        content = '<h1>index.html</h1>'
    }else if (url === `/about.html`) {
        content = '<h1>about.html</h1>'
    }
    res.setHeader('Content-Type', 'text/html; charset=uft-8')
    res.end(content)
})
```

实现clock时钟的web服务器

1. 导入所需要的模块
2. 创建基本的web服务器
3. 将资源的请求url映射为文件的存储地址
4. 读取文件内容响应给客户端
5. 优化资源的请求路径

```js
//导入http模块
const http = require('http')
//导入fs模块
const fs = require('fs')
//导入path路径模块
const path = require('path')
const server = http.createServer()
server.on('request', (req,res) => {
    //获取客户端请求的地址
    const url = req.url
    //把请求的url地址映射为具体的文件存放路径
    const fpath = path.join(__dirname, url)
    //优化路径
    const fpath = ''
    if (url === '/') {
        fpath = path.join(__dirname, './public/index.html')
    } else {
        fpath = path.join(__dirname, './public', url)
    }
    
    //根据映射过来的文件路径读取文件的内容
    fs.readFile(fpath, 'uft-8', (err,dataStr) => {
        if(err) return res.end('404 Not Found')
        res.end(dataStr)
    })
})

```

## 模块化

nodejs分类

- 内置模块(nodejs官方提供的如fs,path,http)
- 自定义模块(用户创建的每个.js文件)
- 第三方模块(由第三方开发出来的模块,使用前要先下载)

```js
//加载内置模块
const fs = require('fs')
//加载自定义模块
const custom = require(`./public/index.js`)
//加载第三方模块
const moment = require('moment')
```

使用require()方法加载其他模块时,会执行被加载模块中的代码

### module对象

在每个自定义模块中都会包含一个module对象,里面存储了和当前模块有关的信息

`console.log(module)`

可以使用module.exports,将模块内的成员共享出去,供外界使用

```js
//被导入文件 lesen.js
module.exports.username = 'lesen'
module.exports.sayHello = function() {
    console.log('Hello!')
}
//导入文件
const m = require('./lesen.js')
console.log(m)
```

module.exports可以简化为exports,共享永远以module.exports为主

### 模块化规范

遵循CommonJS规定:

1. 每个模块内容,module变量代表当前模块
2. module变量是一个对象,他的exports属性是对外的接口
3. 加载某个模块,其实是加载该模块的module.exports属性

## npm

npm安装包后,多一个node_modules的文件夹和package-lock.json的配置文件

- node_modules存放已安装到项目中的包.require()导入时,从这个目录中查找并加载
- package-lock.json 配置文件用来记录node_modules 目录下的每个包的下载信息

## express

本质是npm上的一个第三方包,提供了快速创建web服务器的便捷方法,express相当于http的封装包

- 安装
- 你好世界
- Express 生成器
- 基本路由
- 静态文件
- 更多示例
- 常问问题

### 1.安装

假设您已经安装了 Node.js，创建一个目录来保存您的应用程序，并将其设为您的工作目录。

```sh
mkdir express
cd express
#使用 npm init 命令为您的应用程序创建一个 package.json 文件
npm init
#在 myapp 目录中安装 Express 并将其保存在依赖项列表中
npm install express
```

### 2.你好世界

创建的最简单的 Express 应用程序

```js
const express = require('express')
const app = express()
const port = 3000
//启动一个服务器并在端口 3000 上监听连接
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
```

然后使用命令运行程序:`node app.js`

### 3.express的基本使用

- app.get('请求路径', function(req, res){})

```js
//应用程序以 "Hello World!" 响应对根 URL (/) 或路由的请求
app.get('/', (req, res) => {
  res.send('Hello World!')
})
```

- 通过`req.query`对象,可以访问到客户端通过查询字符串的形式,发送到服务器的参数

```js
app.get('/', (req, res) => {
    //默认对象为空{};客户端使用?name=lesen&age=18 发送到服务器参数
  console.log(req.query)
})
```

- 通过`req.paramas`对象,可以访问到URL中,通过:匹配到的动态参数

```js
app.get('/:name/:id', (req, res) => {
  console.log(req.params)
  res.send(req.params)
})
//链接地址http://127.0.0.1:3000/lesen/3
显示{"name":"lesen","id":"3"}
```

### 4.托管静态资源

1. express.static()
    >可以创建一个静态资源服务器,将public目录下的picture,css,JavaScript文件对外开放

    ```js
    app.use(express.static('public'))
    //现在可以访问public目录中的所有文件了:
    http://localhost:3000/images/index.jpg
    http://localhost:3000/css/index.jpg
    http://localhost:3000/js/index.jpg
    ```

2. 托管多个静态资源目录,多次调用express.static()
3. 挂载路径前缀

   ```js
   app.use('/user', express.static('./public'))
   ```

### 5.路由

#### 5.1路由的概念

在express中,路由就是客户端的请求与服务器处理函数之间的映射关系

express中的路由分3部分组成

1. 请求的类型
2. 请求的url地址
3. 处理函数

```js
app.METHOD(PATH,HANDLER)
```

#### 5.2路由的使用

为了方便对路由进行模块化管理,express不建议将路由直接挂载到app上,推荐将路由抽离为单独的模块

1. 创建路由模块对应的.js文件
2. 调用`express.Router()`函数创建路由对象
3. 向路由对象上挂载具体的路由
4. 使用`module.exports`向外共享路由对象
5. 使用`app.use()`函数注册路由模块

```js
//新建router.js创建路由模块,并且module.exports共享
const express = require('express')
const router = express.Router()
router.get('/user/list', function(req.res) {
    res.send('Get user list')
})
router.get('/user/add', function(req,res) {
    res.send('Add new user')
})
module.exports = router
```

注册路由模块

```js
//在app.js中导入
const router = require('./router')
app.use(router)
```

### express中间件

中间件函数的形参中必须包含next参数

```js
app.get('/', function(req,res,next) {
    next();
})
```
