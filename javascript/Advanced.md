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

###  Spread operator 扩展运算符

在数组变量前加`...`可以把数组取出来

```js
const arr = [2, 3, 4];
//常规办法
const badArr = [1, arr[0], arr[1], arr[2]];
//扩展运算符...
const goodArr = [1, ...arr];
```

合并两个数组

```js
const menu = [...restaurant.mainMenu, ...restaurant.starterMenu];
console.log(menu);
```

iterable可迭代:arrays,strings,maps,sets,NOT objects

```js
const lesen = 'Lesen';
console.log(...lesen);
const letters = [...lesen];
console.log(letters);
$ L e s e n
$ ['L', 'e', 's', 'e', 'n']
```

餐厅案例

```js
//在餐厅对象增加函数
orderPasta: (ing1, ing2, ing3) =>
    console.log(
      `Here is your delicious pasta with ${ing1}, ${ing2} and ${ing3}`
    ),

//弹窗输入3个配料    
const ingredients = [
  prompt("let's make pasta! Ingredient 1?"),
  prompt('Ingredient 2?'),
  prompt('Ingredient 3'),
];
//使用...把数组中的值解析出来
restaurant.orderPasta(...ingredients);
$ Here is your delicious pasta with Mushroom, egg and peanut
```

操作对象

```js
//提取原对象内的数据并且新增合并
const newRestaurant = { foundedIn: 1998, ...restaurant, founder: 'Huangkai' };
console.log(newRestaurant);
//这个复制是另外开辟一个内存栈
const restaurantCopy = { ...restaurant };
restaurantCopy.name = 'flychicken';
console.log(restaurant.name);
console.log(restaurantCopy.name);
$ Classico Italiano
$ flychicken
```

### Rest

左边用`...参数`来代替其余的数值;

1. 需要在最后面
2. 左边要比右边多

```js
//在等号右边的是扩展用法
const arr = [1, 2, ...[3, 4]];
//在等号左边的是Rest用法
const [a, b, ...others] = [1, 2, 3, 4, 5];
console.log(a, b, others);
$ 1 2 [3, 4, 5]
```

用rest方式处理restaurant对象

```js
const { sat, ...weekdays } = restaurant.openingHours;
console.log(weekdays);
```

### Short circuiting(&& ||)

或 ||;按顺序判断,出现第一个为真,JavaScript就不会看后面的了,显示第一个为真的值,或者显示最后一个

```js
console.log('' || 'Lesen'); $ Lesen
console.log(true || 0);		$ true
console.log(undefined || null);	$ null
//可以相当于于if判断语句使用
const guest1 = restaurant.numGuests ? restaurant.numGuests : 10;
console.log(guest1); 
const guest2 = restaurant.numGuests || 10;
console.log(guest2);
```

与 &&;按顺序判断,出现第一个为假,JavaScript就不会看后面的了,显示第一个为假的值,或者最后一个

```js
console.log(0 && 'Lesen');	$ 0
console.log(7 && 'Lesen');	$ Lesen
console.log('Hello' && 23 && null && 'lesen');	$ null
```

### Logical assignment operators逻辑赋值运算符

OR assignment operator

```js
const rest1 = {
  name: 'Capri',
  numGuests: 0,
};

const rest2 = {
  name: 'La Pizza',
  owner: 'laijun',
};

// rest1.numGuests = rest1.numGuests || 10;
// rest1.numGuests ||= 10;	//上一条的简单写法
rest1.numGuests ??= 10; //空值的赋值运算写法

// rest2.numGuests = rest2.numGuests || 10;
// rest2.numGuests ||= 10;
rest2.numGuests ??= 10;

console.log(rest1.numGuests);
console.log(rest2.numGuests);
```

AND assignment operator

```js
// rest1.owner = rest1.owner && '<Noone>';
rest1.owner &&= '<Noone>';
// rest2.owner = rest2.owner && '<Noone>';
rest2.owner &&= '<Noone>';
console.log(rest1);
console.log(rest2);
```

### for-of loop

ES6的循环语法

```js
const menu = [...restaurant.starterMenu, ...restaurant.mainMenu];
for (const item of menu) console.log(item);
```

老式办法取索引号

```js
for (const item of menu.entries()) {
  console.log(`${item[0] + 1}: ${item[1]}`); //item[0]为索引号,从0开始
}
```

结构办法取索引号

```js
for (const [i, el] of menu.entris()) {
    console.log(`${i + 1}: ${el}`);
}
```

### Enhanced object literals增强对象文字

针对对象的ES6语法

当对象的变量和引用变量名字相同时,可以直接只写变量名

```js
const openingHours = {
  thu: {
    open: 12,
    close: 22,
  }
};
const restaurant = {
  openingHours,
}
```

对象内函数可以省略`:`和`function`;

```js
const restaurant = {
  openingHours,
  orderPasta(ingredients) {
    console.log(`Here is your delicious pasta with ${ingredients}`);
  },
};
restaurant.orderPasta('peanut');
```

可以用数值索引号取值

```js
const weekdays = ['mon', 'tue', 'wed', 'thu', 'fir', 'sat', 'sun']
const openingHours = {
  [weekdays[3]]: {
    open: 12,
    close: 22,
  },
  fri: {
    open: 11,
    close: 23,
  },
  [`day-${2+4}`]: {
    open: 0, // Open 24 hours
    close: 24,
  },
};
```

### Set 集合

Set是一个可迭代对象,去重复值,值是**唯一**的;没有索引,不能取值;所以可以检查size,是否含有has,增加add,删除delete.

```js
const orders = ['Pasta',
  'Pizza',
  'Pizza',
  'Risotto',
  'Pasta',
  'Pizza'];
const ordersSet = new Set(orders);
console.log(ordersSet);
console.log(ordersSet.size);	//检查Set的种类数量
console.log(ordersSet.has('Pizza'));	//检查是否包含,返回布尔值
ordersSet.add('Garlic Bread');	//增加
ordersSet.delete('Pizza');	//删除
ordersSet.clear();	//清除

//可迭代
for (const order of ordersSet) console.log(order);
//用扩展的方式重新获取set类型的数组
const ordersUnique = [...new Set(orders)];
console.log(ordersUnique);
```

### Maps 地图

### Callback function 回调函数

**callback function 是编程中非常重要的**可以让代码更清晰,逻辑分明

```js
const upperFirstWord = function (str) {
  const [first, ...others] = str.split(' ');
  return [first.toUpperCase(), ...others].join(' ');
};
```

Higher-order function

```js
const transformer = function (str, fn) {
  console.log(`Original string: ${str}`);
  console.log(`Transformerd string: ${fn(str)}`);
  console.log(`Transformered by: ${fn.name}`);
};

transformer('This is a test text', upperFirstWord);
transformer('Make text in one word', oneWord);
```

The call methods

调用对象里面的函数只能使用call用法

```js
// lufthansa,eurowings都是对象
const book = lufthansa.book;
book.call(eurowings, 40, 'Huangkai');
// 可以把调用值存储到数组中
const flightData = [238, 'Guanzhon'];
book.call(eurowings, ...flightData);
```

The bind methods

call函数是直接调用,bind可以设置函数不调用.

```js
const bookEW = book.bind(eurowings);
bookEW(200, 'Guanzhon');
//可以预设参数
const bookEW23 = book.bind(erowings, 23);
bookEW23('Lesen');
```

