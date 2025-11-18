# BISECTION SEARCH
# Lecture 7
# cube = int(input())
# epsilon = 0.01
# low = 0
# high = cube
# guess=(high+low)/2
# while high-low>epsilon:
#     if guess**3<cube:
#         low=guess
#     elif guess**3>cube:
#         high=guess
#     guess=(high+low)/2
# print(f"The cube root of {cube} is approximately {guess}.")

# FUNCTIONS
# Lecture 9
# def div_by(n,d):
#     """
#     docstr
#     """
#     if n%d == 0:
#         return True
#     else:
#         return False
# 
# def sum_all_odd(a,b):
#     for i in range(a,b+1):
#         if i%2 != 0:
#             sum+=i
#     return sum
# 
# def palindrome(s):
# if s[::-1]==s:
#     return True
# else:
#     return False
# 
# def factorial(num):
#     f=1
#     for i in range(1,num+1):
#         f*=i
#     return f
# print(factorial(5))
# 
# Lecture 10
# def apply(criteria,n):
#     c=0
#     for i in range(n+1):
#         if criteria(i):
#             c+=1
#     return c
# 
# def char_counts(s):
#     v=0
#     for char in s:
#         if char in "aeiou":
#             v+=1
#     return (v,len(s)-v)
# print(char_counts("hello"))
# 
# def sum_and_prod(L):
#     sum,prod=0,1
#     for i in L:
#         sum+=i
#         prod*=i
#     return (sum,prod)
# print(sum_and_prod((1,2,3,4,5)))
# 
# Exception Handling
# def pairwise_div(Lnum,Ldenom):
#     assert len(Lnum)!=len(Ldenom),"The lists are not the same size."
#     assert Lnum!=[] and Ldenom!=[],"The list is empty."
#     if 0 in Ldenom:
#         raise ValueError("The denominator contains 0.")
#     return [Lnum[i]/Ldenom[i] for i in range(len(Lnum))]
# 
# DICTIONARIES
# def find_grades(grades,students):
#     student_grades=[]
#     for i in students:
#         student_grades.append(grades[i])
#     return student_grades
# 
# def find_in_L(Ld,k):
#     for dictionary in Ld:
#         if k in dictionary:
#             return True
#     return False
# 
# def count_matches(d):
#     for key,value in d.items():
#         if key==value:
#             c+=1
#     return c
# def get_average(data,what):
#     all_data=[]
#     for stud in data.keys():
#         #
#     return

# def add_rationals(x,y):
# 	return rational(numer(x)*denom(y)+numer(y)*denom(x),denom(x)*denom(y))

# def make_rational(numer,denom):
#     def get_numer():
#         return numer
#     def get_denom():
#         return denom
#     def add_rational(x,y):
#  	    return rational(numer(x)*denom(y)+numer(y)*denom(x),denom(x)*denom(y))
#     def mul_rational():
         
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
# 
#     def get_length(self):
#         return self.length
#     def get_width(self):
#         return self.width    
#     def area(self):
#         return self.get_length()*self.get_width()
#     def perimeter(self):
#         return 2*(self.length+self.width)
# 
# r1=Rectangle(5,10)
# print(r1.area())

# from math import sqrt
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# 
#     def get_x(self):
#         return self.x
#     def get_y(self):
#         return self.y
#     def distance(self,other):
#         d=sqrt((self.get_x()+other.get_x())**2-(self.get_y()+other.get_y())**2)
#         return d
