# 数据类型
1.数值类型 (int long float comple)

```py
	int 
		运算符：+ - * / ** % abs() > >= < <= == != and or not
		+ ：x + y = z
			x = x + y
			x += y
		- : x - y = z
			x = x - y
			x -= y
		* : x * y = z
			x = x * y
			x *= y
		/ : x / y = z
			x = x / y
			x /= y
		% : x % y = z
			10 % 3 = 1
	    ** : 3 ** 2 = 9
		abs() : abs(-3) = 3
	long
	
	float
```

2 布尔类型 (boolean)

```py
	逻辑运算符：
	and 类似乘法运算
	or  类似加法运算 
	not
	公式：
	a or (b and c) = (a or b) and (a or c)
	a and (b or c) = (a and b) or (a and c)
	not (not a) = a
	not (a or b) = (not a) and (not b)
	not (a and b) = (not a) and (not b)
```

3 字符类型 (str)

```py
	用单引号或双引号括起来的是单独的一行	用3个单引号或3个双引号括起来的代表可以是多行
	操作方法：
	调用谋个字符：字符串名字[对应的索引]
	截取某段字符：字符串名字[对应的索引开始:对应索引结束]
	获取字符串长度：len(字符串名字或者一段字符串)
	获取字符的对应编码：ord('字符')
	获取对应编码的字符：chr(编码)

	此外字符串类型还支持 字符的合并(+) 复制(*) 子串测试(in)

	s = '123123123'
	s[0]  --- 这是第一个
	s[-1] --- 这是最后一个
	s[0:-1] --- 从第一个开始截取到最后一个
	s[0:] --- 和上面的是一样的
	print(len(s))
		+ : 'good' + 'bye' ---- 'goodbye'
		* : 2 * 'bye'  ----  'byebye'
		in : 'oo' in 'good'  ---- True
		ord('A') == 65
		chr(65) == A 
```
```py
字符类型和其他类型的转换：

eval() --- 接收一个字符串，并将字符串解释成Python表达式，进行求值，如果无法解释成合法的oythin表达式，则报错

	eval("3.14") -- 3.14
	eval(a + 1) -- 报错
	eval('good' + 'bye') -- 'goodbye'
	a = '123'
	int(a) --- 123
	long(a) --- 123L
	float(a) --- 123.0
	str(a) --- '123'
	bool(a) --- True
	
```
```py
	字符串的方法：
	name = ' m p y '
	name.upper()	--- 所有字母大写
	name.lower()	--- 所有字母小写
	name.title()	--- 所有首字母大写
	name.lsriop()	--- 删除字符串左端空白
	name.rstrip()	--- 删除字符串右段空白
	name.strip() 	--- 删除字符串两端空白


```
4 列表类型 (list)

列表是由若干数据组成的序列

```py

	[1,2,3,4,5,6,7,8,9]

```

	列表方法：

 ```py
	age = [1,2,3,4,5]

		添加元素：
			age.append(6)      --- [1,2,3,4,5,6]
			age.insert(1,10)   --- [1,10,2,3,4,5,6]
			
				append只能往最后一位插入，
				
				insert可以往任意位置插入

		删除元素：
			del age[1] 		   --- [1,2,3,4,5,6]
			age1 = age.pop()   --- age1 = 6
							   --- age = [1,2,3,4,5]
			age2 = age.pop(2)  --- age2 = 3
							   --- age = [1,2,4,5]
			age.remove(1)      --- [2,4,5]
		
				del是把元素给直接删除
		
				pop是把该索引下的参数取出来，并没有删掉
		
				remove是根据值来删除

		切割元素：

			age[1:3]	(从1开始到3结束不包括3)	       --- [2,3]
			age[:2]		(从0开始到2结束)   		      --- [1,2]
			age[1:]     (从1开始到最后)           	  --- [2,3,4,5]
			age[-3:]    (从-3开始(-1是最后一个)到最后)  --- [3,4,5]

		列表排序：

			car = ['d', 'v', 'c', 'x', 'a', 'e']
			car.sort() 				   --- 按照字母顺序进行排序  ['a', 'c', 'd', 'e', 'v', 'x']
			car.sort(reverse = True)   --- 按照字母顺序进行反排序 (默认a-z,添加上就是z-a) ['x', 'v' ,'e' ,'d', 'c', 'a']
			sorted(car) 			   --- 按照字母顺序进行临时排序 ['a', 'c', 'd', 'e', 'v', 'x']（并不影响原来car的顺序）
			sorted(car,reverse = True) --- 按照字母顺序进行反排序 ['x', 'v' ,'e' ,'d', 'c', 'a']（并不影响原来car的顺序）
			car.reverse() 			   --- 会把这组数据反过来打印  ['x','v','e','d','c','a']
			len(car) --- 确认car的长度
			
```
```py

	range()函数 --- 产生一个列表
		一个参数
			如：range(10) --- [0,1,2,3,4,5,6,7,8,9]
		两个参数
			如：range(1,5) --- [1,2,3,4]
		三个参数 (从第一个参数开始加上第三个参数的值到达第二个参数)
			如：range(1,10,2) --- [1,3,5,7,9]

	便利列表：

		ages = [1,2,3,4,5,6]
		for age in ages:
			print(age)  --- 1,2,3,4,5,6
		for age in range(1,7):
			print(age)  --- 1,2,3,4,5,6
	
	便利切割元素：

		ages = [1,2,3,4,5,6,7]
		for age in ages[:3]:
			print(age)  --- 1,2,3

	在数列中用for循环：

		for number in range(1,11):
			print(number ** 2)
		number = [value ** 2 for value in range(1,11)]
		number			--- 1,4,9,16,25,36,49,64,81,100

```
5 元组类型 (tuple)

