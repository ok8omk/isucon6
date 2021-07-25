## isuda

```
+-------------+---------------------+------+-----+---------+----------------+
| Field       | Type                | Null | Key | Default | Extra          |
+-------------+---------------------+------+-----+---------+----------------+
| id          | bigint(20) unsigned | NO   | PRI | NULL    | auto_increment |
| author_id   | bigint(20) unsigned | NO   |     | NULL    |                |
| keyword     | varchar(191)        | YES  | UNI | NULL    |                |
| description | mediumtext          | YES  |     | NULL    |                |
| updated_at  | datetime            | NO   |     | NULL    |                |
| created_at  | datetime            | NO   |     | NULL    |                |
+-------------+---------------------+------+-----+---------+----------------+

+------------+---------------------+------+-----+---------+----------------+
| Field      | Type                | Null | Key | Default | Extra          |
+------------+---------------------+------+-----+---------+----------------+
| id         | bigint(20) unsigned | NO   | PRI | NULL    | auto_increment |
| name       | varchar(191)        | YES  | UNI | NULL    |                |
| salt       | varchar(20)         | YES  |     | NULL    |                |
| password   | varchar(40)         | YES  |     | NULL    |                |
| created_at | datetime            | NO   |     | NULL    |                |
+------------+---------------------+------+-----+---------+----------------+
```

## isutar

```
+------------+---------------------+------+-----+---------+----------------+
| Field      | Type                | Null | Key | Default | Extra          |
+------------+---------------------+------+-----+---------+----------------+
| id         | bigint(20) unsigned | NO   | PRI | NULL    | auto_increment |
| keyword    | varchar(191)        | NO   |     | NULL    |                |
| user_name  | varchar(191)        | NO   |     | NULL    |                |
| created_at | datetime            | YES  |     | NULL    |                |
+------------+---------------------+------+-----+---------+----------------+
```
