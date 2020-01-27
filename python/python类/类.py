# !/usr/bin/python3
# -*- coding:utf-8 -*-
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.login_number = 0
        print(self.name)
        print(self.age)

    def jiao(self):
        print(self.name.title() + " wangwang")

    def gun(self):
        print(self.name.title() + " dagong")

    def jia1(self):
        self.login_number += 1
        return self.login_number

    def jian1(self):
        self.login_number -= 1
        return self.login_number

    def zhi(self):
        return self.login_number


my_person = Person("while", 7)
a = my_person.jia1()
print(a)
b = my_person.jian1()
print(b)
c = my_person.zhi()
print(c)

# 继承
class Car(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.wheel = 4

    def run(self):
        do_run = self.name.title() + " is running !!!"
        return do_run

    def norun(self):
        do_notrun = self.name.title() + " is out of oil"
        return do_notrun


class SecondCar(Car):
    def __init__(self, name, color):
        super(SecondCar, self).__init__(name, color)


john = SecondCar("mpy", "red")
print(john)
print(john.run())
print(john.norun())
# class Car(object):
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = str(self.year) + " " + self.make + " " + self.model
#         return long_name.title()

#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles


# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super(ElectricCar, self).__init__(make, model, year)


# my_tesla = ElectricCar("tesla", "model s", 2016)
# print(my_tesla.get_descriptive_name())
