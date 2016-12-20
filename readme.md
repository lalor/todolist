在MySQL中导入数据库:

    mysql -h127.0.0.1 -ulaimingxing -plaimingxing -Dtest -P3306 < schema.sql
    insert into todolist(id, user_id, title, status, create_time) values(1, 1, '习近平五谈稳中求进 织密扎牢民生保障网', 'yes', 1482214350), (2, 1, '特朗普获超270张选举人票将入主白 宫', 'yes', 1482214350);
