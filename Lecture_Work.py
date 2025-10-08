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