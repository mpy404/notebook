## 类的创建
```py

类的创建：

class Person():
# 这里的__init__()是一个特殊的方法，每当宠幸创建一个新的Person类会自动运行
    def __init__(self,name,age):
        # self当创建新的Person类时，会自动传入实参self,它是一个指向实例本身的引用，当向Person()传递name和age时，self会自动传递，因此我们不需要传递它，每当我们根据Person()创建示例时，都只需要给后面的name和age传递值就ok了
        self.name = name
        self.age = age

    def jiao(self):
        print(self.name.title() + " wangwang")


    def gun(self):
        print(self.name.title() + " dagong")

类的调用：

person = Person('beibei' , 20)      ---     person的name = beibei age = 20
person.jiao()                       ---     beibei wangwang
person.gun()                        ---     beibei dagong
    
```
## 继承
```py

class Person(object):
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def run(self):
        do_run = self.name.title() + " is running !!!"
        return do_run

    def norun(self):
        do_notrun = self.name.title() + " is out of oil"
        return do_notrun

class NewPerson(Person):
    def __init__(self , name , age):
        super(NewPerson , self).__init__(name , age)

person = NewPerson('mpy' , 18)

print(person)           --- 看不懂的一个东西
print(person.run())     --- mpy is running !!!
print(person.norun())   --- mpy is out of oil

```
