# Working with Arrays

在现代的js用法中升级了arrays的使用

### Simple array methods

```js
let arr = ['a', 'b', 'c', 'd', 'e'];
//slice 切片,不改变原数组
console.log(arr.slice(2));
console.log(arr.slice(-2));
console.log(arr);
//splice 拼接,改变原数组
console.log(arr.splice(-1));
console.log(arr); $ ['a', 'b', 'c', 'd']
arr.splice(1, 2);
console.log(arr); $ ['a', 'd']
//reverse 逆转,改变原数组
arr = ['a', 'b', 'c', 'd', 'e'];
let arr2 = ['f', 'g', 'h', 'i', 'j'];
console.log(arr2.reverse());
console.log(arr2);
//concat 拼接
const letters = arr.concat(arr2);
console.log(letters);
console.log([...arr, ...arr2]); //也可以使用扩展数组方式
//join
console.log(letters.join(' - '));
```

push,shift,pop,index of等用法同理

### Array at method

```js
let arr = [11, 22, 33];
console.log(arr[0]);
console.log(arr.at(0));

//getting last array element
console.log(arr[arr.length - 1]);
console.log(...arr.slice(-1));
console.log(arr.slice(-1)[0]);

console.log(arr.at(-1));

```

### forEach method

```js
const movements = [200, 450, -400, 3000, -650, -130, 70, 1300];
//for of loop
for (const [i, movement] of movements.entries()) {
  if (movement > 0) {
    console.log(`Movement ${i + 1}: You deposited ${movement}`);
  } else {
    console.log(`Movement ${i + 1}: You withdrew ${Math.abs(movement)}`);
  }
}
//forEach 回调函数的参数顺序不同(数值,索引,数组)
movements.forEach(function (movement, index, array) {
  if (movement > 0) {
    console.log(`Movement ${index + 1}: You deposited ${movement}`);
  } else {
    console.log(`Movement ${index + 1}: You withdrew ${Math.abs(movement)}`);
  }
});
```

### forEach with Map and Set

```js
const currencies = new Map([
  ['USD', 'United States dollar'],
  ['EUR', 'Euro'],
  ['GBP', 'Pound sterling'],
]);

currencies.forEach(function (value, key, map) {
  console.log(`${key}: ${value}`);
});

const currenciesUnique = new Set(['USD', 'GBP', 'EUR', 'USD', 'EUR']);
currenciesUnique.forEach(function (value, key, set) {
  console.log(`${key}, ${value}`);
});
```

