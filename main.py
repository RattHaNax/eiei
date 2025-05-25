# Strings
# fist_name = 'Bro'
# food = "pizza"
# email = "Bro123@hee.com"
#
# print(f'Hello {fist_name}')
# print(f"I like {food}")
#from http.client import responses
# from _ast import arguments
# from ftplib import print_line
# from multiprocessing.reduction import duplicate
import math
#Integers
# age = 25
# quantity = 3
# num_of_students = 10
#
# print(f"you are {age} years old")
# print(f"you are buying {quantity} items")
#
# # Float (contains = มีอยู่,บรรจุ)
# price = 10.99
# GPA = 4.0
# distance = 5.5 # ระยะ
#
# print(f"The price is {price}")
# print(f"Your GPA is {GPA}")

# Boolean
# is_student = False
# if is_student:
#     print("you are a student")
# else:
#     print("you are not a student")

# ------------------------------------------------------------------------------------------------------------------------------
#Typecasting คือการเปลี่ยนสถานะของตัวแปรเช่น str>int

# name = "Bro Code"
# age = 25
# gpa = 4.2
# is_student = True

# age = str(age)
# age = age+"100"
# print(age)

# name = bool(name)
# print(name) ถ้าในstr มันว่างจะมีค่าเป็น fail

#--------------------------------------------------------------------------------------------------------------------------
# input คือการเก็บค่าๆนึงไว้แบบ str สามารถเก็บไว้ในตัวแปรได้เช่น name ถ้าจะเอาไปคิดเลขก็ไปเปลี่ยนเป็น int float
# name = input("What is your name? : ")
# age = int(input("How old are you? : "))
# age = age + 1
#
# print(f"Hello {name}")
# print(f"You are {age} years old.")

#---------------------------------------------------------------------------------------------------------------------------
#Exercise 1 Rectangle Area Calc
# Width = int(input("What is your width? : "))
# Legth = int(input("What is your length? : "))
# Area = Width * Legth
# print(Width)
# print(Legth)
# print(f"The area is:{Area}cm")

#----------------------------------------------------------------------------------------------------------------------------
#Eercise 2 Shopping Cart Program
# item = input("มึงจะเอาอะไร?:")
# price = float(input("ราคา:"))
# quantity = int(input("กี่ชิ้น:"))
# total = price * quantity
# print(f"item: {item}, price: {total}")

#-----------------------------------------------------------------------------------------------------------------------------
#friends = 0
#friends += 1 > N = N+1
#friends -= 2 > N = N-2
#friends *= 1 > N = N*2
#friends /= 2 > N = N/2
#friends **= 2 > N = N**2
# remainder = friends % 2 เป็นการหาเศษ
# print(friends)

# import math
#
# x = 3.14
# y = -4
# z = 9

#result = round(x,1) ปัดเศษ เหลือ 1 ตำแหน่ง
#result = abs(y) แอ้บ
#result = pow(4, 3) ยกกำลัง 4 กำลัง 3
# result = max(x,y,z) หาค่าสูงสุด
# result = min(x,y,z) หาค่าต่ำสุด
# result = math.sqrt(z)
# print(result)


#-------------------------------------------------------------------------------------------------------------------------------
# import math
#
# radius = input('Enter the radius of the circle: ')
# radius = float(radius)
# cricumfernece = 2 * math.pi * radius
# print(f"The circumference of the circle is: {cricumfernece}")

# radius = float(input("Enter radius: "))
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle is : {round(area, 2)}cm^2")

#--------------------------------------------------------------------------------------------------------------------------------
# import math
#
# a = float(input("Enter side A : "))
# b = float(input("Enter side B : "))
# c = math.sqrt(pow(a,2)+pow(b,2))
#
# print(f"พื้นที่ของสามเหลี่ยมพีทาโกรัสเท่ากับ: {c}")

#--------------------------------------18--------------30--------------------------------------------infi---------------------------
# if else คือการใช้คำสั่งถ้าถูกตามคำสั่งจะใช้ใน if แค่ถ้าไม่ถูกจะบินไป else
# age = int(input("Enter age : "))
# if age >=30:
#     print('พี่อั้ม')
# elif age >= 18 :
#     print("ผู้ใหญ่")
# else:
#     print("เด็ก")

# response = input("Would you like to continue (y/n)? ")
# if response == "y":
#     print("Goodbye")
# else:
#     print("Bye")

# name = input("What is your name? ")
# if name == "":
#     print("Please enter a name.")
# else:
#     print(f"Hello {name}")

# for_sale = True
# if for_sale:
#     print("This item is for sale") มันเป็น Ture ifจะทำเลย
# else:
#     print("This item is Not for sale")

#------------------------------------------------------------------------------------------------------------------------------------
#Python calculator
# operator = input("Enter an operator(+ - * /): ")
# num1 = float(input("Enter the 1 st number: "))
# num2 = float(input("Enter the 2 st number: "))
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
#     print(f"{operator}ไอเอ๋อ")

#----------------------------------------------------------------------------------------------------------------------------------
#Python weight converter
# weight = float(input("Enter your weight: "))
# unit = input("Killograns or Pounds? (K or L): ")
# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs."
#     print(f"Your weight is {round(weight, 1)} {unit}")
# elif unit == "L":
#     weight = weight * 2.205
#     unit = "Kfs."
#     print(f"Your weight is {round(weight, 1)} {unit}")
# else:
#     print(f"{unit} was not valid.")