元组看起来很像列表，但却使用圆括号括起来  


```py
	创建一个元组：
	money = (1,2,3,4,5)
	访问元组：

	money[0]			--- 1
	money[1]			--- 2

	money[0] = 2     ------ 会发现报错  这是因为python指出不能给元组的元素赋值
```

	元组的操作方法

```py

	便利元组：
	ages = (10,11,12,13,14)
	for age in ages:
		print(age)			--- 10,11,12,13,14

	修改元组值：	(通过修改整个元组值来达到修改元素值)
	ages = (10,11,12,13,14)
	print(ages)				--- 10,11,12,13,14
	ages = (0,1,2,3,)
	print(ages)				--- 0,1,2,3,4

```

6 字典类型 (dict)

字典是一系列健-值对。每个键都与一个值相关联，你可以用键来访问与之相关联的健

```py

	创建一个字典

	dog = {
		'name' : 'beibei',
		'age' : 2,
		'color' : gray
	}

	访问字典中的值

	print(dog['name])		--- 'beibei'
	print(dog['age])		--- 2

	添加字典健——值

	dog['weight'] = 100
	dog['eyes'] = 2
	
	修改字典中的值

	dog['name'] = 'huanghuang'
	dog['age'] = 1

	删除字典中的值

	del dog['eyes']

```

便利字典

```py

people = {
	"name": "mpy",
	"age": 19,
	"sex": "man",
	"width": 120,
	"heihgt": 180
	}

	便利键——值

	for key , value in people.items():
		print('keys:' + key)
		print('Values' + value)

	便利键(想要让键按照大小写顺序打印加上sorted())

	for name in sorted(people.keys()):
		print(name)

	便利值(想要让值按照大小写顺序打印加上sorted())

	for value in sorted(people.values()):
		print(value)

	便利独一无二的健或值/去掉相同的键或值	(加上set())

	language = {
		'jen' : 'python',
		'ben' : 'c',
		'ailis' : 'java',
		'john' : 'c'
	}
										让里面的值不会重复出现，并且按照字母顺序打印出来
	for key in set(lanaguage.keys()): 	=====》	for key in sorted(set(language.keys())):
														
		print(key)									print(key)

	for value in set(language.values()):=====》	for value in sorted(set(language.values())):	

		print(value)								print(value)

```

字典存放在列表中

```py

	lists = []
	for lists_number in range(10):
		new_list = {'color' : 'red', 'name' : 'a'}
		lists.append(new_list)
	for list in lists[:5]:
		print(list)

```

在列表中存放字典

```py

language = {
    "jhon": ["python", "c"],
    "winner": ["javascript", "java"],
    "tom": ["html5", "css3", "javascript"],
		}
for name, languages in language.items():
    print(name.title())
    for language in languages:
        print(language.title())
    print("\n")

```
在字典中存放字典

```py


a = {
	"aa": {
		"aaa": "aaa"
		}, 
	"bb": {
		"bbb": "bbb"
		}
	}
print(a)

for name, values in a.items():
    print(name)
    for value in values:
        print(value)

```
