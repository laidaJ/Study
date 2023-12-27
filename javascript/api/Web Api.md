# Web Api

## DOM

### DOM对象

DOM对象:浏览器根据html标签生成的JS对象

document对象:是DOM里提供的一个对象,所以它提供的属性和方法都是用来访问和操作页面内容的

#### 根据css选择器来获取DOM元素

```js
//获取匹配的第一个元素
const box = document.querySelector('div')
const box = document.querySelector('.box')
const nav = document.querySelector('#nav')
//获取第一个小ul li
const li = document.querySelector('ul li:first-child')
//获取所有的小li
document.querySelectorAll('css选择器')
document.querySelectorAll('ul li')
```

#### 操作元素内容

对象`.innerText`属性

对象`.innerHTML`属性:可以解析标签

```html
<body>
    <div class = box>
        我是文字的内容
    </div>
	<script>
    const box = document.querySelector('.box');
    box.innerText = '我是一个盒子'
    box.innerHTML = '<strong>我是一个盒子</strong>'
    </script>
</body>
```

```js
//抽取一等奖
const personArr = ['周杰伦', '刘德华', '周星驰', '张学友', '来小盛'];
const one = document.querySelector('#one')
const random = Math.floor(Math.random() * personArr.length)
one.innerHTML = personArr[random]
personArr.splice(random, 1)
//抽取二等奖
const two = document.querySelector('#two')
const random2 = Math.floor(Math.random() * personArr.length)
two.innerHTML = personArr[random2]
personArr.splice(random2, 1)
//抽取三等奖
const three = document.querySelector('#three')
const random3 = Math.floor(Math.random() * personArr.length)
three.innerHTML = personArr[random3]
personArr.splice(random3, 1)
```

#### 操作样式属性

通过style属性控制样式

```js
对象.style.属性 = 值
const box = document.querySelector('.box')
box.style.width = '300px'
box.style.backgroundColor = 'pink'
//修改样式通过style属性引出
//如果属性有-连接符,需要转换为小驼峰命名法
//赋值的时候,不要忘记加css单位
```

通过className属性控制样式

```js
const box = document.querySelector('.box')
box.className = 'div'
```

通过classList属性控制样式

```js
const box = document.querySelector('.box')
box.classList.add('div') //增加类
box.classList.remove('div') //删除类
box.classList.toggle('box')	//切换类
```



随机更换背景图

```css
body {
  background: url(./images/desktop_1.jpg) no-repeat top center/cover
}
```

```js
const getRandom = (n, m) => {
  return Math.floor(Math.random() * (m - n + 1) + n)
}
const random = getRandom(1, 10)
document.body.style.backgroundImage = `./images/desktop_${random}.jpg`
```

#### 操作表单元素属性

```js
const uname = document.querySelector('input')
console.log(uname.value)
uname.value = '这是表单'
uname.type = 'password'
<input type = 'checkbox'>
const ipt = document.querySelector('input')
ipt.checked = true
const btn = document.querySelector('button')
btn.disabled = true //不能点击
```

#### 自定义属性

**标准属性**:标签天生自带的属性,比如class,id,title等,可以直接使用语法操作比如:disabled,checked,selected

**自定义属性**:在html5推出了专门的data-自定义属性;标签上一律以data-开头;在DOM上一律以dataset对象方式获取

```html
<body>
    <div data-id = '1' data-spm = '1.1'>1</div>
    <div data-id = '2'>2</div>
    <div data-id = '3'>3</div>
    <div data-id = '4'>4</div>
    <div data-id = '5'>5</div>
    <script>
    const one = document.querySelector('div')
    console.log(one.dataset.id)	// 1
    console.log(one.dataset.spm)	//1.1
    </script>
</body>
```

### 定时器

```js
//匿名函数
setInterVal(函数, 间隔时间)
setInterval(() => {
  document.write('一秒一次定时器')
}, 1000)
//有名函数
const fn = () => {
  console.log('调用一次')
}
setInterval(fn, 1000) //调用函数名,不需要加()
```

关闭定时器

```js
const fn = () => {
    console.log('执行定时器')
}
let timer = setInterval(fn, 1000)
clearInterval(timer) //关闭定时器
```

定时器案例

```html
<body>
  <textarea name="" id="" cols="30" rows="10">用户注册协议</textarea>
  <button disabled>我已经阅读了用户协议(5)</button>
  <script>
    const btn = document.querySelector('button')
    let i = 5;
    let timer = setInterval(() => {
      i--;
      btn.innerHTML = `我已经阅读了用户协议(${i})`
      if (i === 0) {
        btn.innerHTML = '我已经阅读了用户协议'
        clearInterval(timer)
        btn.disabled = false
      }
    }, 1000)
  </script>
</body>
```

