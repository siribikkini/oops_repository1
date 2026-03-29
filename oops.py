# object oriented programmihng language

'''oops is programming based on the concept of "objects".the object contains both data and code:data in the form of properties
{often known as attributes},in the form of methods (actions object can perform)
 1.depends on objects
 2.it provides security

attribute is known as data member or variable
behaviour is also known as member function or method

class:the cls is a user-defined data structure that binds the data members(variables)and methods into a single unit.cls is a blue print or code templet for obj
creation.using a cls,u can create many obj as u want.

syntax:class classname:

class greet():
    print("hello")
greet()

object is simply a collection of data(variables)and methods(functions)that act on those data.similarly,a cls is a blueprint for that object'''




# class siri():
    # constructors
    # functions
    # variables


# we can access the attributes and methods of current class only

# class siri():   #class def
#     def output(self):
#         print("this is cls")
#  object name= class name() object creatiojn
# vivo=siri()
# vivo.output()    #method access cheskovali ante object name.method


# class shiva():
#     a=10
#     def hi(self):
#         print("this is cls")
# siri=shiva()
# print(siri.a)
# siri.hi()


# class siri():
#     a=10
#     def hi(self):
#         print("this is cls")
# siriobj1=siri()
# siriobj=siri()
# siriobj.hi()
# print(siriobj1.a)


# class siri():
#     a=10
#     def show(self):
#         print(self.a)
# satya=siri()
# durga=siri()
# satya.show()
# durga.show()



# class fruits():
#     a="apple"
#     def fruit(self):
#         print(self.a)
# fru=fruits()
# fruitss=fruits()
# fru.fruit()
# fruitss.fruit()




# __init__
# constructor



# class siri():
#     def __init__(self,a,b,c):
#         self.sri=a
#         self.my=b
#         self.name=c
#     def output(self):
#         print(self.sri,self.my,self.name)
# s=siri(1,2,3)
# s.output()




# class dogs():
#     def __init__(self,breed,cost):
#         self.breed=breed
#         self.cost=cost
#     def out(self):
#         print("breed:",self.breed)
#         print("cost:",self.cost)
# while True:
#     breed=input("enter the dog breed:")
#     cost=float(input("enter the cost:"))
#     a=dogs(breed,cost)
#     a.out()
    
        
# class animal():
#     def __init__(self,a,b):
#         self.dog=a
#         self.cat=b
#     def panda(self):
#         print(self.dog,self.cat)
# s=animal("bones","milk")
# s.panda()

    
       


# class fruits():
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def siri(self):
#         print(self.a,self.b,self.c)
# sri=fruits("apple","mango","kiwi")
# sri.siri()

# init is used to intiallise variables and to access from another function in the same cls


# class siri():
#     def __init__(self,mobile_name,price,ram):
#         self.mob=mobile_name
#         self.a=price
#         self.c=ram
#     def sri(self):
#         print("mobile_name:",self.mob)
#         print("price:",self.a)
#         print("ram:",self.c)
# while True:
#     name=input("enter the mobile name:")
#     price=input("enter the mobile price:")
#     ram=input("enter the mobile ram:")
#     d=siri(name,price,ram)
#     d.sri()

# d=siri("realme p3 ultra","25k","8gb")
# d.sri()

# types
# 1.inheritance
# inheritance allows us to define a class that inherits all the methods and properties from another class
# parent cls is the cls being inherited from,also called base cls or super cls
# child cls is the cls that inherits from another class,also called derived cls or sub cls

# types of inheritence
# single inheritence
# multilevel inheritence
# hierarchical inheritence
# multiple inheritence

# 1.1 parent and 1 child cls vunte adi s.i
# 2.grandfather -- father--son/daughter is multilevel
# 3.1 parent and more child cls  father--son and daughter is h.i
# 4.more parent cls single child father and mom --child is multiple inheritance
# 


# polymorphism-polymorphism is the condition of occuramnce in diff forms
# types
# 1.method overloading
# 2.method overriding

# encapsulation
# it is a mechanism of wrapping the data (variables) and code acting on the data (methods)together as a single unit.
# access modifiers
# 1.public-can access anyone like tsrtc etc..,,accessible to outside world   public phone,library
# 2.protected-own car .,,accessible to derived cls  home phone,running notes
# 3.private data-jet plane,,not accessible outside  prsnl phone,diary 

# data abstaction
# internal ga m jaruguthundi anedi manaki avasaram ledu only we need output 

# task
# implement a bike details using init

# class bikes():
#     def __init__(self,bike_name,bike_price,launch):
#         self.a=bike_name
#         self.b=bike_price
#         self.c=launch
#     def output(self):
#         print("bike_name:",self.a)
#         print("bike_price:",self.b)
#         print("launch:",self.c)
# while True:
#      name=input("enter the bike name:")
#      price=float(input("enter the price:"))
#      launch=input("launched in:")
#      bike=bikes(name,price,launch)
#      bike=bikes("MT-150","200000",2018)
#      bike.output()


