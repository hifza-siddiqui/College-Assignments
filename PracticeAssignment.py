# Q1. Solve the following problems by writing Python programs:

# A) Shopping Bill: Write a program to input the price of an item and its quantity. Calculate and display the total bill.
item = input("Enter Product Name: ")
price = int(input("Enter Product Price: "))
quantity = int(input("Enter Product Quantity: "))
total_bill  = price*quantity
print("TOTAL BILL:", total_bill)
print("-------------------------------------------------\n")

# B) Student Marks: Write a program to input marks obtained in three subjects. Calculate and display the total marks and average marks.
sub1 = int(input("Enter Marks Of Computer: "))
sub2 = int(input("Enter Marks Of Maths: "))
sub3 = int(input("Enter Marks Of Physics: "))
total_marks = (sub1 + sub2 + sub3)
avg_marks = (sub1 + sub2 + sub3)/3
percent = ((sub1 + sub2 + sub3)/300)*100
print("TOTAL MARKS (out of 300):", total_marks)
print("PERCENTAGE:", percent)
print("AVERAGE MARKS:", avg_marks)
print("-------------------------------------------------\n")

# C) Rectangle Area: Write a program to input the length and width of a rectangle. Calculate and display its area.Formula: Area = Length × Width
lenght = int(input("Enter Length Of Rectangle: "))
width = int(input("Enter Width Of Rectangle: "))
Area = lenght*width 
print("Area Of Rectangle:", Area)
print("-------------------------------------------------\n")

# D) Square Area: Write a program to input the side of a square and calculate its area. Formula: Area = Side × Side
side = int(input("Enter Side Of A Square:"))
area = side*side
print("Area of A Square:", area)
print("-------------------------------------------------\n")

# E) Simple Interest: Write a program to input principal amount, rate of interest, and time. Calculate and display simple interest. Formula: SI = (P × R × T) / 100
principal_amount = int(input("Enter Principal Amount: "))
rate = int(input("Enter Rate Of Interest: "))
time = int(input("Enter Time: "))
sI = (principal_amount * rate * time)/100
print("Simple Interest:", sI)
print("-------------------------------------------------\n")

# F) Write a python program to input two numbers and display its square and cube.
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
sqr1 = num1 ** 2
sqr2 = num2** 2
print("Square Of First Number:", sqr1)
print("Square Of Second Number:", sqr2)
cube1 = num1 ** 3
cube2 = num2 ** 3
print("Cube Of First Number:", cube1)
print("Cube Of Second Number:", cube2)
print("-------------------------------------------------\n")

# G) Write a program that asks the user to enter their age and displays: "You are ___ years old."
age = int(input("Enter Your Age: "))
print(f"You are {age} years old.")
print("-------------------------------------------------\n")
