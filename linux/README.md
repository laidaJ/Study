# 如何使用linux

## 命令

解压
- tar解压  
  - c: 建立压缩档案
  - x：解压
  - t：查看内容
  - r：向压缩归档文件末尾追加文件
  - u：更新原压缩包中的文件  
    这五个是独立的命令，压缩解压都要用到一个，可以和别的命令连用但只能用其中一个

  - z：有gzip属性的
  - j：有bz2属性的
  - Z：有compress属性的
  - v：显示所有过程
  - O：将文件解开到标准输出

  下面的参数-f是必须的  
  -f: 使用档案名字，切记，这个参数是最后一个参数，后面只能接档案名。

    ```sh
    tar -zxvf abc.tar.bz2 解压
    tar -zcvf abc.tar.bz2 abc.txt 压缩
    ```

- 解压tar.xz包  
    文件是node-v8.11.1-linux-x64.tar.xz，这是两层压缩，外面是xz压缩，里层   是tar压缩，所以分两步实现解压。

    ```sh
    xz -d node-v8.11.1-linux-x64.tar.xz
    tar -xvf node-v8.11.1-linux-x64.tar.xz
    ```

    也可以直接解压
    ```
    tar -xvJf node-v8.11.1-linux-x64.tar.xz
    ```

```sh
    ar -xvf file.tar       #解压 tar包
    tar -xzvf file.tar.gz    #解压tar.gz   
    tar -xjvf file.tar.bz2   #解压 tar.bz2
    tar -xZvf file.tar.Z   #解压tar.Z 
    unrar e file.rar   #解压rar 
    unzip file.zip     #解压zip 
    unzip -oq common.war -d common#解压war包并制定存储目录    
    jar -xvf game.war         #解压war包并存储在当前目录下
    rar x test.rar     #解压rar包
```

***  
压缩tar包   
创建xxx.tar文件  
`tar -cvf xxx.tar xxx`  
压缩tar.xz包    
先创建xxx.tar文件   
`tar -cvf xxx.tar xxx`  
再创建xxx.tar.xz文件    
`xz -z xxx.tar`  
如果要保留被压缩的文件，需要加上参数-k  
压缩war包   
`jar -cvfM0 game.war ./      //把当前目录下的所有文件打包成game.war`    
压缩zip包   
`zip -r test.zip ./*      //将当前目录下的所有文件和文件夹全部压缩成    test.zip文件,-r表示递归压缩子目录下所有文件`  
压缩rar包   
#压缩/test/下的文件为 test.rar  
`rar test.rar ./test/`  

- 7z解压

    ```sh
    apt install p7zip 安装软件
    7z x filename.7z  解压
    ```

下载

- git下载  
    下载的地址为当前目录
    ```
    git clone https://xxx-xxx-xxx.com
    ```

## 配置环境变量

Linux读取环境变量  
读取环境变量的方法：

`export` 命令显示当前系统定义的所有环境变量  
`echo $PATH` 命令输出当前的PATH环境变量的值  
这两个命令执行的效果如下

```sh
lesen@ubuntu:~$ export
declare -x CLUTTER_IM_MODULE="fcitx"
declare -x COLORTERM="truecolor"
declare -x DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
declare -x DEBUGINFOD_URLS="https://debuginfod.ubuntu.com "
declare -x DESKTOP_SESSION="ubuntu"

lesen@ubuntu:~$ echo $PATH
/home/lesen/vulkan/1.x.yy.z/x86_64/bin:
/home/lesen/anaconda3/bin:
/home/lesen/.local/bin:
```

其中PATH变量定义了运行命令的查找路径，以冒号:分割不同的路径，使用`export`定义的时候可加双引号也可不加。

### Linux环境变量配置方法一：`export PATH`

使用export命令直接修改PATH的值，配置MySQL进入环境变量的方法:

```sh
export PATH=/home/uusama/mysql/bin:$PATH
#或者把PATH放在前面
export PATH=$PATH:/home/uusama/mysql/bin
```

注意事项：
- 生效时间：立即生效
- 生效期限：当前终端有效，窗口关闭后无效
- 生效范围：仅对当前用户有效
- 配置的环境变量中不要忘了加上原来的配置，即`$PATH`部分，避免覆盖原来配置

### Linux环境变量配置方法二：`vim ~/.bashrc`

通过修改用户目录下的 `~/.bashrc` 文件进行配置：

```sh
vim ~/.bashrc
#在最后一行加上
export PATH=$PATH:/home/lesen/mysql/bin
```

注意事项：
- 生效时间：使用相同的用户打开新的终端时生效，或者手动source ~/.bashrc生效
- 生效期限：永久有效
- 生效范围：仅对当前用户有效
- 如果有后续的环境变量加载文件覆盖了PATH定义，则可能不生效


### Linux环境变量配置方法三：`vim ~/.bash_profile`

和修改`~/.bashrc`文件类似，也是要在文件最后加上新的路径即可：

```sh
vim ~/.bash_profile
# 在最后一行加上
export PATH=$PATH:/home/uusama/mysql/bin
```

注意事项：

- 生效时间：使用相同的用户打开新的终端时生效，<br>或者手动`source ~/.bash_profile`生效
- 生效期限：永久有效
- 生效范围：仅对当前用户有效
- 如果没有`~/.bash_profile`文件，则可以编辑`~/.profile`文件或者新建一个

### Linux环境变量配置方法四：`vim /etc/bashrc`

该方法是修改系统配置，需要管理员权限（如root）或者对该文件的写入权限：

```sh
# 如果/etc/bashrc文件不可编辑，需要修改为可编辑
chmod -v u+w /etc/bashrc
vim /etc/bashrc
# 在最后一行加上
export PATH=$PATH:/home/uusama/mysql/bin
```

注意事项：
- 生效时间：新开终端生效，或者手动source /etc/bashrc生效
- 生效期限：永久有效
- 生效范围：对所有用户有效

### Linux环境变量配置方法五：`vim /etc/profile`

该方法修改系统配置，需要管理员权限或者对该文件的写入权限，和vim /etc/bashrc类似：

```sh
# 如果/etc/profile文件不可编辑，需要修改为可编辑
chmod -v u+w /etc/profile
vim /etc/profile
# 在最后一行加上
export PATH=$PATH:/home/uusama/mysql/bin
```

注意事项：
- 生效时间：新开终端生效，或者手动source /etc/profile生效
- 生效期限：永久有效
- 生效范围：对所有用户有效


### Linux环境变量配置方法六：`vim /etc/environment`

该方法是修改系统环境配置文件，需要管理员权限或者对该文件的写入权限：

```sh
# 如果/etc/bashrc文件不可编辑，需要修改为可编辑
chmod -v u+w /etc/environment
vim /etc/profile
# 在最后一行加上
export PATH=$PATH:/home/uusama/mysql/bin
```

注意事项：
- 生效时间：新开终端生效，或者手动source /etc/environment生效
- 生效期限：永久有效
- 生效范围：对所有用户有效

### ln

```sh
ln -s ~/file /usr/local/bin/file
```

不同文件夹下的软连接需要使用绝对路径,不然会显示红色不可执行
