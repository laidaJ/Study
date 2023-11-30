# 遇到的问题汇总

## 数据库备份与还原

```sh
# 备份
mysqldump -uroot -p nextcloud > /home/mysqldata/2023-11-21_13-51.sql
# 还原
mysql -uroot -p nextcloud <  /home/mysqldata/2023-11-21_13-51.sql
```