#-----------------------------------------------------------------------------------------------------------------------------------
# unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
# temp = float(input("Enter the temperature: "))
# if unit == "C":
#     temp = (temp * 9 / 5) + 32
#     print(f"{temp} แปลงแล้ว")
# elif unit == "F":
#     temp = (temp - 32) * 5/9
#     print(f"{temp} แปลงแล้ว")
# else:
#     print(f"{unit} is not a valid input")

#-------------------------------------------------------------------------------------------------------------------------------------
# or คือใน condition มีเงื่อนไขใดเงื่อนไขนึงที่เชื่อมด้วย or จะทำงาน if เลยเพราะเป็น ture
# and คือใน condition เงื่อนไขทั้งหมดต้องเป็นจริงถึงทำงานใน if
# not ด้านหน้า condition ยังกลับ condition เป็นขั้วตรงข้ามเช่น จากที่เช็ค True เป็น False แทน

# temp = 31
# is_raining = False
#
# if temp > 35 or temp < 15 or is_raining :
#     print("The outdoor event is cancelled")
# else :
#     print("The outdoor event is running")
#----------------
# temp = 5
# is_sunny = False
#
# if temp >= 28 and is_sunny:
#     print("It is Hot outside")
#     print("It is Sunny")
# elif temp <= 0 and is_sunny:
#     print("It is Cold outside")
#     print("It is Sunny")
# elif temp < 28 and temp > 0 and is_sunny:
#     print("It is WARM outside")
#     print("It is Sunny")
# elif temp >= 28 and not is_sunny:
#     print("It is Hot outside")
#     print("It is Cloud")
# elif temp <= 0 and not is_sunny:
#     print("It is Cold outside")
#     print("It is Cloud")
# elif temp < 28 and temp > 0 and not is_sunny:
#     print("It is WARM outside")
#     print("It is Cloud")
#ไอพวกนี้เป็น statement ไม่ได้ตีค่ากลับเป็นข้อความโง่ๆ

#---------------------------------------------------------------------------------------------------------------------------------------
# conditional expression ต้องการ การ return
#สอนเขียน if else ในบรรทัดเดียว
# num = -4
# a = 6
# b = 7
# age = 13
# temperature = 20
# user_role = "guest"
# print("Positive" if num > 0 else "Negative")
# result = "Even" if num % 2 == 0 else "Odd"
# print(result)
#max_num = a if a > b else b
# min_num  = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temperature > 20 else "COLD"
# access_level = "Full Access" if user_role == "admin" else "Limited Access"
#print(max_num)

#--------------------------------------------------------------------------------------------------------------------------------------
#name = input("Ent9er your name: ")
#phone_number = input("Enter your phone number:")
#reesult = len() หาความยาวของตัวอักษรทั้งหมด
#result = name.find("1")หาตำแหน่งตัวที่ใกล้ที่สุดในด้านซ้าย
#result = name.rfind("f")หาตำแหน่งตัวที่ใกล้ที่สุดในด้านขวาแต่ก็ยังนับเหมิอนเดิม
#result = name.capitalize() #เริ่มต้นด้วยตัวพิมพ์ใหญ่ทั้งหมด
#result = name.upper() เปลี่ยนทั้งหมดให้เป็นตัวพิมพ์ใหญ่
#result = name.lower() #เปลี่ยนทั้งหมดให้เป็นตัวพิมพ์เล็ก
#result = name.isdigit() #เช็คbool ถ้าเป็นintหมดเช็ค true
#result = name.isalpha() เช็คbool ถ้าเป็นstrหมดเช็ค true
#result = phone_number.count("-") ต้องหาตัวไรซักอย่างในข้อความ
#result = phone_number.replace("-", "หี")
#print(result)

#---------------------------------------------------------------------------------------------------------------------------------
#print(help(str))

#---------------------------------------------------------------------------------------------------------------------------------
# user = input("Enter your name:")
#
# if len(user) > 12 :
#     print("Please enter a number between 1 and 12")                                                                     )
# elif not user.find(" ") == -1 :
#     print("Your name can't contain space")
# elif not user.isalpha():
#     print("your name can't contain numbers")
# else:
#     print(f"welcome {user}")

#---------------------------------------------------------------------------------------------------------------------------------
#indexing =[Start : End : Step] Start ต้องเป็น STR

# print(credit_number[3])
# print(credit_number [:4]) Start 0 ถึง 3
# print(credit_number [5:8]) Start 5 ถึง 7
# print(credit_number [5:]) Start ตำแหน่ง 5 ถึงตัวท้าย
# print(credit_number [-1]) Start จากตำแหน่งหลังสุด
# print(credit_number [::3])
# last_digits = credit_number[::-1]
# print(f"XXX-XXX-X{last_digits}")

#---------------------------------------------------------------------------------------------------------------------------------
#format specifiers = {value:flags}
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34