# class laptop():
#     def __init__(self,a,b):
#         self.c=a
#         self.d=b
#     def mylaptop(self):
#         print("name of laptop:",self.c)
#         print("price of laptop:",self.d)
# lap=laptop("hp",35000)
# lap.mylaptop()


# inheritance

# single inheritance

# class parent():
#     def output(self):
#         print("this is parent cls")
# class child(parent):
#     def  childout(self):
#        print("this is child class")
# obj=child()
# obj.childout()
# obj.output()

# class choco():
#     def shop(self):
#         print("give me milky bar")
# class bis(choco):
#     def shops(self):
#         print("give me biscuits")
# out=bis()
# out.shop()
# out.shops()

# multilevel 


# class father():
#     def outputf(self):
#         print("this is father")
# class mother():
#     def outputm(self):
#         print("this is mother")
# class child(father,mother):
#     def outputc(self):
#         print("this is child cls")
# output=child()
# output.outputf()
# output.outputm()
# output.outputc()


# hierarichal


# class father():
#     def output(self):
#         print("this is father class")
# class child1(father):
#     def output1(self):
#         print("this is child1")
# class child(father):
#     def output2(self):
#         print("this is child2")
# out=child1()
# out1=child()
# out.output()
# out.output1()
# out1.output()
# out1.output2()

# # reusable
# to write flexible code and saves time


# polymorphism


# poly-many
# morph-forms
# 1.method overloading
# 2.method overriding
# 1.example
# class methodoverlod:
#     def siri(self,a="siri",b="siri",c=None):
#         print(a,b,c)
# obj=methodoverlod()
# obj.siri(1,2,3)
# obj.siri(1,2)
# obj.siri(1)
# obj.siri()

# class methodoverri:
#       def display(self):
#             print("this is parent")
# class child(methodoverri):
#       def display(self):
#             print("this is child")
#             super().display()    #super cls lo vunnadi access cheskuntadi
# out=child()
# out.display()

# encapsulation-methods ni attributes ni kalipithe adi encapsulation
# public
# private __(double underscore)
# protected _(single underscore)

# protected

# class gf:
#     def output(self,a):
#         self.__y=a
#         print(self.__y)                                   
# class father(gf):
#     def out1(self):              
#         print(self.__y)
# class child(father):
#     def out2(self):
#         print(self.__y)
# output1=child()
# output1.output(10)
# output1.out1()
# output1.out2()
        
# # private

# class gf:
#     def output(self,a):
#         self._y=a
#         print(self._y)
# class father(gf):
#     def out1(self):
#         print(self._y)
# class child(father):
#     def out2(self):
#         print(self._y)
# output1=child()
# output1.output(10)
# output1.out1()
# output1.out2()


# # global variable(outside the func which can access anywhere)
# a=10
# def func():
#     b=20  #local variable (we can access with in the func only)
#     print("this is fun",b,a)
# func()
# # print(b)
# print(a)


# abstraction(hiding)
# abstract method has no body
# abstract class can not create obj
# a class contain one or more abstract methods then it said to be a abc(abstract base class)
# Abstraction in programming means hiding complex details and showing only what is necessary to the user.

# ✔ Simple Explanation

# Think of a car:
# You press the accelerator → the car moves faster.
# You don’t need to know how the engine, fuel injection, pistons, and sensors work.
# That is abstraction.



# from abc import ABC,abstractmethod
# class car():
#     @abstractmethod  #decorator
#     def mileage(self):
#         pass
# class tesla(car):
#     def mileage(self):
#         print("the mileage is 30kmph")
# class suzuki(car):
#     def mileage(self):
#         print("the mileage is 40kmph")
# t=tesla()
# t.mileage()
# s=suzuki()
# s.mileage()
# c=car()


# Single Inheritance
# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def display_name(self):
#         print(f"Dog's Name: {self.name}")

# class Labrador(Dog):  # Single Inheritance
#     def sound(self):
#         print("Labrador woofs")

# # Multilevel Inheritance
# class GuideDog(Labrador):  # Multilevel Inheritance
#     def guide(self):
#         print(f"{self.name}Guides the way!")

# # Multiple Inheritance
# class Friendly:
#     def greet(self):
#         print("Friendly!")

# class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
#     def sound(self):
#         print("Golden Retriever Barks")

# # Example Usage
# lab = Labrador("Buddy")
# lab.display_name()
# lab.sound()

# guide_dog = GuideDog("Max")
# guide_dog.display_name()
# guide_dog.guide()

# retriever = GoldenRetriever("Charlie")
# retriever.display_name()
# retriever.greet()
# retriever.sound()


