# Task 1: Function Abstraction – Circle Calculator
# def circle_properties(radius):
#     area=circle_area(radius)
#     circumference=circle_circumference(radius)
#     return area,circumference
# 
# def circle_area(radius):
#     area=3.14*radius**2
#     return area
# 
# def circle_circumference(radius):
#     circumference=2*3.14*radius
#     return circumference
# print(circle_properties(3))

# Task 2: Guess and Check – Cube Root
# def guess_and_check_cube_root(num):
#     guess=0
#     while guess**3<num:
#         guess+=1
#     if guess**3==num:
#         return guess
#     else:
#         return guess-1
# 
# print(guess_and_check_cube_root(30))
# print(guess_and_check_cube_root(27))

# Task 3: Random Search for Two Integers
# def random_search_sum_of_squares(target):
#     for i in range(1,101):
#         for j in range(1,101):
#             if i**2+j**2==target:
#                 return i,j
#     return None
# 
# print(random_search_sum_of_squares(50))
# print(random_search_sum_of_squares(20000))          

# Task 4: Function Composition – Temperature Converter
# def celsius_to_fahrenheit(celsius):
#     fahrenheit=(celsius*9/5)+32
#     return fahrenheit
# 
# def fahrenheit_to_kelvin(fahrenheit):
#     kelvin=(fahrenheit-32)*5/9+273.15
#     return kelvin
# 
# def celsius_to_kelvin(celsius):
#     fahrenheit=celsius_to_fahrenheit(celsius)
#     kelvin=fahrenheit_to_kelvin(fahrenheit)
#     return celsius,fahrenheit,kelvin
# 
# print(celsius_to_kelvin(25))

# Task 5: Approximate π Using Leibniz Series
# import math
# def approximate_pi(epsilon):
#     approx=0.0
#     k=0
# 
#     while True:
#         term=(-1)**k/(2*k+1)
#         approx+=term
#         pi_approx=4*approx
# 
#         if abs(pi_approx-math.pi)<epsilon:
#             print("Number of terms needed:",k+1)
#             print("Approximation:",pi_approx)
#             return
#         k+=1
# 
# approximate_pi(0.001)

# Task 6: Triangle Type Checker
# def  check_triangle_type(a,b,c):
#     if a+b>c and a+c>b and b+c>a:
#         if a==b==c:
#             return "Equilateral"
#         elif a==b or b==c or a==c:
#             return "Isosceles"
#         else:
#             return "Scalene"
#     else:
#         return "Invalid triangle"
# 
# print(check_triangle_type(3,3,3))
# print(check_triangle_type(4,4,7))   
# print(check_triangle_type(3,4,5))
# print(check_triangle_type(1,2,3))

# Task 7: Custom Operation Calculator
# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def divide(x,y):    
#     return x/y
# def calculator(x,y,operation):
#     if operation=='+':
#         return add(x,y)
#     elif operation=='-':
#         return subtract(x,y)
#     elif operation=='*':
#         return multiply(x,y)
#     elif operation=='/':
#         return divide(x,y)

# CCC '04 J3 - Smile with Similes
# n=int(input())
# m=int(input())
# adjectives=[]
# nouns=[]
# for _ in range(n):
#     adjectives.append(input())
# for _ in range(m):
#     nouns.append(input())
# for i in range(n*m):
#     print(adjectives[i//m]+' as '+nouns[i%m])

# CCC 2006 J2
# m=int(input())
# n=int(input())
# c=0
# for i in range(1,m+1):
#     for j in range(1,n+1):
#         if i+j==10:
#             c+=1
# if c==1:
#     print(f"There is {c} way to get the sum 10.")
# else:
#     print(f"There are {c} ways to get the sum 10.")

# CCC '11 J2 - Who Has Seen The Wind
# h=int(input())
# M=int(input())
# for i in range(1,M+1):
#     A=(-6*(i**4))+h*(i**3)+2*(i**2)+i
#     if A<=0:
#         print(f'The balloon first touches the ground at hour: {i}')
#         break
# if A>0:
#     print('The balloon does not touch ground in the given time.')