# print(f"Price 1 is ${price1:.2f}")ปัดทศนิยมให้เหลือ 2 ตำแหน่งปกติเราใช้ round(price,1) f ย่่อมาก fixed point number
# print(f"Price 2 is ${price2:.2f}")
# print(f"Price 3 is ${price3:.2f}")
# print(f"Price 1 is ${price1:010}") ให้ตัวท้ายข้ามไปตำแหน่ง 10 โดยให้มี 0 มากั้น
# print(f"Price 2 is ${price2:<10}") ชิดซ้ายและมี  space 10 ตัว
# print(f"Price 2 is ${price2:^10}") ให้price2 อยู่ตรงกลางและมี  space 10 ตัว
# print(f"Price 2 is ${price2:>10}") ให้price2 อยู่ขวาและมี  space 10 ตัว
# print(f"Price 3 is ${price3:10}") ให้ตัวท้ายข้ามไปตำแหน่ง 10 โดยให้มี " " มากั้น
# print(f"Price 2 is ${price2:+}") ค่าบวกใส่ +
# print(f"Price 2 is ${price2: }") ค่า + ใส่ space
# print(f"Price 2 is ${price2:,}") ใส่ comma ให้เลขหลัก
# print(f"Price 2 is ${price2:+,.2f}")

#---------------------------------------------------------------------------------------------------------------------------------
# while loop >>> if กับ while   if fail แล้วไป else ส่วน while จะทำไปเรื่อยๆ whiile ทำงานจบloop
# age = int(input("Enter your age: "))
# while(age < 0):
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))
#
# print(f"Your age is {age}")

# food = input("Enter a food you like (q to quit): ")
# while  food != "q":
#     print(f"you like {food}")
#     food = input("Enter a food you like (q to quit): ")
# print("bye")

# num = int(input("Enter a between 1-10: "))
# while num < 1 or num > 10:
#     print(f"{num} is not a valid number")
#     num = int(input("Enter a between 1-10: "))
# print(f"Your number is: {num}")

#--------------------------------------------------------------------------------------------------------------------------------------
#Python compound interest calculator
# principle = 0
# rate = 0
# time = 0
# # while มีไว้รับค่า input ไม่ให่้ <= 0 ส่วน if ก็เช็คและเตือน
# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle can't be less than or equal to 0.")
#
# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#        print("Interest rate can't be less than or equal to 0.")
#
# while time <= 0:
#      time = int(input("Enter the time in years: "))
#      if time <= 0:
#         print("Time can't be less than or equal to 0.")
#
# total = principle * pow((1 +rate / 100), time)
# print(f"Balance after {time} years/s ${total:.2f}")

# while True:
#     principle = float(input("Enter the principle amount: "))
#     if principle < 0:
#         print("Principle can't be less than or equal to 0.")
#     else:
#         break
#
# while True2:
#     rate = float(input("Enter the interest rate: "))
#     if rate < 0:
#         print("Interest rate can't be less than or equal to 0.")
#     else:
#         break
#
# while True:
#     time = int(input("Enter the time in years: "))
#     if time < 0:
#         print("Time can't be less than or equal to 0.")
#     else:
#         break
#
# total = principle * pow((1 +rate / 100), time)
# print(f"Balance after {time} years/s ${total:.2f}")

#---------------------------------------------------------------------------------------------------------------------------------------
#for loops = for x in range(หี , ควย ) เริ่มหี จบ ควย
# import time
# my_time = int(input("Enter the time: "))
# for x in range(my_time,0,-1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600) % 24
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("Time up!")

#--------------------------------------------------------------------------------------------------------------------------------------
#nested loop
# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbols = int(input("Enter the number of symbols: "))
#
# for x in range(rows):
#     for x in range(columns):
#         print(symbols,end="") = end="" คิอการให้ไม่ไปขึ้นบรรทัดใหม่
#     print()

#-------------------------------------------------------------------------------------------------------------------------------------
#collection =
#index กับ list >> list คือชุดข้อมูล index คือการเข้าถึงชุดข้อมูลโดยใช้
#list = [] ordered and changeble. duplicates OK
# fruits = ["apple","banana","orange","mango","pineapple"]
# print(dir(fruits)) บอกคำสั่งที่ใช้ได้
# print(help(fruits))
# print(len(fruits)) บอกความยาวของ list
# print("apple" in fruits) เช็คว่ามี apple
# fruits.append("หี") นำคำว่าหีไปใส่ตัวท้าย append เติมต่อท้าย

# fruits[0] = "หี"  นำคำว่า หี ไปแทนในindex0
# for fruit in fruits:
#     print(fruit) เรียงทุกตัวลง
# fruits.remove("orange") ลบออก
# fruits.insert(3,"orange") เพิ่มส้มลงตำแหน่งที่ 3
#fruits.sort() เรียง A-Z
#fruits.reverse() สลับตำแแหน่ง
# fruits.clear() ลบข้อมูล
# print(fruits.index("orange"))หาตำแหน่งของข้อมูล
# print(fruits.count("apple")) เช็คว่ามีข้อมูลที่ซ้่ำกันกี่ตัว
# print(fruits)
# fruits.pop()
#--------------------------------------------------------------------------------------------------------------------------------------
# Set = {} unorder and immutable, but Add/Remove OK. No duplicate immutable = เปลี่ยนแปลงไม่ได้ ข้างในไม่มีลำดับ
# fruits = {"apple","banana","orange","mango","pineapple"}
#print(dir(fruits))
# print(help(fruits))
#print(len(fruits))
#print("apple" in fruits)
# fruits.add("หี")
# fruits.remove("apple")
# fruits.pop() pop คือคำสั่งลบตัวท้ายแต่ใน set สุ่มลบเพราะunorder
# fruits.clear()
# print(fruits)
# print(fruits.count("apple"))
#-------------------------------------------------------------------------------------------------------------------------------------
# Tuple = () มีลำดับ แต่เปลี่ยนไม่ได้ และ ทำซ้ำได้
# fruits = ("apple","banana","orange","mango","pineapple")
# print(fruits.count("apple"))
# print(fruits)

