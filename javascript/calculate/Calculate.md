# Calculate

# 运算符

- 赋值运算符
- 比较运算符
- 一元运算符
- 逻辑运算符
- 运算符优先级

### 赋值运算符

```js
let num = 10 #只能给变量赋值
num += 1	# 等于 num = num + 1
```

### 一元运算符

```js
let i = 1;
console.log(++1)	#2
let i = 1;
console.log(i++)	#2
```

### 比较运算符

```js
let i = 10
console.log(i < 11);	# true
console.log(i > 11);	# false
```

### 逻辑运算符

| 符号 | 名称   | 日常读法 | 特点                                   | 口诀          |
| ---- | ------ | -------- | -------------------------------------- | ------------- |
| &&   | 逻辑与 | 并且     | 符号两边都为true<br />结果才为true     | 一假则假      |
| \|\| | 逻辑或 | 或者     | 符号两边有一个为true<br />结果就为true | 一真则真      |
| !    | 逻辑非 | 取反     | true变为false<br />false变为true       | 真变假,假变真 |

### 运算符优先级

| 优先级 | 运算符     | 顺序          |
| ------ | ---------- | ------------- |
| 1      | 小括号     | ()            |
| 2      | 一元运算符 | ++ -- !       |
| 3      | 算术运算符 | 先*/%后+-     |
| 4      | 关系运算符 | > >= < <=     |
| 5      | 相等运算符 | == != === !== |
| 6      | 逻辑运算符 | 先&& 后\|\|   |
| 7      | 赋值运算符 | =             |
| 8      | 逗号运算符 | ,             |

## 语句

表达式是可以被求值的代码,语句是一段可以执行的代码

### 分支语句

三种使用:单分支,双分支,多分支

#### if分支语句

```js
if (true) {
	console.log('This is true')
}
---------------
if (true) {
	console.log('This is true')
} else {
	console.log('This is false')
}
--------------
if (条件) {
	执行1
} else if (条件) {
	执行2
} else {
	执行3
}
```

#### 三元运算符

比if双分支更简单的写法, `?`和`:`配合使用

```js
let num1 = +prompt('输入第一个数');
let num2 = +prompt('输入第二个数');
num1 > num2 ? alert(`最大的数是${num1}`) : alert(`最大的数是${num2}`)
```

#### switch语句

```js
let num1 = +prompt('num1');
let cal = prompt('cal');
let num2 = +prompt('num2');
switch (cal) {
  case '+':
    alert(`${num1} + ${num2} 的结果是 ${num1 + num2}`)
    break;
  case '-':
    alert(`${num1} - ${num2} 的结果是 ${num1 - num2}`)
    break;
  case '*':
    alert(`${num1} * ${num2} 的结果是 ${num1 * num2}`)
    break;
  case '/':
    alert(`${num1} / ${num2} 的结果是 ${num1 / num2}`)
    break;
}
```

#### 循环语句

```js
let result = prompt('Do you love me?');
    while (result) {
      if (result === 'yes') {
        alert('I love you too');
        break; # break是退出循环,continue是略过循环
      }
    }
```

#### 取款机案例

```js
let result = 0;
    while (true) {
      const doWhat = +prompt(`请输入操作:
      1.存钱
      2.取钱
      3.查看余额
      4.退出`)
      if (doWhat === 4) {
        break
      }
      switch (doWhat) {
        case 1:
          let putIn = +prompt('请输入存款金额');
          result += putIn;
          break;
        case 2:
          let takeOut = +prompt('请输入取款金额');
          if (result < takeOut) {
            alert('您的余额不足')
            break;
          }
          result -= takeOut;
          break;
        case 3:
          alert(`您的余额为${result}`)
          break;
      }
    }
```

### 循环

#### for循环语句

```js
for (起始值; 结束条件; 变量变化量) {
	#循环体
}
```

#### 案例

```js
# 打印1-100岁
for (let age = 1; age <= 100; age++) {
	document.write(`我今年${age}岁了<br>`)
}
# 1-100偶数的和
let sum = 0;
for (let num = 1; num <= 100; num++) {
	if(num % 2 === 0) {
		sum += num
	}
}
document.write(`1-100偶数的和是${sum}`)
# 打印5个五角星
for (let i = 0; i < 5; i++) {
  document.write('☆')
}
# 打印数组
const arr = ['马超', '张飞', '关羽', '黄忠', '赵云'];
for (let i = 0; i < arr.length; i++) {
  document.write(`${arr[i]}<br>`)
}
# 99乘法表
for (let i = 1; i <= 9; i++) {
  for (let j = 1; j <= i; j++) {
    let result = i * j;
    if (result < 10) {
      result = '&nbsp&nbsp' + result
    }
    document.write(`<span>${j}×${i}=${result}</span>`)
  }
  document.write('<br>')
}
```

### 数组

Array是一种可以按顺序保存数据的数据类型

- 声明数值

  - `let 数组名 = [值1, 值2, 值3, ......]`
  - `let arr = new Array(1, 2, 3, 4)`

- 取值语法

  - 数组名[下标]

- 遍历数组

  - 语法

    ```js
    for (i = 0, i < 数组名.length, i++) {
    	数组名[i]
    }
    ```

- 案例

  ```js
  for (let i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
          max = arr[i]
        }
        if (arr[i] < min) {
          min = arr[i]
        }
      }
      document.write(`最大值是${max}`)
      document.write(`最小值是${min}`)
  ```

- 操作数组

| 查数组              | 改数组      | 增数组                                                       | 删数组                                                       |
| ------------------- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| console.log(arr[i]) | arr[i] = 10 | arr.push('str') #在后面增加<br />arr.unshift('str') #在前面增加 | arr.pop() #删除最后<br />arr.shift() #删除最开头<br />arr.splice(start, deleteCount) |

#### 数组筛选

```js
let arr = [2, 0, 6, 1, 77, 0, 52, 0, 25, 7];
// 声明新的数组
let newArr = [];
// 遍历旧的数组
for (let i = 0; i < arr.length; i++) {
  if (arr[i] >= 10) {
      // 满足条件 追加给新数组
    newArr.push(arr[i])
  }
}
// 输出新的数组
document.write(newArr)
```

#### 冒泡排序(了解即可)

```js
let arr = [5, 4, 3, 2, 1];
for (let i = 0; i < arr.length - 1; i++) {
  for (let j = 0; j < arr.length - i - 1; j++) {
    if (arr[j] > arr[j + 1]) {
      let tep = arr[j + 1];
      arr[j + 1] = arr[j]
      arr[j] = tep;
    }
  }
}
console.log(arr)
```

实际开发中

`arr.sort()`

