# Task 3

- 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

```sql
INSERT INTO member (id, name, username, password, follower_count, time) VALUES(1, 'Ross', 'test', 'test', 10, '2023-08-01 17:44:00');
INSERT INTO member (id, name, username, password, follower_count, time) VALUES(2, 'Rachel', 'rachel01', 'rachel02', 20, '2023-07-31 16:13:00');
INSERT INTO member (id, name, username, password, follower_count, time) VALUES(3, 'Joey', 'joey01', 'joey02', 30, '2023-07-30 15:30:00');
INSERT INTO member (id, name, username, password, follower_count, time) VALUES(4, 'Chandler', 'chandler01', 'chandler02', 40, '2023-07-29 14:29:00');
INSERT INTO member (id, name, username, password, follower_count, time) VALUES(5, 'Monica', 'monica01', 'monica02', 50, '2023-07-28 13:06:00');
INSERT INTO member (id, name, username, password, follower_count, time) VALUES(6, 'Phoebe', 'phoebe01', 'phoebe02', 60, '2023-07-27 12:18:00');
```

![image](https://raw.githubusercontent.com/wennie-tung/wehelp/main/week5/img/Task3_1.png)


- 使用 SELECT 指令取得所有在 member 資料表中的會員資料。

```sql
SELECT * FROM member;
```

![image](https://github.com/wennie-tung/wehelp/blob/main/week5/img/Task3_2.png?raw=true)


- 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。

```sql
SELECT * FROM member ORDER BY time DESC;
```

![image](https://github.com/wennie-tung/wehelp/blob/main/week5/img/Task3_3.png?raw=true)


- 使用 SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )

```sql
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```

![image](https://github.com/wennie-tung/wehelp/blob/main/week5/img/Task3_4.png?raw=true)


- 使用 SELECT 指令取得欄位 username 是 test 的會員資料。

```sql
SELECT * FROM member WHERE username = 'test';
```

![image](https://github.com/wennie-tung/wehelp/blob/main/week5/img/Task3_5.png?raw=true)


- 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

```sql
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```

![image](https://github.com/wennie-tung/wehelp/blob/main/week5/img/Task3_6.png?raw=true)


- 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

```sql
SET SQL_SAFE_UPDATES = 0;
UPDATE member SET name = 'test2' WHERE username = 'test';
SELECT * FROM member;
```

![image](https://github.com/wennie-tung/wehelp/blob/main/week5/img/Task3_7.png?raw=true)



# Task 4 

- 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

```sql
SELECT COUNT(*) AS total_members FROM member;
```

![image](https://github.com/wennie-tung/wehelp/blob/main/week5/img/Task4_1.png?raw=true)


- 取得 member 資料表中，所有會員 follower_count 欄位的總和。

```sql
SELECT SUM(follower_count) AS total_followers FROM member;
```

![image](https://github.com/wennie-tung/wehelp/blob/main/week5/img/Task4_2.png?raw=true)


- 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

```sql
SELECT AVG(follower_count) AS avg_follwers FROM member;
```

![image](https://github.com/wennie-tung/wehelp/blob/main/week5/img/Task4_3.png?raw=true)



# Task 5

- 在資料庫中，建立新資料表紀錄留言資訊，取名字為 message。資料表中必須包含以
下欄位設定

```sql
CREATE TABLE message(
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id BIGINT NOT NULL,
    content VARCHAR(255) NOT NULL,
    like_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(member_id)
    REFERENCES member(id)
);

DESC website.message;
```

![image](https://github.com/wennie-tung/wehelp/blob/main/week5/img/Task5_1.png?raw=true)


- 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者的姓名。

```sql
SELECT member.name, message.content FROM member INNER JOIN message ON member.id = message.member_id;
```

![image](https://github.com/wennie-tung/wehelp/blob/main/week5/img/Task5_2.png?raw=true)


- 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者的姓名。

```sql
SELECT member.name, message.content FROM member INNER JOIN message ON member.id = message.member_id WHERE username = 'test';
```

![image](https://github.com/wennie-tung/wehelp/blob/main/week5/img/Task5_3.png?raw=true)


- 使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。

```sql
SELECT AVG(like_count) AS test_avg_likes FROM member INNER JOIN message ON member.id = message.member_id WHERE username = 'test';
```

![image](https://github.com/wennie-tung/wehelp/blob/main/week5/img/Task5_4.png?raw=true)

