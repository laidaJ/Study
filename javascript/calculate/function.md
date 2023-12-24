# function

## 函数的使用

### 使用

```js
//声明函数
function 函数名 () {
    函数体
}
//调用
函数名()
```

#### 命名规则

- 基本和变量一致
- 驼峰命名法 getNumber
- 最好开头用动词 get\can\has\set

#### 函数参数

```js
function 函数名(参数) {
    函数体
}
//数组求和
const getSum = (arr = []) => {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i]
  }
  console.log(sum)
}
getSum([1, 2, 3, 4, 5])
```

#### 函数的返回值

```js
function fn() {
    return 20 // 返回值
}
let num = fn()
console.log(num)
```

