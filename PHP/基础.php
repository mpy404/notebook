<!-- 返回变量的类型长度数值 -->
var_dump()
<!-- 拼接用小数点 .-->
$a = 1;
$b = 2;
echo $a.$b;
<!-- 累和 .= -->
$a = 'a';
$b = 'b';
$c = 'c';
$c .= $a; // $c = $c . $a
$c .= $b; // $c = $c . $b
echo $c;  // c = cab
<!-- 循环 -->
for ($a = 0 ; $a < 10; $a ++){
    each 1;
}

<!-- get  post请求 -->
$_GET数组获取GET方式提交的内容
var_dump($_GET) ---> array(1) { ["id"]=> string(1) "1" }

$_POST数组获取POST方式提交的内容
var_dump($_POST) --->array(1) { ["a"]=> string(1) "2" }

$_COOKIE数组获取COOKIE
var_dump($_COOKIE) ---> array(1) { ["PHPSESSID"]=> string(24) "ed9cbceefd89d741262348da" }

$_REQUEST数组获取GET|POST|COOKIE
get传参id = 1
post通过from表单进行传参 a(input.name的name属性) = 2
var_dump($_REQUEST) ---> array(2) { ["id"]=> string(1) "1" ["a"]=> string(1) "2" }

$_REQUEST在PHP5.4版本以上是不会接受cookie值但在5.4以下就会接受到
