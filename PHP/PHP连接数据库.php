<?php
// @意思是屏蔽报错
@$id = $_GET['id'];

// 连接数据库
// 方法一
$conn = mysqli_connect("127.0.0.1","root","root","mpy");
// 方法二
$conn = mysqli_connect("127.0.0.1","root","root");
mysqli_select_db($conn,"数据库名字");
// 执行语句
$result = mysqli_query("$conn","SQL语句");
// 便利查询结果
$row = mysqli_fetch_row(); // 返回一行
$table = mysqli_fetch_all(); // 返回全部内容，一个表
$row = mysqli_fetch_array($result); // 以数组返回数据
// 循环打印出每条数据
while ($row = mysqli_fetch_row($result)){
    var_dump($row);
    echo '<br/>';
}

// 关闭数据库
mysqli_close($conn);


?>