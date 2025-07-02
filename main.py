# Python Calculator
# operator = input("Enter an operator: +, -, * or / :")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
#
# if operator == "+":
#     result = num1 + num2
#     print(result)
# elif operator == "-":
#     result = num1 - num2
#     print(result)
# elif operator == "*":
#     result = num1 * num2
#     print(result)
# elif operator == "/":
#     result = num1 / num2
#     print(result)
# else:
#     print(f"{operator} does not exists")

# # დაწერეთ ფუნქცია რომელსაც გადაეცემა ერთი არგუმენტი, ეს არგუმენტი იქნება
# # კილომეტრების რაოდენობა, ხოლო ფუნქციამ გადაცემული რიცხვი უნდა გადამიყვანოს
# # მილებში.
# def km_numb(x):
#     miles = x/1.609344
#     return miles
# y = km_numb(5)
# print(y)
# # მაგ: kilometres_to_miles(5) უნდა დააბრუნოს დაახლოებით 3.1
#
# # დაწერეთ ფუნქცია რომელსაც გადავცემ 3 რიცხვს და უკან უნდა აბრუნებს
# # მოცულობას. არცერთი არგუმენტი არ უნდა იყოს სავალდებულო.
# def motsuloba(*args):
#     v = 1
#     for i in args:
#         v *= i
#     return v
# v1 = motsuloba(5,7,9)
# v2 = motsuloba(2,5)
# print(v1)
# print(v2)
# # მაგ: calculate_volume(5, 3, 2) უნდა დააბრუნოს 30. calculate_volume(2, 5)
# # უნდა დააბრუნოს 10 რადგან ერთი არგუმენტი არ გადავეცი
#
# # დაწერეთ ფუნქცია რომელსაც შემიძლია გადავცე უსასრულო რაოდენობის სტრინგები,
# # ხოლო უკან უნდა დამიბრუნოს სია სადაც იქნება მხოლოდ ისეთი სტრინგები რომელიც
# # იწყება ხმოვანით.
# def stringebi(*args):
#     list1 = []
#     for i in args:
#         if i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'u' or i[0] == 'o':
#             list1.append(i)
#     return list1
# string1 = stringebi('miley','selena','adele','sza','oscar')
# print(string1)
# # მაგ: get_vowels("Iaragi", "Globusi", "Energia", "Manqana") უნდა დააბრუნოს
# # ["Iaragi", "Energia"]

# უნდა შექმნათ შემდეგი ორი კლასი: Customer და Bank
#
# Customer კლასი უნდა შეიცავდეს შემდეგ ატრიბუტებს:
# სახელი, გვარი და პირადი ნომერი. ბალანსი არ შეინახოთ მომხმარებლის ობიექტში
#
# Bank კლასი უნდა შეიცავდეს შემდეგ მეთოდებს და ატრიბუტებს:
# სახელი და მისამართის ატრიბუტი, რომელიც გადაეცემა init მეთოდში.
# კლიენტების ატრიბუტი, რომელიც init-ში არ გადაეცემა მაგრამ ავტომატურად
# იქმნება, უნდა იყოს ცარიელი dictionary.
#
# register_account მეთოდი. უნდა გადაეცემოდეს Customer ტიპის ობიექტი და
# საწყისი ბალანსი.
# Customer უნდა შეინახოს კლიენტების დიქტში, თავის ბალანსთან ერთად.
# საწყისი ბალანსი უნდა იყოს 0.
# აუცილებლად უნდა შეინახოთ მლითანი Customer ობიექტი, და არა მისი რომელიმე
# ატრიბუტი, როგორიცაა სახელი ან პირადი ნომერი.
#
# თუ Customer-ის პირადი ნომრით უკვე შექმნილი არის აქოუნტი, მაშინ უნდა
# დაუპრინტოს რომ ამ მომხმარებელს უკვე აქვს ბანკში ანგარიში
# deposit მეთოდი, უნდა გადაეცემოდეს პირადი ნომერი და შესატანი თანხის
# რაოდენობა. კლიენტების dict-ში უნდა იპოვოს მომხმარებელი შესაბამისი პირადი
# ნომრით, და გაზარდოს მისი ბალანსი მითითებული თანხის რაოდენობით.
# თუ ვერ იპოვა მომხმარებელი, დაუპრინტოს რომ მითითებული პირადი ნომრით
# მომხმარებელი არ არსებობს
#
# withdraw მეთოდი, უნდა გადაეცემოდეს პირადი ნომერი და გამოსატანი თანხის
# რაოდენობა.
#
# აქაც იგივე ლოგიკა უნდა იყოს რაც deposit-ში, ეძებს კლიენტს პირადი ნომრით,
# და თუ იპოვა შესაბამის რაოდენობის თანხას გამოიტანს.
# თუ გამოსატანი თანხა აღემატება ჩემს ბალანსზე მყოფ თანხის რაოდენობას, უნდა
# დამიპრინტოს რომ არასაკმარისი თანხა მაქვს.
# თუ პირადი ნომრით კლიენტი ვერ იპოვა, დამიპრინტოს რომ მომხმარებელი არ
# არსებობს
#
# check_balance მეთოდი, გადაეცემა პირადი ნომერი.
# ეძებს მომხმარებელს პირადი ნომრით და აბრუნებს მის ანგარიშზე თანხის
# რაოდენობას, თუ ვერ იპოვა მომხმარებელი დაუპრინტეთ რომ მომხმარებელი არ
# არსებობს.
from logging import exception
from random import choice
from tkinter.font import names


