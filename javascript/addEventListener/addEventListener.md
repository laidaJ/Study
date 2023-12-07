# 事件监听

## 语法

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
## 事件类型

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
- 表单输入触发
    1. input 用户输入事件

## 事件对象

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
- key 用户按下的键盘的值