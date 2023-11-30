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

### 遇到的问题

更换python安装目录后,需要更新pip文件

1. 到PyIP网站下载适合版本的pip版本
2. 解压出来pip和pip-*.info
3. 把这两个目录copy到 \python38\Lib\site-packages

升级pip
`python -m pip install --upgrade pip`