# class Customer:
#     def __init__(self, first_name, last_name, id):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.id = id
#
# class Bank:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#         self.customers = {}
#
#     def register_account(self, customer, initial_balance=0):
#         if customer.id in self.customers:
#             print("This user already has an account in the bank.")
#         else:
#             self.customers[customer.id] = {"customer": customer, "balance": initial_balance}
#             print(f"Account created for {customer.first_name} {customer.last_name}.")
#
#     def deposit(self, id, amount):
#         if id in self.customers:
#             self.customers[id]["balance"] += amount
#             print(f"Deposited ${amount} into account of id {id}.")
#         else:
#             print("The user with the specified personal number does not exist.")
#
#     def withdraw(self, id, amount):
#         if id in self.customers:
#             current_balance = self.customers[id]["balance"]
#             if current_balance >= amount:
#                 self.customers[id]["balance"] -= amount
#                 print(f"Withdrew ${amount} from account of id {id}.")
#             else:
#                 print("Not enough funds.")
#         else:
#             print("The user with the specified personal number does not exist.")
#
#     def check_balance(self, id):
#         if id in self.customers:
#             balance = self.customers[id]["balance"]
#             print(f"Account balance for id {id}: ${balance}")
#         else:
#             print("The user with the specified personal number does not exist.")
#
#
# customer1 = Customer("Luka", "Maisuradze", "01019078839")
# customer2 = Customer("Nini", "Morchiladze", "01019078837")
#
# my_bank = Bank("Pasha", "Rustaveli Avenue")
#
# my_bank.register_account(customer1)
# my_bank.register_account(customer2)
#
# my_bank.deposit("01019078839", 1000)
# my_bank.deposit("01019078837", 500)
#
# my_bank.check_balance("01019078839")
# my_bank.check_balance("01019078837")
#
# my_bank.withdraw("01019078839", 500)
# my_bank.withdraw("01019078837", 1000)
#
# my_bank.check_balance("01019078839")
# my_bank.check_balance("01019078837")


# class Product:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def print_price(self):
#         print(f"{self.name} --- {self.price}ლ")
# class Store:
#     def __init__(self,name,address):
#         self.name = name
#         self.address = address
#         self.products = []
#     #     არგუმენტად უნდა გადაეცემოდეს Product ის ობიექტი და ამატებდეს products ში
#     def add_product(self,product):
#         self.products.append(product)
#     def get_product(self,product_name):
#         for product in self.products:
#             if product.name == product_name:
#                 return product
#     def print_products(self):
#         for product in self.products:
#             product.print_price()
#     def ask_product(self):
#         a = input("რისი ყიდვა გსურს? ")
#         found_product = self.get_product(a)
#         if found_product is None:
#             print("We do not have that Product")
#             self.ask_product()
#         else:
#             self.confirm_purchase(found_product)
#     def confirm_purchase(self,product):
#         print(f"The price of {product.name} is {product.price}ლ")
#         choice = input("Would you like to buy? Y/N: ")
#         if choice == "Y":
#             print("Thank you for shopping with us, good bye!")
#         else:
#             wants_other = input("Would you like to buy something else? Y/N: ")
#             if wants_other == "Y":
#                 self.ask_product()
#             else:
#                 print("Good bye!")
#
# Product1 = Product("Coca-cola",1.25)
# Product2 = Product("Pepsi",1.25)
# Product3 = Product("Nataxtari",1)
#
# store = Store("Giorgis magazia", "Tbilisi")
# store.add_product(Product1)
# store.add_product(Product2)
# store.add_product(Product3)
#
# store.print_products()
# store.ask_product()


