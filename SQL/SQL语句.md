<font size = 5 color = skyblue>数据库</font>

1. Oracle Database :甲骨文公司
2. SQL Sever: 微软公司
3. DB2：IBM公司
4. PostgreSQL：开源
5. MySQL：开源
6. Access：微软公司[古董]

<font size = 5 color = skyblue>数据库结构</font>

1. 服务端：用于接受并处理其他程序发出的请求程序或者是安装此类程序的设备
2. 客户端：向服务端发出请求的程序（软件），或者是安装此类程序的设备（计算机）
3. 库：就是一堆表组成的数据集合
4. 表：类似Excel，由行和列组成的二维表
5. 字段：表的列（垂直方向）
6. 记录：表的行（水平方向）

<font size = 5 color = skyblue>书写规范</font>
1. 以英文分号结尾
2. sql语句不区大小写，但是插入列表的数据是回区分的
3. 采用关键字大写，表名列名大写
4. 单词使用英文空格隔开
5. 字符串，日期用当引号扩起来如：'Hello World'和'2020-2-2'
6. 数字直接书写，不需要单引号如：4
7. 16进制(0x1a3c4d)可以代表字符串，但它却不能代表操作语句

<font size = 5 color = skyblue>SQL语句(用关键字、表名和列名等组而成的一条语句)</font>

<font size =4  color = red>3种SQL语句种类</font>

<font size = 3 color = yellow> DDL(数据定义语言)：创建、删除或修改数据库以及数据库中的表等对象</font>
 - CREATE：创建数据库和表等对象
 - DROP：&nbsp;&nbsp;&nbsp;&nbsp;删除数据库和表等对象
 - ALTER： &nbsp;&nbsp;修改数据库和表等对象

<font size = 3 color = yellow> DML(数据操作语言)：查询修改表中的记录</font>

 - SELECT：查询表中的数据
 - INSERT：想表中插入数据
 - UPDATE：修改表中的数据
 - DELETE：删除表中的数据

<font size = 3 color = yellow> DCL(数据控制语言)：确认或取消对数据库中的数据变更的执行操作，以及对用户的操作数据库中的对象权限进行设定</font>

<font size = 5 color = skyblue>操作</font>

 - <font size = 4 color = red>库操作</font>

```
增加：

创建db_name数据库   create database db_name;

查看：

查看数据库的数量    show databases;

查看当前数据库    select database();

查看当前所属用户    select user();

删除：


删除db_name数据库     drop database db_name;

进入：


进入db_name数据库       use db_name;
```

  - <font size = 4 color = red>表操作</font>

```
增加：


创建表      create table db_name(id int,username varchar(),password varchar());

删除：


删除db_name表      drop table db_name;

删除db_name表中一个叫i的字段名alter table db_name drop i; 

更改：


在db_name表中添加一个叫i的字段名    alter table db_name add i varchar(255);

将db_name表中的user字段名改成username字段名     alter table db_name change user username varchar(255);

查看：


查看当前表的数量    show tables;

进入：


查看db_name的类型     desc db_name;
```
 - <font size = 4 color = red>一些属性</font>
```
主键    PRIMARY KEY[不能为空且唯一]

自增长  AUTO_INCREMENT

不能为空    NOT NULL

Eg:
create table mpy
(id int PRIMARY KEY AUTO_INCREMENT NOT NULL,
 usernmae varchar(255),
 password varchar(255));
将id设置为数值类型   为主键    而且自增长(不给id值会直接跟在上一条数据后面)   且不为空
```

 - <font size = 4 color = red>数据的操作(数据区分大小写，表名字段名操作语句不区分大小写)</font>

```
增加：


db_name表中插入数据    insert into db_name VALUES (1,'mpy',123456);

将数据插入顺序按照id,password,username的顺序来插入    insert into db_name (id,password,username);

删除：

将mpy表中id=1的数据给删掉   delete from mpy where id = 1;

更改：

将db_name表中username字段名中的所有值改为mpy 后面的where是条件，当id的值为10时才会发生改变
update db_name set username = 'mpy' where id = 10;

查看：

查询db_name表的所有数据     select * from db_name;
```