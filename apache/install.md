# Ubuntu下安装和配置apache2并启用https

## 摘要

### 第一部分：安装并测试apache2

步骤一：安装apache2  
```sh
sudo apt install apache2
```
步骤二：在防火墙中放行80端口
通过ufw放行用于测试默认网站的80端口：
```sh
sudo ufw allow 80
firewall-cmd --zone=public --add-port=443/tcp --permanent
firewall-cmd --reload #重启生效
```
步骤三：测试默认网站   
在浏览器中输入网址<http://127.0.0.1>，正常情况下将会打开类似的页面：
![apache2.html](/apache2/apache2.png)

### 第二部分：在Ubuntu下配置apache2

在用一个示例网站配置之前，我们先了解一下apache2安装目录“/etc/apache2/”的文件结构：
```sh
/etc/apache2/
├── apache2.conf    # 主配置文件，通常很少修改。
├── conf-available
├── conf-enabled
├── envvars # Apache2的环境变量，通常很少修改。
├── magic
├── mods-available  # 已安装的apache2模块，非启用的模块。
├── mods-enabled    # 已启用的模块。
├── ports.conf  # 所有监听的端口配置。
├── sites-available # 所有的虚拟主机配置文件。
└── sites-enabled   # 所有正在运行的虚拟主机配置文件。
```
我们现在以通过虚拟主机部署一个网站为例，介绍如何使用apache2。  
假设已经有一个服务部署在了9264端口，我们想通过网址<http://service.example.com>访问这个服务（域名<http://service.example.com>已经通过A记录解析到ubuntu服务器上）。  
为此，我们新建一个.conf的虚拟主机配置文件

步骤一：新建配置文件  
在`/etc/apache2/sites-available/`目录下新建一个配置文件`service.conf`
```sh
cd /etc/apache2/sites-available/
sudo vim service.conf
```
步骤二：编辑配置文件  
将如下配置添加到文件中：
```sh
<VirtualHost _default_:80>
    Servername service.example.com
    ProxyPass / http://localhost:9264/
    ProxyPassReverse / http://localhost:9264/
    ProxyPreserveHost On
</VirtualHost>
```
保存文件并退出文件。  

步骤三：启用网站并重新加载apache2  
通过如下命令启用网站：
```sh
sudo a2ensite service.conf
sudo systemctl reload apache2
```
步骤四：启用ssl模块并重启apache2  
我们可以启用https（默认在443端口）提高访问服务的安全性，首先启用apache2的ssl模块：
```sh
sudo a2enmod ssl
sudo systemctl restart apache2
```
检查“/etc/apache2/ports.conf”文件中443端口是否启用监听，默认情况下443端口是监听的。如果未监听，加入“Listen 443 https”并重新加载apache2。

步骤五：启用虚拟主机https监听  
在启用虚拟主机的https前，先保证有一个对应域名的SSL证书。免费的SSL证书可以通过Let’s Encrypt申请
```sh
<VirtualHost _default_:443> 
    Servername service.example.com
    SSLEngine on 
    SSLCertificateFile /path/to/certificate/file
    SSLCertificateKeyFile /path/to/certificate/key/file
    ProxyPass / http://localhost:9264/
    ProxyPassReverse / http://localhost:9264/ 
    ProxyPreserveHost On
</VirtualHost>
```
步骤六：在防火墙中放行443端口
```sh
sudo ufw allow 443
```
现在我们可以通过网址<https://service.example.com>访问服务

### 第三部分：常用命令

切换服务状态
```sh
sudo systemctl start apache2
sudo systemctl stop apache2	
sudo systemctl reload apache2
sudo systemctl restart apache2
#启用/禁用虚拟主机配置
sudo a2ensite <.conf file>
sudo a2dissite <.conf file>
#启用/禁用apache2模块
sudo a2enmod <module name>
sudo a2dismod <module name>
```