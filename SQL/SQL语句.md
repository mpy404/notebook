# 数据库
1. Oracle Database :甲骨文公司
2. SQL Sever: 微软公司
3. DB2：IBM公司
4. PostgreSQL：开源
5. MySQL：开源
6. Access：微软公司[古董]

# 数据库结构
1. 服务端：用于接受并处理其他程序发出的请求程序或者是安装此类程序的设备
2. 客户端：向服务端发出请求的程序（软件），或者是安装此类程序的设备（计算机）
3. 库：就是一堆表组成的数据集合
4. 表：类似Excel，由行和列组成的二维表
5. 字段：表的列（垂直方向）
6. 记录：表的行（水平方向）

# 书写规范
1. 以英文分号结尾
2. sql语句不区大小写，但是插入列表的数据是回区分的
3. 采用关键字大写，表名列名大写
4. 单词使用英文空格隔开
5. 字符串，日期用当引号扩起来如：'Hello World' '2020-2-2'
6. 数字直接书写，不需要单引号如：4
7. 16进制(0x1a3c4d)可以代表字符串，但它却不能代表操作语句

# SQL语句(用关键字、表名和列名等组而成的一条语句)

## 3种SQL语句种类
### DDL(数据定义语言)：创建、删除或修改数据库以及数据库中的表等对象
1. CREATE：创建数据库和表等对象
2. DROP：删除数据库和表等对象
3. ALTER：修改数据库和表等对象
### DML(数据操作语言)：查询修改表中的记录
1. SELECT：查询表中的数据
2. INSERT：想表中插入数据
3. UPDATE：修改表中的数据
4. DELETE：删除表中的数据
### DCL(数据控制语言)：确认或取消对数据库中的数据变更的执行操作，以及对用户的操作数据库中的对象权限进行设定

# 操作
## 库操作
```
增加：
create database db_name;     --->    创建db_name数据库

查看：
show databases;              --->    查看数据库的数量
select database();           --->    查看当前数据库
select user();               --->    查看当前所属用户

删除：
drop database db_name;       --->    删除db_name数据库

进入：
use db_name;                 --->    进入db_name数据库
```
## 表操作
```
增加：
create table db_name(id int,username varchar(),password varchar());    --->    创建表 

删除：
drop table db_name;                          --->     删除db_name表
alter table db_name drop i;                  --->     删除db_name表中一个叫i的字段名

更改：
alter table db_name add i varchar(255);      --->     在db_name表中添加一个叫i的字段名
alter table db_name change user username varchar(255)        --->    将db_name表中的user字段名改成username字段名

查看：
show tables;                                 --->     查看当前表的数量

进入：
desc db_name;                                --->     查看db_name的类型
```
## 一些属性
```
PRIMARY KEY[不能为空且唯一]            --->     主键
AUTO_INCREMENT                       --->    自增长
NOT NULL                             --->   不能为空
eg:
create table mpy(id int PRIMARY KEY AUTO_INCREMENT NOT NULL, usernmae varchar(255), password varchar(255))
将id设置为数值类型   为主键    而且自增长(不给id值会直接跟在上一条数据后面)   且不为空
```
## 数据的操作(数据区分大小写，表名字段名操作语句不区分大小写)
```
增加：
insert into db_name VALUES (1,'mpy',123456)         --->    db_name表中插入数据
insert into db_name (id,password,username)          --->    将数据插入顺序按照id,password,username的顺序来插入

删除：
delete from mpy where id = 1                        --->    将mpy表中id=1的数据给删掉

更改：
update db_name set username = 'mpy' where id = 10   --->    将db_name表中username字段名中的所有值改为mpy 后面的where是条件，当id的值为10时才会发生改变

查看：
select * from db_name                               --->    查询db_name表的所有数据
```