#-------------------------------------------------------------------------------------------------------------------------------------
#shopping cart program
# foods = []
# prices = []
# total = 0
# while True:
#     food = input("What food do you want to buy? (q to quit): ")
#     if food.lower() == "q": ใช้lower เพราะคนที่กรอก q จะเป็นตัวใหญ่เล็กได้หมด
#         break
#     else:
#         price = float(input(f"Enter the price of {food}: $"))
#         foods.append(food)
#         prices.append(price)
#
# print("---- YOUR CART-----")
# for food in foods:
#     print(food,end=" ")
#
# for price in prices:
#     total += price
#
# print()
# print(f"Your total is ${total}")

#-----------------------------------------------------------------------------------------------------------------------------------
# เมทริกปกติ (groceries[0:2])แถว0ช่อง2
# fruits = ["mango","orange","banana","coconut"]
# pet = ["cat","dog","fish"]
# meat = ["chicken","eggs","milk"]
#
# groceries = (fruits, pet, meat)
#
# for total in groceries: ถ
#     for all in total:
#         print(all, end=" ")
#     print()

#------------------------------------------------------------------------------------------------------------------------------------
# num_pad = ((1,2,3),
#            (4,5,6),
#            (7,8,9),
#            ("+",0,"#"))
# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()

#--------------------------------------------------------------------------------------------------------------------------------------
#dictionary = {key:value}
# capitals = {"USA":"Washington D.C.",
#             "India":"New Delhi",
#             "China":"Beijing",
#             "Russia":"Moscow"}
#print(dir(capitals))
#print(help(capitals))
# print(capitals.get("China")) การหา key ใน dic เพิ่อหา value

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany":"Berlin",
#                  "Italy":"Paris",})
# for name,capital in capitals.items():
#     print(f"{name},{capital}")
# capitals.pop("China") ใข้ pop ในการลบแทน remove
# capitals.popitem()
# Keys =  capitals.keys()
# Values = capitals.values()
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# for key,value in items:
#     print(f"{key}: {value}")

#-----------------------------------------------------------------------------------------------------------------------------------
#Concession stand program
# menu = {"popcorn":1.00,
#         "hotdog":2.00,
#         "giant pretzel":2.00,
#         "asst candy":1.00,
#         "soda":1.00,}
# cart = []
# total = 0
#
# items = menu.items()
# print("CONCESSIONS")
# for key, value in menu.items():
#     print(f"{key:15}: ${value:.2f}")
# print("-----------------------")
#
# while True:
#     food = input("Select an item (q to quit):) ")
#     if food.lower() == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
#
# print(cart)
#
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")
#
# print()
# print(f"Total is: {total:.2f}")

#--------------------------------------------------------------------------------------------------------------------------------------
#สุ่มเลข
# import random
# low = 1
# high = 100
# options = ("rock", "paper", "scissor")
# cards = ["2","3","4","5","6","7","8","9","10","11",]
# number = random.randint(low,high) สุ่มint ภายในช่วง [low,high]
# number = random.random() สุ่ม float ระหว่าง 0ถึง1 ไม่รวม 1
# option = random.choice(options) สุ่มค่าจากใน list tuple string
# random.shuffle(cards) สับรายการแบบสุ่ม
# print(cards)

#----------------------------------------------------------------------------------------------------------------------------------------
# import random
#
# lowest_num = 1
# hightest_num = 100
# answer = random.randint(lowest_num, hightest_num)
# guesses = 0
# is_running = True
#
# print("Python Number Guessing Game")
# print(f"select a number between {lowest_num} and {hightest_num}")
#
# while is_running:
#
#     guess = input("Enter your guess: ")
#
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#
#         if guess < lowest_num or guess > hightest_num:
#             print("That number is out of range")
#             print(f"Please select a number between {lowest_num} and {hightest_num}")
#
#         elif guess < answer:
#             print(f"Your guess is too low")
#         elif guess > answer:
#             print(f"Your guess is too high")
#         else:
#             print(f"CORRECT! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False
#
#     else:
#       print("Invalid guess")
#       print(f"Please enter a number between {lowest_num} and {hightest_num}")

#----------------------------------------------------------------------------------------------------------------------------------
# import random
#
# options = ("rock","paper","scissors")
# running = True
#
# while running:
#     player = None
#     computer = random.choice(options)
#
#     while player not in options:
#         player = input("Enter a chiove (rock, paper, scissors): ")
#
#     print(f"Player: {player}")
#     print(f"computer: {computer}")
#
#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")
#
#     if not input("Do you want to play again? (y/n): ").lower() == "y" :
#         running = False
#
# print("Thank you for playing!")

#-------------------------------------------------------------------------------------------------------------------------------------
#import random
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