# შევქმნათ ახალი მეთოდი სახელად confirm_purchase
# ამ მეთოდს არგუმენტად გადაეცემა Product ობიექტი
# მეთოდი პრინტავს რომ პროდუქტი სახელად ---, ღირს --- ლ
# შემდეგ კი ეკითხება მომხმარებელს ნაღდად სურს თუ არა ყიდვა

# თუ მომხმარებელი ეტყვის რომ სურს ყიდვა, ვუხდით მადლობას და ვემშვიდობებით
# თუ არ უნდა ყიდვა, ვეკითხებით სხვა ნივთის შეძენა თუ სურს
# ტუ სურს სხვა ნივთის შეძენა, ისევ ვეკითხებით რისი ყიდვა სურს
# თუ თქვა რომ არაფრის ყიდვა არ სურს, ვემშვიდობებით

# a = 67
# b = 235
# print(a.__add__(b))
# c = "Luka"
# print(c.__len__())
#
# class Counter:
#     def __init__(self):
#         self.value = 1
#     def count_up(self):
#         self.value += 1
#     def count_down(self):
#         self.value -= 1
#     def __str__(self):
#         return f"Count = {self.value}"
#     def __add__(self, other):
#         if isinstance(other, Counter):
#             return self.value + other.value
#         raise Exception("Invalid type")
# count1 = Counter()
# count2 = Counter()
#
# count1.count_up()
# count2.count_up()
#
# print(count1,count2)
# print(count1 + count2)

# დავალება 1
# def MinimalValue(**kwargs):
#     list = []
#     for i in kwargs:
#         if type(kwargs[i]) == int:
#             list.append(kwargs[i])
#     print(min(list))
# MinimalValue(kwargs_1=23, kwargs2=24,kwargs3 = "Katy", kwargs5 = 58)
#
# # დავალება 2
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n-1)
# print(factorial(5))


# class Car:
#     def __init__(self,brand,model,production_year,color,horse_power,is_sport_car=False):
#         self.__brand = brand
#         self.__model = model
#         self.__production_year = production_year
#         self.__color = color
#         self.__horse_power = horse_power
#         self.__is_sport_car = is_sport_car
#     def get_brand(self):
#         return self.__brand
#     def get_model(self):
#         return self.__model
#     def get_production_year(self):
#         return self.__production_year
#     def get_color(self):
#         return self.__color
#     def get_horse_power(self):
#         return self.__horse_power
#     def get_is_sport_car(self):
#         return self.__is_sport_car
#     def change_color(self,new_color):
#         if new_color != self.__color:
#             new_color = self.__color
#             return True
#         else:
#             return False
#     def increase_horse_power(self, hp):
#         if hp > 0:
#             self.__horse_power += hp
#             return True
#         else:
#             return False

# class Student:
#     university = "Business and Technology University"
#     def __init__(self, name, grade, age):
#         self.name = name
#         self.grade = grade
#         self.age = age
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
#     @property
#     def is_passing(self):
#         if self.grade > 60:
#             return True
#         else:
#             return False
#     def increase_grade(self,additional_grade):
#         self.grade += additional_grade
#         return self.grade
# student1 = Student("Luka",100,23)
# print(student1.__str__())
# print(student1.is_passing)
# print(student1.increase_grade(12))


# for i in range(5):
#     for k in range(10):
#         print("*", end="")
#     print()

# num = 1
# a = int(input("Enter the amount of rows: "))
# for i in range(a):
#     print(num * "*")
#     num += 1

# class Person:
#     def __init__(self,name,surname,age):
#         self.name = name
#         self.surname = surname
#         self.age = age
# class Student(Person):
#     def __init__(self,University,name,surname,age):
#         super().__init__(name,surname,age)
#         self.University = University
#     def mixin(self):
#         print(f"name: {self.name}, surname: {self.surname}, age: {self.age}")
# student = Student("BTU", "Luka", "Natsvlishvili", 23)
# student.mixin()

# class Person:
#     def __init__(self, name='doel'):
#         self.name = name
#
# person = Person('max')
# print(person.name)

