# python的基础

## pip

pip 是一个现代的，通用的 Python 包管理工具。提供了对 Python 包的查找、下载、安装、卸载的功能。

在正式安装pip之前，可在控制台输入以下命令，用于检测当前Windows环境中是否已经安装pip。

```sh
python -m pip --version
```

### 安装

官网下载

1. 在Python官网上下载pip安装包
2. 压缩包解压
3. cd到解压后文件夹
4. 控制台输入 `python setup.py install`
5. 配置环境变量(可选),文件在python\script内

命令行安装

1. 访问<https://link.zhihu.com/?target=https%3A//bootstrap.pypa.io/get-pip.py>,保存文件
2. 打开命令行输入`python get-pip.py`

### 更新pip

更换python安装目录后,需要更新pip文件

1. 到PyIP网站下载适合版本的pip版本
2. 解压出来pip和pip-*.info
3. 把这两个目录copy到 \python38\Lib\site-packages

升级pip
`python -m pip install --upgrade pip`

### 使用pip更新所有的包

查看所有可以升级的包

```bash
pip list --outdated
```

借用第三方库`pip-review`,如果未安装需要先安装

```bash
pip install pip-review
```

升级所有的包

```bash
pip-review --local --interactive
```

### Print

```python
print("Hello pyhton")
```

### Input

```python
input("What is your name?")
```

### Variables

```python
name = input("What is your name?")
print(name)
```

### Data types

- String

  print("Hello")

- Interger

  print(123)

- Float

  print(3.1415926)

- Boolean

  True/False



### Mathmatical Operations(数学运算)

PEMDAS

Parentheses括号 ()

Exponents指数 **

Multiplication乘法 *

Division除法 /

Addition加法 +

Subtraction减法 -

```python
PEMDAS
#先括号内，乘方，乘除，加减
()
**
* /
+ -
```

### F-string

格式化字符串，f"{}",f加双引号，中括号内放变量

```python
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
```

### if and else

```python
if condition:
    do this
else:
    do this
```

Nested if/elif/else

```python
if condition:
    if another condition:
        do this
    elif another condition:
        do this
    else:
        do this
else:
    do this
```

multiple if

```python
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C
#三个条件都满足，三个都执行
```

### Random module

```python
import random
random_interger = random.randint(1, 10)
print(random_interger)
random_float = round(random.random() * x, y) #random()随机生成一个0~1的小数，*x，便是随机生成0~x的小数, round()四舍五入, y为小数点后几位
print(random_float)
```



### Logical Operatoers

and/or/not

and: A True and B True, result True

or: A False or B False, result False

not: not A True, result False

### List

fruits = [item1,  item2， item3, ......]

### Loops

- For loop

  for item in list_of_items:

  #Do somthing to each item

- range

  ```python
  total = 0
  
  for num in range(1, 101): #range范围从1到100
  
  	total += num
  
  print(total)
  ```

### Defining Functions

def my_function():

​	#Do this

​	#Then do this

my_function()

### While Loops

while somthing_is_true:

​	#Do something repeatedly

practice python on <https://reeborg.ca/reeborg.html>

### Functions with Inputs

def my_function(something):

​	#Do this with something

my_function(123)

def my_function(name, location):

​	#Do this with something

my_function("Lesen", "LongYou")

### Dictionaries

dictionary = {key: value}

```python
dictionary = {
    "bug": "An error in a program that prevents the program from running as expected.", #use , between keys
    "function": "A piece of code that you can easily call over and over again.",
    1: "A number",
}

#Retrieving items from dictionary
print(dictionary["bug"])

#Adding new items to dictionary
dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
dictionary = {}

#Edit an item in a dictionary
dictionary["bug"] = "a moth in your computer"

#Loop through dictionary
for item in dirctionay:
    print(item)
```

### Nesting

[{

key: [list],

key2: {dictionary},

},

{

key3: [list],

key4: value

}]