# "┌────────────┐"
# "│            │ "
# "│            │ "
# "│            │ "
# "└────────────┘"
#
# dice_art = {
#     1: ("┌────────────┐",
#         "│            │ ",
#         "│      ●     │ ",
#         "│            │ ",
#         "└────────────┘"),
#     2: ("┌────────────┐",
#         "│  ●         │ ",
#         "│            │ ",
#         "│         ●  │ ",
#         "└────────────┘"),
#     3: ("┌────────────┐",
#         "│  ●         │ ",
#         "│     ●      │ ",
#         "│        ●   │ ",
#         "└────────────┘"),
#     4: ("┌────────────┐",
#         "│  ●      ●  │ ",
#         "│            │ ",
#         "│  ●      ●  │ ",
#         "└────────────┘"),
#     5: ("┌────────────┐",
#         "│  ●      ●  │ ",
#         "│     ●      │ ",
#         "│  ●      ●  │ ",
#         "└────────────┘"),
#     6: ("┌────────────┐",
#         "│  ●      ●  │ ",
#         "│  ●      ●  │ ",
#         "│  ●      ●  │ ",
#         "└────────────┘")
# }
#
#
# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))
#
# for die in range(num_of_dice):
#     dice.append(random.randint(1,6))
#
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)
#
# for die in dice : ไม่ได้ใช้ range
#     total += die
# print(f"total: {total}")

#-----------------------------------------------------------------------------------------------------------------------------------
# funtion
# Positional Argument
# No return เพื่อให้แค่แสดงผล และ ไม่ต้องการผลลัพธ์
# def happy_birthday(name,age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()
#
# happy_birthday("bro",20)
# happy_birthday("M",30)
# happy_birthday("Mmi",40)

#  return ที่ใช้เพราะเราต้องการเก็บค่าของตัวของตัวแปรที่เราใช้งาน
# def add(x,y):
#     z = x + y
#     return z
#
# def subtract(x,y):
#     z = x - y
#     return z
#
# def muliply(x,y):
#     z = x * y
#     return z
#
# def divide(x,y):
#     z = x / y
#     return z
#
# frame=add(3,4)
# print(frame)
# frame = print(subtract(3,4))
# frame=muliply(frame,4)
# print(frame)
# frame= print(divide(3,4))

#----------------------------------------------------------------------------------------------------------------------------------------
#default argument = กำหนดค่า default ไว้ใน ฟังก์ชัน ตอนเรียกใช้ถ้าไม่ใส่ค่าเข้าparamitor ค่าที่ส่งไปจะเป็นค่า default

# def net_price(list_price,discount = 0 ,tax =  0.05) :
#     return list_price * (1 - discount) * (1+ tax)
#
# print(net_price(500,0.5))

# import time
# # def count(start = 0,end): ใช้ไม่ได้ ค่าที่จะset default ต้องเอาไปไว้ค่าปกติ
# def count(end,start = 0):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(0.1)
#     print("Done!")
#
# count(30,10)

#-----------------------------------------------------------------------------------------------------------------------------------------
#keyword arguement = ระบุ ชื่อพารามิเตอร์ พร้อมกับค่า paramitor
# def hello(greeting,title,first,last):
#    print(f"{greeting} {title} {first} {last}")
# hello("Hellp","Mr.","spongebob","Squarpepants")
# hello(greeting="Hellp",title="Mr.",first="spongebob",last="Squarpepants")
# hello(greeting="Hellp",title="Mr.","spongebob","Squarpepants") จะใช้ร่วมกับ Positional arguments ต้องใช้ Positional arguments

#-----------------------------------------------------------------------------------------------------------------------------------------
# ARBITRARY
# **kwargs =

# *args = ใช้เมื่อเราไม่ทราบจำนวน arguments (อาร์กิวเมนต์) ที่จะส่งเข้าฟังก์ชันล่วงหน้า ทำให้สามารถรับ หลายค่า ได้อย่างยืดหยุ่น
# def add(*args): บวกทุกตัวในadd
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1,2,3))

# def show_items(*args):
#    for item in args:
#        print("Item:", item)
#
# show_items("Apple", "Banana", "Cherry")

# def display_name(*args):
#     for arg in args:
#         print(arg,end=" ")
#
# display_name("Dr.","Spongebob","Harold","Squarepants","III")

#**kmargs =
# def print_address(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")
#
# print_address(streest="123 Fake St.",city="Detroit",state="MI",zip="54321")

# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg,end=" ")
#     print()
#
#     if "apt" in kwargs:
#         print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#     elif "pobox" in kwargs: อันนี้คือการใช้ membership operator
#         print(f"{kwargs.get('street')}")
#         print(f"{kwargs.get('pobox')}")
#     else:
#         print(f"{kwargs.get('street')}")
#     print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')} ")
#
# shipping_label("Dr.","Spongebob","Squarepant","III",
#                street="123 Fake St.",
#                pobox="PO box #1001",
#                city="Detroit",
#                state="MI",
#                zip="12345")

#------------------------------------------------------------------------------------------------------------------------------------
#Iterables = ใช้ for loop กับ list set tuple dict str

# fruits ={"apples","oranges","pears"} ใช้ revert ไม่ได้เพราะ เป็นเซท
# fruits =("apples","oranges","pears")
# fruits =["apples","oranges","pears"]
# name = "Bro "Code"
# dicks = {1:"one",2:"two",3:"three"}
# for key,value in dicks.items():
#     print(key,value)