# class Heart:
#     def __init__(self,usage):
#         self.usage = usage
#     @property
#     def state(self):
#         if self.usage > 70:
#             return "High Blood Pressure"
#         else:
#             return "Feeling Good"
# class Brain:
#     def __init__(self,usage):
#         self.usage = usage
#     @property
#     def state(self):
#         if self.usage > 90:
#             return "tired"
#         else:
#             return "rested"
# class Person:
#     def __init__(self,heart_usage, brain_usage):
#         self.heart_obj = Heart(heart_usage)
#         self.brain_obj = Brain(brain_usage)
# class Leg:
#     def __init__(self,person,moving_speed):
#         self.person = person
#         self.moving_speed = moving_speed
#     @property
#     def state(self):
#         if self.moving_speed > 10:
#             return "running"
#         elif self.moving_speed == 0 :
#             return "standing"
#         else:
#             return "walking"
#
#     def report(self):
#         return (
#             f"Leg report : {self.state}\n"
#             f"Heart report : {self.person.heart_obj.state}\n"
#             f"Brain report : {self.person.brain_obj.state}"
#         )
# person = Person(heart_usage=75, brain_usage=60)
# leg = Leg(person, moving_speed=12)
# print(leg.report())

# class Shape:
#     def area(self):
#         return "Undefined"
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# shapes = [Rectangle(2, 3), Circle(5)]
# for shape in shapes:
#     print(f"Area: {shape.area()}")
#
# class Animal:
#     def sound(self):
#         return "Some generic sound"
#
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
#
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
#
# # Polymorphic behavior
# animals = [Dog(), Cat(), Animal()]
# for animal in animals:
#     print(animal.sound())  # Calls the overridden method based on the object type
#
# # class Test:
# #     def __init__(self):
# #         self.__value = 10
# # obj = Test()
# # print(obj.__value)

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
#
#     @abstractmethod
#     def stop_engine(self):
#         pass
# class Car(Vehicle):
#     def __init__(self,max_speed):
#         self.max_speed = max_speed
#         self.current_speed = 0
#     def start_engine(self):
#         return "Car started"
#     def stop_engine(self):
#         return "car stopped"
# class SportCar(Car):
#     def start_engine(self):
#         print(super().start_engine())
#         print(f"Car started and it's maximum speed is {self.max_speed}")
#     def stop_engine(self):
#         print(super().stop_engine())
#         self.current_speed = 0
#         print(f"car stopped and it's current speed is {self.current_speed}")
#
# sport_car = SportCar(max_speed=300)
# sport_car.start_engine()
# sport_car.stop_engine()

# from abc import ABC, abstractmethod
#
# class BalanceException(Exception):
#     """
#     Exception to raise when performming invalid operations to balance.
#     """
# class BaseAccount(ABC):
#     @abstractmethod
#     def deposit(self, amount):
#         pass
#
#     @abstractmethod
#     def withdraw(self, amount):
#         pass
#
#     @property
#     @abstractmethod
#     def balance(self):
#         pass
#
# class TransferFundsMixin:
#     def transfer_funds(self, destination_account, amount):
#         withdrawn = self.withdraw(amount)
#         if withdrawn == 1:
#             return f"Transfer failed from {self.account_num} to {destination_account.account_num}"
#         else:
#             destination_account.deposit(amount)
#             return f"Transferred {amount} from {self.account_num} to {destination_account.account_num}"
#
# class BankAccount(BaseAccount, TransferFundsMixin):
#     def __init__(self, account_num, account_holder, init_balance, *args):
#         self.account_num = account_num
#         self.account_holder = account_holder
#         self._balance = init_balance
#
#     def deposit(self, amount):
#         if amount> 0:
#             self.balance += amount
#             print(f"Deposited {amount} in the account. Current balance is {self._balance}")
#         else:
#             print(f"Money you want to deposit into your account is negative: {amount}")
#
#     def withdraw(self, amount):
#         if amount > 0:
#             try:
#                 self.balance -= amount
#             except BalanceException as exp:
#                 print(exp)
#                 return 1
#             print(f"Withdrawn money from the account. amount - {amount}")
#         else:
#             print(f"Money you requested is negative: {amount}")
#
#     @property
#     def balance(self):
#         return self._balance
#
#     @balance.setter
#     def balance(self, amount):
#         if amount < 0:
#             raise BalanceException(f"Insufficient funds provided for the new balance."
#                                    f"new amount: {amount}")
#         else:
#             self._balance = amount
#
#     @property
#     def account_detail(self):
#         return f"{self.account_num} - {self.account_holder}"
#
# class SavingsAccount(BankAccount):
#     def __init__(self,account_num, account_holder, init_balance, interest_rate):
#         super().__init__(account_holder, init_balance, interest_rate)
#         self.interest_rate = interest_rate
#
#     def add_interest(self):
#         interest = self.interest_rate * self.balance
#         self.balance += interest
#         print(f"Interest of {interest} earned for account - {self.account_num}")
#
# class Bank:
#     def __init__(self, name):
#         self.name = name
#         self.account_types= {
#             'debit': BankAccount,
#             'savings': SavingsAccount
#         }
#         self.accounts = {}
#
#     def create_account(self,account_type, account_num, account_holder, init_balance, interest_rate=None):
#         if account_type not in self.account_types:
#             print(f"Requested account type - {account_type} isn't provided by the Bank class."
#                   f"available options - {self.account_types.keys()}")
#             return 1
#
#         if account_num in self.accounts:
#             print(f"Provided account number - {account_num} already exists!")
#         else:
#             new_account = self.account_types.get(account_type)(account_num, account_holder, init_balance, interest_rate)
#             self.accounts[account_num] = new_account
#             print(f"New account has been created with number - {account_num}")
#     def delete_account(self, account_num):
#         if account_num in self.accounts:
#             del self.accounts[account_num]
#             print(f"account with number {account_num} has been deleted")
#         else:
#             print(f"account with number - {account_num} does not exist!")
#
#
#
# bank = Bank('bank')
# bank.create_account('debit','1234','max',12)
# savings = bank.create_account('savings','5678','max',45)
#
# debit = bank.accounts.get('1234')
# savings = bank.accounts.get('5678')
#
# debit.transfer_funds(savings, 20)

