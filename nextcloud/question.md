# 安装nextcloud遇到的问题汇总

## 授权问题

`2023-11-20`

网页登录显示空白，只有nextcloud背景，app登录显示需要授权

1. 查询apache2的日志文件

    ```sh
    vim /var/log/apache2/err.log
    # 日志中找到下面这段两段话
    Unable to create file /var/www/nextcloud/config/config.php because Permission denied at /var/www/nextcloud/lib/private/Config.php
    
    fopen(/var/www/nextcloud/data/nextcloud.log): Failed to open stream: No such file or directory at /var/www/nextcloud/lib/private/Log/File.php
    ```

2.