#------------------------------------------------------------------------------------------------------------------------------------
#membership operator ใช้ตรวจสอบการมีอยู่ของตัวแปรด้วยการใช้ if  จะมี if in และ if not in(มักใช้ในการตรวจสอบตัวแปร)
#ex1
# Word = "taralalo talala"
# letter = input("Guess a letter in the secret word : ").lower()
#
# if letter not in Word:
#     print_line(f"{letter} not in the secret word")
# else:
#     print_line(f"{letter} in the secret word")
# ex2 ใช้ set
# students = {"mix","frame","miw","few"}
# student = input("Enter the name of a student: ")
#
# if student not in students:
#     print(f"{student} is not a valid student.")
# else:
#     print(f"{student} is valid.")
#ex3 dic
# grads = {"mix":3,"frame":4,"miw":3.5,"few":1}
# student = input("enter the name of a student: ")
#
# if student not in grads:
#     print(f"{student} is not a valid student.")
# else:
#     print(f"student {student} has {grads[student]} grades.")
#ex4 str
# email = "khot96321@gmail.com"
# if "@" in email and "." in email:
#     print("valid email")

#-----------------------------------------------------------------------------------------------------------------------------------
#list comprehension =
# doubles = []
# for x in range(1,11):
#     doubles.append(x*2)
#
# print(doubles)
#ex2 ใช้ list comprehension
# doubles = [x*2 for x in range(1,11)]
# triples = [y*3 for y in range(1,11)]
# squares = [y*4 for y in range(1,11)]
# print(doubles)
# print(triples)
# print(squares)
#ex3
# fruits = ["apple","orange","banana","coconut"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# fruits = ["apple","orange","banana","coconut"]
# fruits_chard = [fruit[0] for fruit in fruits]
# print(fruits_chard)

# numbers = [1,-2,3,-4,5]
# positive_nums = [num for num in numbers if num >= 0]
# print(positive_nums)

# grades =[85,42,30,56,70,78,100]
# grades = [grade for grade in  grades if grade >= 60  ]
# print(grades)

#-----------------------------------------------------------------------------------------------------------------------------------------
#Match-case statment (swich)
# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is Sundy"
#         case 2:
#             return "It is Monday"
#         case 3 :
#             return "It is Tuesday"
#         case 4 :
#             return "It is Wednesday"
#         case 5 :
#             return "It is Thursday"
#         case 6 :
#             return "It is Friday"
#         case 7 :
#             return "It is Saturday"
#         case _ :
#             return "Not a valid day"
# print(day_of_week(3))

# def is_weekend(day):
#     match day:
#         case "Saturday"|"Sunday":
#             return True
#         case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
#             return False
#         case _ :
#             return False
#
# print(is_weekend("Monday"))

#-------------------------------------------------------------------------------------------------------------------------------------------
# module = คือหน่วยข้อมูลเล็กๆที่เราต้องการเรียกใช้
# import math
# from math import e
# import example
#
# result = example.pi
# result = example.square(3)
# result = example.cube(3)
# result = example.cricumference(3)
# result = example.area(3)
#
# print(result)

# -----------------------------------------------------------------------------------------------------------------------------------------
# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

#
# def func1():
#     a = 1
#     print(a)
# def func2():
#     b = 2
#     print(b)
# func1()
# func2()

# def func1():
#     x = 1 #L
#
#     def func2():
#         x = 2 # E
#         print(x)
#
#     func2()
# func1()

# def func1():
#     print(x)
#
# def func2():
#     print(x)
#
# x=3
#
# func1()
# func2()

# from math import e
#
# def func():
#     print(e)
#
# func()

#---------------------------------------------------------------------------------------------------------------------------------------
# from banking1 import *
# balance = 1000
# Show_Balance(balance)
# balance = deposit(balance,200)
# Show_Balance(balance)
# balance= withdraw(balance,300)
# Show_Balance(balance)

#---------------------------------------------------------------------------------------------------------------------------------------
#object
# Class คือ blueprint คือโครงของมันยกตัวอย่างรถ
# from car import Car
#
# car1 = Car("Mustang",2024,"red",False)
# car2 = Car("Corvette",2025,"Blue",True)
# car3 = Car("BMW",2026,"green",False)
#
# print(car3)
# print(car3.model)
# print(car3.year)
# print(car3.color)
# print(car3.for_sale)

#-------------------------------------------------------------------------------------------------------------------------------------
#class variables กำหนดตัวแปรที่ตายตัว
# class Student:
#
#     class_year = 2024 นี่ๆ
#     num_students = 0
#
#     def __init__(self,name,age,height,weight):
#         self.name = name
#         self.age = age
#         Student.num_students += 1
#
# student1 = Student("John",22,23,24)
# student2 = Student("Miji",50,23,24)
# student3 = Student("spongebob",1000,23,24)
# student4 = Student("sunny",26,23,24)
#
# print(student1.name)
# print(student2.age)
# print(student2.class_year)
# print(Student.num_students)
# print(f"graduating class of {Student.class_year} has {Student.num_students} students ")

#---------------------------------------------------------------------------------------------------------------------------------------
#Inheritance การสืบทอด
# class Animal :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.is_alive = True
#
#     def eat(self):
#         print(f"{self.name} is eating.")
#
#     def sleep(self):
#         print(f"{self.name} is sleeping.")
#
# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass
# class Mouse(Animal):
#     pass
#
# dog = Dog("Cola",1)
# cat = Cat("Garfield",2)
# mouse = Mouse("Mickey",1)
#
# print(dog.name)
# print(dog.age)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()