# from abc import ABC, abstractmethod
#
# class Person(ABC):
#     def __init__(self,name):
#         self.name = name
#     @abstractmethod
#     def display_details(self):
#         pass
#
# class GradeValidationMixin:
#     def validate_grade(self, grade):
#         if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
#             raise ValueError("Grade must be a number between 0 and 100.")
#
#
# class Student(Person,GradeValidationMixin):
#
#     def __init__(self,student_id,name):
#         super().__init__(name)
#         self.__student_id = student_id
#         self.__grades = {}
#
#     @property
#     def student_id(self):
#         return self.__student_id
#
#     @property
#     def student_grades(self):
#         return self.__grades
#
#     def add_grade(self, subject, grade):
#         self.validate_grade(grade)
#         self.__grades[subject] = grade
#
#     def avarage_grade(self):
#         if not self.__grades:
#             return 0
#         return sum(self.__grades.values())/len(self.__grades)
#
#     def display_details(self):
#         print(f"{self.name} with id number {self.__student_id} has {self.avarage_grade()} avarage grade")
#
# class StudentManagementSystem:
#     def __init__(self):
#         self.students = {}
#
#     def add_student(self, student_id, name):
#         if student_id in self.students:
#             print("Student with this ID already exists.")
#             return
#         student = Student(student_id, name)
#         self.students[student_id] = student
#         print(f"Student '{name}' added successfully.")
#
#     def show_student_details(self, student_id):
#         student = self.students.get(student_id)
#         if student:
#             student.display_details()
#         else:
#             print("Student not found.")
#
#     def show_student_average_grade(self, student_id):
#         student = self.students.get(student_id)
#         if student:
#             print(f"Average Grade: {student.avarage_grade()}")
#         else:
#             print("Student not found.")
#
#     def add_grade_to_student(self, student_id, subject, grade):
#         student = self.students.get(student_id)
#         if student:
#             try:
#                 student.add_grade(subject, grade)
#                 print(f"Grade added for {student.name}.")
#             except ValueError as e:
#                 print(f"Error: {e}")
#         else:
#             print("Student not found.")
#
# obj1 = StudentManagementSystem()
# obj1.add_student(5,"Luka")
# obj1.add_grade_to_student(5,"Math", 10)
# obj1.add_grade_to_student(2,"Biology", 8)
# obj1.show_student_details(5)
# obj1.show_student_average_grade(5)

# print(bool("2>5"))
# print(bool(0.0000000001))

# a = 1
# while True:
#     if a != 1:
#         print('if')
#         break
#     else:
#         print('else')

# print(bool(0.1))
# myvalue = tuple(set(list("abc")))
# print(type(myvalue))
# myvalue1 = {1,2,3}
# print(type(myvalue1))
# my_dict = {'a':1,"b":2,"c":3}
# print(my_dict.get("a"))
# print(my_dict["a"])

