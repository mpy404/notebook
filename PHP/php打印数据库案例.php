<?php
// 数据库连接
$conn = mysqli_connect("127.0.0.1","root","root");
mysqli_select_db($conn,"mpy");
// 数据库操作
$result = mysqli_query($conn,"select * from family");
// 打印每个数据
while($row = $result->fetch_row())
{
    for ($i=0; $i < 3; $i++) { 
        echo "&emsp;&emsp;"."$row[$i]"."&emsp;&emsp;"; //这里是不是一行，放4个要显示的值不就行了？
    }
    echo "<br />";
}

?>