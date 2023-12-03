# Nextcloud基础教程

## 刷新

有时候文件太多,从网页上一个个上传太麻烦,用scp传文件后网页上并没有更新;需要手动刷新

```sh
cd /var/www/nextcloud #cd到安装nextcloud的文件根目录下
sudo -u www-data php occ files:scan --all
```
会显示如下信息:

```sh
Starting scan for user 1 out of 3 (admin)
Starting scan for user 2 out of 3 (nicen)
Starting scan for user 3 out of 3 (yefei)
+---------+-------+-----+---------+---------+--------+--------------+
| Folders | Files | New | Updated | Removed | Errors | Elapsed time |
+---------+-------+-----+---------+---------+--------+--------------+
| 1213    | 3888  | 0   | 3219    | 13      | 0      | 00:00:46     |
+---------+-------+-----+---------+---------+--------+--------------+
```

再进入网页后就可以看到更新拉

### 指定用户扫描

先查看有哪些用户

```sh
sudo -u www-data php occ user:list
sudo -u www-data php occ files:scan admin
```

### 指定路径扫描

```sh
sudo -u www-data php occ files:scan --path="/admin/files/work"
```
