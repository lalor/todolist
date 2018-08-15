# 使用说明

在MySQL中导入数据库:

    mysql -h127.0.0.1 -ulaimingxing -plaimingxing -Dtest -P3306 < schema.sql

修改app.py，配置访问数据库的用户名、密码和端口号。

# TODO

* 分离配置文件secret.py
* 密码加密
* 用户注册
* 以用户为维度，管理TodoList
