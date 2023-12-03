# MySQL 数据库备份还原方法

## 备份

使用 mysqldump 命令

```sh
mysqldump -uroot -p database_name > ~/backup/2023-12-03.sql
```

## 还原

恢复的原理是恢复数据库内的操作,如果数据库整个删除drop了,需要另外新建数据库

```sh
#登录数据库
mysql -uroot -p
#创建数据库
create database database_name;
#退出数据库
exit
#还原
mysql -uroot -p database_name < ~/backup/2023-12-03.sql
```