#-----------------------------------------------------------------------------------------------------------------------------------------
# multiple inheritance = ใช้ attribute ของ ตัวแม่มากกว่า 1 class
# class Animal:
#     def __init__(self,name):
#         self.name = name
#
#
#     def sleep(self):
#         print(f"{self.name} Sleeping")
#     def eat(self):
#         print(f"{self.name} Eating")
#
# class Prey(Animal):
#     def flee(self):
#         print(f"This {self.name} is fleeing")
#
# class Predator(Animal):
#     def hunt(self):
#         print(f"This {self.name} is hunting")
# class Rabbit(Prey):
#     pass
#
# class Fish(Prey,Predator):
#     pass
#
# fish = Fish("frame")
# fish.sleep()

#---------------------------------------------------------------------------------------------------------------------------------------------
#super() เราอยากตัดแต่งพันธุกรรมเพิ่มจากปู่
# class Shape: #ปู่
#     def __init__(self,color,is_filled):
#         self.color = color
#         self.is_filled = is_filled
#
#     def describe(self):
#         print(f"Your {self.color} and {"filled" if self.is_filled else "unfilled"}")
#
# class Circle(Shape):
#     def __init__(self,color,is_filled,radius):
#         super().__init__(color,is_filled)
#         self.radius = radius
#
#     def describe(self):
#         print(f"it is {3.14 * self.radius * self.radius}")
#         super().describe()
#
#
# class Square(Shape):
#     def __init__(self,color,is_filled,width):
#         super().__init__(color, is_filled)
#         self.width = width
#
#     def describe(self):
#         print(f"it is {3.14 * self.radius * self.radius}")
#         super().describe()
#
#
# class Triangle(Shape):
#     def __init__(self,color,is_filled,width,height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height
#
#         def describe(self):
#             print(f"it is {3.14 * self.radius * self.radius}")
#             super().describe()
#
# circle = Circle(color="red",is_filled=True,radius=5)
# square = Square(color="Green",is_filled=False,width=5)
# triangle = Triangle(color="red",is_filled=True,width=5,height=6)
#
# print(square.color)

#-------------------------------------------------------------------------------------------------------------------------------------------
#Polymorphism = หลายร่าง
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return side * self.side
#
# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return (self.base * self.height) / 2
#
# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.topping = topping
#
# shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni,15")]
#
# for shape in shapes:
#     print(f"Shape: {shape.area()}")
#
#-----------------------------------------------------------------------------------------------------------------------------------------
# Duck typing = If it looks like a duck quacks like a duck, it must be a duck
# Instance methods = ขึ้นตรงกับ object ^^^^^^^^^
#-----------------------------------------------------------------------------------------------------------------------------------------
# Static methods = ฟังก์ชันที่ไม่ได้เรียก attribute จาก object
# class Employee:
#
#     def __init__(self,name,position):
#         self.name = name
#         self.position = position
#
#     def get_info(self):
#         return f"Name: {self.name}, Position: {self.position}"
#
#     @staticmethod
#     def is_vaild_position(position):
#         vaild_position = ["Manager","Cashier","Cook","Janitor"]
#         return position in vaild_position
#
# employee1 = Employee("M","Manager")
# employee2 = Employee("F","Cook")
# employee3 = Employee("A","Janitor")
#
# print(Employee.is_vaild_position("หี"))
# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())

#---------------------------------------------------------------------------------------------------------------------------------------
#Class methods = การที่เราต้องการเรียกใช้ attribute ของ class
# class Student:
#     count = 0 # พวกนี้คือ attribute ของ class
#     total_gpa = 0
#
#     def __init__(self,name,gpa): # self แทนชื่อของ object
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa
#
#     #INSTANCE METHOD
#     def get_info(self):
#         return f"Name: {self.name}, GPA: {self.gpa}"
#
#     @classmethod # เรียกใช้ attribute ของ class
#     def get_count(cls):
#         return f"Total # of students: {cls.count} "
#     @classmethod
#     def get_total_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"{cls.total_gpa / cls.count} GPA"
#
# student1 = Student("Alex",3.5)
# student2 = Student("Bob",2.5)
#
# print(Student.get_count())
# print(Student.get_total_gpa())

#------------------------------------------------------------------------------------------------------------------------------------------
#Megic methods =

# class Book:
#     def __init__(self,title,author,num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages
#
#     def __str__(self):
#         return f"{self.title} by {self.author}"
#
#     def __eq__(self,other):
#         return self.title == other.title and self.author == other.author
#
#     def __it__(self,other):
#         return self.num_pages < other.num_pages
#
#     def __gt__(self,other):
#         return self.num_pages > other.num_pages
#
#     def __add__(self, other):
#         return f"{self.num_pages + other.num_pages} pages"
#
#     def __contains__(self,other):
#         return keyword in self.title or keyword in self.author
#
#     def __getitem__(self,key):
#         if key == "title":
#             return self.title
#         elif key == "author":
#             return self.author
#         elif key == "num_pages":
#             return self.num_pages
#         else:
#             return f"ket {key} was not found"
#
#
# book1 = Book("The Hobbit","J.R.R Tolkien",310)
# book2 = Book("Harry Potter and The Phillosopher's Stone","J.K. Rowling",223)
# book2 = Book("The Lion,the Wirch and the Wardrobe","C.S. Lewis",172)
#
# print( book1 )
# print( book1 == book2 )
# print( book2 < book1 )
# print( book1 > book2 )
# print("Lion" in book1)
# print("Rowling" in book1)
# print(book1['title'])

#------------------------------------------------------------------------------------------------------------------------------------------
#@property

