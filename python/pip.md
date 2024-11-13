### PIP

#### install pip

```bash
sudo apt install python3-pip
```

#### pip install package

直接使用pip install 会导致一个问题`error: externally-managed-environment`
解决办法有三种

**pipx**
pipx适合安装application

```bash
apt install pipx
pipx install some-python-application
```

**venv**
需要导入库的情况下使用, 创建一个虚拟环境

```bash
python -m venv my-venv
my-venv/bin/pip install some-python-library
```

**--break-system-packages**
强制安装, 但是有破坏系统风险

- 在命令后加上`--break-system-packages`
- 把如下命令加到`~/.config/pip/pip.conf`

  ```bash
  [global]
  break-system-packages = true
  ```
- 使用pip的`config`命令

  ```bash
  python3 -m pip config set global.break-system-packages true
  ```

  