# class siri_mro_():

# class siri:
#     def __enter__(self):
#         print("enter")
#         return self
#     def __exit__(self,exc_type,exc,tb):
#         print("exit")
# with siri():
#     pass

# def len2(x):
#     return x.__len__()
# x="sori"
# print(len(x))

# import RPi.GPIO as GPIO
# import time

# FAN_PIN = 17   # GPIO pin connected to relay or fan driver

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(FAN_PIN, GPIO.OUT)

# print("Fan ON")
# GPIO.output(FAN_PIN, True)
# time.sleep(5)

# print("Fan OFF")
# GPIO.output(FAN_PIN, False)

# GPIO.cleanup()


# import tkinter as tk

# initial state
# fan_on = False

# def toggle_fan():
#     global fan_on
#     if not fan_on:
#         fan_on = True
#         status_label.config(text="Fan is ON 🌀")
#         btn.config(text="Switch OFF")
#     else:
#         fan_on = False
#         status_label.config(text="Fan is OFF ⛔")
#         btn.config(text="Switch ON")

# root = tk.Tk()
# root.title("Fan Switch")

# status_label = tk.Label(root, text="Fan is OFF ⛔", font=("Arial", 16))
# status_label.pack(pady=10)

# btn = tk.Button(root, text="Switch ON", font=("Arial", 14), command=toggle_fan)
# btn.pack(pady=10)

# root.mainloop()


# class circle:
#       def __init__(self,radius):
#             self.r=radius
#       def area(self):
#             print(3.14*self.r*self.r)
#       def peri(self):
#             print(2*3.14*self.r)
# out=circle(6)
# out.area()
# out.peri()

# class cal:
#     def __init__(self,a,b):
#         self.a=a
#         self.s=b
#     def add(self):
#         if c=="+":
#            print("addition:",self.a +self.s)
#     def sub(self):
#          if c=="-":
#             print("subtraction:",self.a-self.s)
#     def mul(self):
#          if c=="*":
#             print("multiplication:",self.a*self.s)
#     def div(self):
#          if c=="/":
#             print("division:",self.a/self.s)
# a=int(input("enter the num:"))
# b=int(input("enter the num:"))
# c=input("enter the symbol:")
# out=cal(a,b)
# out.add()
# out.sub()
# out.mul()
# # out.div()


# class cal:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def calcu(self):
#         if c=="+":
#             print("add:",self.a+self.b)
#         elif c=="-":
#             print("sub:",self.a-self.b)
#         elif c=="*":
#             print("mul:",self.a*self.b)
#         else:
#             c=="/"
#             print("div:",self.a/self.b)
# a=int(input("enter the num:"))
# b=int(input("enter the num:"))
# c=input("enter the operator:")
# output=cal(a,b)
# output.calcu()



 
# 3.  create a cls representing a person with attributes name contry and date od birth implement a method to calculate
#  and return the prsns current age.


# class person:
#     def __init__(self,name,country,DOB,):
#         self.a=name
#         self.b=country
#         self.c=DOB
#     def details(self):
#         print("name:",self.a)
#         print("country",self.b)
#         print("DOB",self.c)
#     def birth(self,current_year,birth_year):
#         return current_year - birth_year

# a=int(input("enter the current year:"))
# b=int(input("enter the  year:"))

# output=person("siri","india","15-2-2007")
# output.details()

# age=output.birth(a, b)
# print(age)

# output.birth()birth()
# 4.  design a bank acc cls include activites like acc num acc holder,acc bal,implement methods for cash deposite,cash withdrw,bal check.
 
 
# class Bank:
#     def __init__(self):
#         self.name = input("Name of acc holder: ")
#         self.pin = int(input("Enter the pin: "))
#         self.balance = 100000

#     def menu(self):
#         print("1. Withdraw")
#         print("2. Deposit")
#         print("3. Check balance")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             amount = int(input("Enter amount to withdraw: "))
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print("Amount withdrawn. New balance:", self.balance)
#             else:
#                 print("Insufficient balance")

#         elif choice == "2":
#             amount = int(input("Enter amount to deposit: "))
#             self.balance += amount
#             print("Amount deposited. New balance:", self.balance)

#         elif choice == "3":
#             print("Current balance:", self.balance)

#         else:
#             print("Invalid option")


# # create object and call menu
# account = Bank()
# account.menu()


# class parent():
#     def first(self):
#         print("1st")
# class parent2():
#     def func2(self):
#         print("func2")

# # class child(parent):
# #     def sec(self):
# #         print("2nd")
# class child(parent,parent2):
#     def func3(self):
#         print("this is func")
# a=child()
# a.first()
# a.func2()
# # a.sec()
# a.func3()



     
       


        

        


          














#SVBs5s
25010139844038