# class Rectangle:
#     def __init__(self,width,height):
#         self._width = width # เพิ่ม _ ให้ access ให้เข้าถึง medtod ไม่ได้ แล้วไปเข้าใน getter แทน
#         self._height = height
#
#     @property #getter คือการรับค่า
#     def width(self):
#         return f"{self._width:.1f}"
#
#     @property
#     def height(self):
#         return f"{self._height:.1f}"
#
#     @width.setter
#     def width(self,new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be greater than 0")
#
#     @height.setter
#     def height(self,new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("Height must be greater than 0")
#
#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width deleted")
#
#     @height.deleter
#     def height(self):
#         del self._height
#         print("Height deleted")
#
# rectangle = Rectangle(3,4)
#
# rectangle.width = 5
# rectangle.height = 6
#
# del rectangle.width
# del rectangle.height
#
# print(rectangle.width)
# print(rectangle.height)

#-------------------------------------------------------------------------------------------------------------------------------------------
#decorator = เรียกใ
# def add_sprinkles(func):
#     def wrapper():
#         print("*You add sprinkles*")
#         func()
#     return wrapper
#
# def add_fudge(func):
#     def wrapper():
#         print("*You add fudge*")
#         func()
#     return wrapper
#
# @add_fudge
# @add_sprinkles
# def get_ice_cream():
#     print("*You add ice cream*")
#
# get_ice_cream()

#------------------------------------------------------------------------------------------------------------------------------------------------
# exception = ดักจับerror

# try:
#     number = int(input("Enter a number: "))
#     print(1 / number)
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except ValueError:
#     print("You didn't enter a number")
# except Exception:
#     print("Something went wrong")
# finally:
#     print("Do some cleanup here")

#-------------------------------------------------------------------------------------------------------------------------------------------------
#Python file detection หาไฟล์
# import os
# file_path = "test.txt"
#
# if os.path.exists(file_path):
#     print(f"The location {file_path} already exists!")
# else:
#     print(f"The location {file_path} does not exist!")

#Python write file และ Python reading files
#.txt , .json , .csv

#-------------------------------------------------------------------------------------------------------------------------------------------------------
# import datetime
#
# date = datetime.date(2025,1,2)
# today = datetime.date.today()
#
# time = datetime.time(12,30,0)
# now = datetime.datetime.now()
#
# now = now.strftime("%H:%M")
#
# target_dete time = datetime.deteetime(2030,1,2,12,30,1)
# currentt_date = datetime.date.today()

#--------------------------------------------------------------------------------------------------------------------------------------------
#Python Alarm Clock
# import time
# import datetime
# import pygame
#
# def set_alarm(alarm_time):
#     print(f"Alarm set for {alarm_time}")
#     sound_file = "my_music.mp3"
#     is_running = True
#
#     while is_running:
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")
#         print(current_time)
#
#         if current_time == alarm_time:
#             print("WAKE UP")
#
#             pygame.mixer.init()
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play()
#
#             while pygame.mixer.music.get_busy():
#                 time.sleep(1)
#
#             is_running = False
#
#         time.sleep(1)

#---------------------------------------------------------------------------------------------------------------------------------------------
# Multithreading = การทำให้โปรแกรมทำงานหลายงานได้โดยใช้ Thread
# import threading
# import time
#
# def walk_dog(first,last):
#     time.sleep(8)
#     print(f"You finish walking {first}{last}")
#
# def take_out_trash():
#     time.sleep(2)
#     print("You take out trash")
#
# def get_mail():
#     time.sleep(4)
#     print("You get a mail")
#
# chore1 = threading.Thread(target=walk_dog, args=("Scooby","Doo"))
# chore2 = threading.Thread(target=take_out_trash)
# chore2 = threading.Thread(target=take_out_trash)
# chore3 = threading.Thread(target=get_mail)
#
# chore1.start()
# chore2.start()
# chore3.start()
#
# #ใส่เมื่อจบการทำงาน
# chore1.join()
# chore2.join()
# chore3.join()
#
# print("All chore are complete")

#------------------------------------------------------------------------------------------------------------------------------------------
#เชื่อม API ใน python
# import requests
# base_url =  "https://pokeapi.co/api/v2/"
#
# def get_pokemon_info(name):
#     url = f"{base_url}/pokemon/{name}"# ใช้เรียกข้อมูลของโปเกม่อนตัวที่จะเรียก
#     #print(response) ถ้าเรียกสำเร็จจจะขึ้น [200]
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         pokemon_data = response.json()  #เป็นเมธอดของอ็อบเจ็กต์ Response ใน requests เพื่อ แปลงข้อมูล JSON ที่ได้จาก API ให้เป็นโครงสร้างข้อมูลของ Python (เช่น dict หรือ list)
#                                         #ในที่นี้ข้อมูล JSON คือข้อมูลของโปเกมอน
#         return pokemon_data
#     else:
#         print(f"Failled to retrieve data {response.status_code}")
#
# pokemon_name = "Kubfu" # ใส่ชื่อตัวที่จะหาข้อมูล
# pokemon_info = get_pokemon_info(pokemon_name) #กำหนดตัวแปลของ def
#
# if pokemon_info:
#     print(f"{pokemon_info["name"]}")
#     print(f"Id:{pokemon_info["id"]}")
#     print(f"Height:{pokemon_info["height"]}")
#     print(f"Weight:{pokemon_info["weight"]}")

#--------------------------------------------------------------------------------------------------------------------------------------------------