# my_dict = {1 : [3,4,5],
#            2: {"Luka", "Nini", "Nodo"},
#            3: "Hello",
#            4: 992
# }
# # მონაცემებზე წვდომის პირველი გზა
# try:
#     print(my_dict[5])
# except KeyError:
#     print("მითითებული Key - ით ვერაფერი მოიძებნა ლექსიკონში")
# # მონაცემებზე წვდომის მეორე გზა get() მეთოდის დახმარებით
# print(my_dict.get(2))
# print(my_dict.get(5,"Not Found"))
# # მითითებული Key -ს Value -ს შეცვლა
# my_dict[3] = {"Lion","Kangaroo"}
# print(my_dict)
# # ახალი წყვილის დამატება ლექსიკონში
# my_dict[5] = [776,235]
# print(my_dict)
# # წყვილის წაშლა
# del my_dict[1]
# my_dict.pop(4)
# print(my_dict)
# # ლექსიკონის მთლიანად წაშლა
# # del my_dict
# # print(my_dict)
# # ლექსიკონის გაცარიელება
# # my_dict.clear()
# # print(my_dict)
# # ლექსიკონის გასაღებების სიის ზრდადობით დალაგება
# t = sorted(my_dict)
# print(t)
# # ლექსიკონის ელემენტების რაოდენობა
# print(len(my_dict))
#
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
#
# my_dict1 = my_dict.copy()
# print(my_dict1)
# my_dict2 = my_dict.fromkeys({1,2},9)
# print(my_dict2)
# my_dict1.update(my_dict2)
# print(my_dict1)
# print(3 in my_dict1)
# print(3 not in my_dict)

# *********************************************************************
# my_list = [6,8,8,8,7,88,12,16]
# print(sum(my_list))
# print(max(my_list))
# print(min(my_list))
# print(len(my_list))
# my_list.append(56)
# print(my_list)
# my_list.insert(6,98)
# print(my_list)
# print(my_list.index(12))
# my_list.remove(6)
# print(my_list)
# my_list.pop(0)
# print(my_list)
# # my_list.clear()
# # print(my_list)
# del my_list[4]
# print(my_list)
# print(my_list.count(8))
# my_list.sort()
# print(my_list)
# my_list.reverse()
# print(my_list)

# ***************************************************
# def sashualo_aritmetikuli(*args):
#     print(sum(args)/len(args))
# sashualo_aritmetikuli(4,5,7,8)
#
# double = [i*i for i in range(10) if i % 2 == 0]
# print(double)


# my_set = set()
# my_set.add(5)
# print(my_set)
# my_set.update([2,3,4])
# print(my_set)
# my_set.update({2,3,6,7,8})
# print(my_set)
# my_set.update("Luka")
# print(my_set)
# my_set.discard(9)
# print(my_set)
# my_set.remove(9)
# print(my_set)
# my_set.pop()
# print(my_set)

# A = {2,3,4}
# B = {4,5,6,7}
# print(A | B)
# print(A.union(B))
# print(A & B)
# print(A.intersection(B))
# print(A - B)
# print(A.difference(B))
# print(A.symmetric_difference(B))
# print(A ^ B)


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return (n * factorial(n - 1))
# print(factorial(88))

# print(hash([]))
# print(hash({}))

# immutable
# x = int(1)
# print(hex(id(x)))
# x += 1
# print(hex(id(x)))
#
# # mutable
# x = []
# print(id(x))
# x.append(1)
# print(id(x))

# ფაქტორიალის ლოგიკა
# def faqtoriali(n):
#     if n == 1:
#         return n
#     else:
#         return n * faqtoriali(n-1)
# print(faqtoriali(5))
# # ფიბონაჩის ლოგიკა
# def fibonacci():
#     fibonacci_list = [0,1]
#     i = 0
#     m = 1
#     k = i + m
#     while k <= 120:
#         fibonacci_list.append(k)
#         i = m
#         m = k
#         k = i + m
#     return fibonacci_list
# print(fibonacci())


# from queue import Queue
# q = Queue(maxsize=15)
# import random
#
# def fifo():
#     while True:
#         if q.full():
#             print("ნაკადი სავსეა")
#             break
#         x = random.randint(1, 100)
#         if 1 <= x <= 10:
#             continue
#         q.put(x)
#         print(f"ნაკადს დაემატა - {x}")
#
#     print("\nFIFO ამოღება:")
#     while not q.empty():
#         print(f"ამოიღო რიგიდან: {q.get()}")
# fifo()

# from chatbot import ChatBot
#
# Hannah: ChatBot = ChatBot(name = "Hannah")
# Hannah.run()

# import pong
# pong.run()

