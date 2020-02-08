<?php
// 数据库连接
$conn = mysqli_connect("127.0.0.1","root","root");
// 修改数据据库名和表名
mysqli_select_db($conn,"mpy");
$tablename = "family";
// 数据库操作
$result = mysqli_query($conn,"select * from " . $tablename);
$counts = mysqli_query($conn,"select count(*) from information_schema.COLUMNS where table_name = " . $tablename);
// 打印每个数据
while($row = mysqli_fetch_row($result)){
    for ($i=0; $i < 3; $i++) { 
        echo "&emsp;&emsp;"."$row[$i]"."&emsp;&emsp;";
    }
    echo "<br />";
}
?>