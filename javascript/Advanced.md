# JavaScript Advanced

### Web Api

DOM对象

DOM对象:浏览器根据html标签生成的JS对象

document对象:是DOM里提供的一个对象,所以它提供的属性和方法都是用来访问和操作页面内容的

根据css选择器来获取DOM元素

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

操作元素内容

对象`.textContent`属性

对象`.innerText`属性

对象`.innerHTML`属性:可以解析标签

```html
<body>
    <div class = box>
        我是文字的内容
    </div>
	<script>
    const box = document.querySelector('.box');
    box.textContent = '我是一个盒子'
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

操作样式属性

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

操作表单元素属性

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

自定义属性

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

定时器

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

### 事件监听

语法

1. 什么是事件监听

   > 让程序检测是否有事件产生,一旦有事件触发,就立即调用一个函数做出响应

2. 事件监听三要素

   >- 事件源(谁被触发了)
   >- 事件类型(触发条件是什么)
   >- 事件处理程序(要做什么事情)

```js
const btn = document.querySlector('button')
btn.addEventListener('click', function(){
    alert('hello')
})
```

事件类型

- 鼠标触发

  1. click 鼠标点击
  2. mouseenter 鼠标经过
  3. mouseleave 鼠标离开

- 焦点事件

  1. focus 获得焦点
  2. blur 失去焦点

- 键盘触发

  1. keydown 键盘按下

  2. keyup 键盘抬起

  3. keypress 键盘按下

     ```js
     document.addEventListener('keydown', function (e) {
         console.log(e.key);// 获取按下的键盘是哪个
     })
     ```

     

- 表单输入触发

  1. input 用户输入事件

事件对象

回调函数的第一个参数就是事件对象

```js
const btn = document.querySelector('button')
btn.addEventListener('click', function(e){
    console.log(e) // e 就是事件对象
})
```

部分常用属性

- type 事件类型
- clientx/clientY 光标对于浏览器可见窗口左上角的位置
- offsetX/offsetY 对于当前DOM元素左上角的位置
- key 用户按下的键盘的值# Working with JSON

JavaScript Object Notation (JSON)JS对象注释

- 先决条件:基础计算机知识,了解一点html和css,熟悉JavaScript
- 目的:了解如何使用存储在JSON中的数据,并且创建你自己的JSON字符串

### Destructuring Arrays 解构数组

解构数组有点像解压压缩包,可以数组 = 数组的形式,对应的取值

```js
const arr = [1, 2, 3];
const [a, b, c] = arr;
console.log(a, b, c);
$ 1 2 3
```

用`空格`可以跳过不想取的数值

```js
const arr = [1, 2, 3];
const [a, , c] = arr;
console.log(a, c);
$ 1 3
```

不需要temp来临时存储,可以直接交换两个值

```js
const arr = [1, 2, 3];
let [a, b] = arr;
[b, a] = [a, b];
console.log(a, b);
$ 2 1
```

对象内的函数也可以解构

```js
const restaurant = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],

  order: function (startIndex, mainIndex) {
    return [this.starterMenu[startIndex], this.mainMenu[mainIndex]];
  }
};
const [starter, main] = restaurant.order(2, 0);
console.log(starter, main);
$ Garlic Bread Pizza
```

数组内的数组

```js
const arr = [1, 2, [3, 4]];
const [a, b, [c, d]] = arr;
console.log(a, b, c, d);
$ 1 2 3 4
```

设置默认值

```js
const arr = [1, 2, 3];
const [a = 1, b = 1, c = 1, d = 1] = arr;
console.log(a, b, c, d);
$ 1 2 3 1
```

### Desctructuring Objects 解构对象

解构对象与解构数组原理一样,只是解构对象需要对应准确的参数

```js
const restaurant = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],

  order: function (startIndex, mainIndex) {
    return [this.starterMenu[startIndex], this.mainMenu[mainIndex]];
  },

  openingHours: {
    thu: {
      open: 12,
      close: 22,
    },
    fri: {
      open: 11,
      close: 23,
    },
    sat: {
      open: 0, // Open 24 hours
      close: 24,
    },
  },
};
```

解构对象

```js
const { name, categories, openingHours } = restaurant;
console.log(name, categories, openingHours);
```

重新命名

```js
const {
  name: restaurantName,
  categories: tags,
  openingHours: open,
} = restaurant;
console.log(restaurantName, tags, open);
```

设置默认值

```js
const { name: restaurantName = [], menu = [] } = restaurant;
console.log(restaurantName, menu);
```

内嵌对象取值

```js
const {
  fri: { open, close },
} = restaurant.openingHours;
console.log(open, close);
const {
  fri: { open: o, close: c },
} = restaurant.openingHours;
console.log(o, c);
```

更改数值

```js
let a = 111;
let b = 999;
const obj = { a: 1, b: 2, c: 3 };
({ a, b } = obj);
console.log(a, b);
$ 1 2
```

