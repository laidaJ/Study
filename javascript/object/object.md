# 对象

- 对象(object):JavaScript的一种数据类型

- 可以理解为是一种无序的数据集合,注意数组是有序的数据集合
- 用来描述某个事物,例如描述一个人

## 对象的使用

```js
let 对象名 = {
    属性名:属性值,
    方法名:函数
}
//对象由属性和方法组成
```

### 增删改查

语法:对象名.属性

```js
let person = {
    uname: 'lesen',
    age: 18,
    gender: 'male'
}
//查
console.log(person.uname)
$ lesen
console.log(person.age)
$ 18
console.log(person.gender)
$ male
//标准的查
console.log(person['uname'])
//改
person.age = 20
console.log(person.age)
$ 20
//增
person.hobby = 'baskteball'
```

### 对象的方法

```js
let person = {
    uname: 'lesen',
    sum: (x, y) => {
        console.log(x + y)
    }
}
person.sum(1, 2)
```

### 遍历对象

```js
let person = {
    uname: 'lesen',
    age: 18,
    gender: 'male'
}
for (let k in person) {
    console.log(person.uname)
    console.log(person[k])//k的值是'uname', 'age', 'gender'
}
```

## 内置对象

Math

```js
//属性
console.log(Math.PI)
//方法
//ceil 向上取整
console.log(Math.ceil(1.1))	$ 2
//floor 乡下取整
console.log(Math.floor(1.1)) $ 1
//round 四舍五入
console.log(Math.roud(1.5))	$ 2
```

###  随机数

`Math.random()`是[0-1)的数

```js
//0-10的整数
Math.floor(Math.random()*(10+1))
//n-m的随机数
Math.floor(Math.random()*(m - n + 1)) + n
//在数组中随机取
let arr = ['red', 'pink', 'green']
let random = Math.floor(Math.random()*arr.length)
console.log(arr[random])
```









