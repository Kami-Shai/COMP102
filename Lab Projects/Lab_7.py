# First Function
# def greet(name):
#     """ Takes a name and returns a greeting message """
#     message="Hello, "+name+"!"
#     return message
# result=greet("Alice")
# print(result)
# result=greet("Bob")
# print(result)
#
# Rectangle Calculator
# def calculate_area (length,width):
#     """ 
#     Calculate area of a rectangle
#     Parameters:
#     length: length of rectangle ( number )
#     width: width of rectangle ( number )
#     Returns:
#     area of rectangle ( number )
#     """
#     area=length*width
#     return area
# print("Rectangle 1: 5 x 3")
# print(f"Area: {calculate_area(5 , 3)}")
# print("\nRectangle 2: 10 x 7")
# print(f"Area: {calculate_area(10 , 7)}")
# 
# def calculate_perimeter(length, width):
#     perimeter=2*(length+width)
#     return perimeter
# 
# Closure Intro
# def make_counter(start):
#     """ 
#     Creates a counter that starts at ’start ’
#     """
#     count=start
#     def increment():
#         """ 
#         Increment and return the count
#         """
#         nonlocal count #This means we use the ’count ’ from parent function
#         count+=1
#         return count
#     return increment
# 
# Create a counter starting at 0
# counter1=make_counter(0)
# # Create a counter starting at 100
# counter2=make_counter(100)
# 
# print ("Counter 1:")
# print (counter1()) # 1
# print (counter1()) # 2
# print (counter1()) # 3
# print ("\nCounter 2:")
# print (counter2()) # 101
# print (counter2()) # 102
# print ("\nCounter 1 again:")
# print (counter1()) # 4 - it remembers!
# 
# Make Adder
# def make_adder(n):
#     """ 
#     Creates a function that adds n to its input 
#     """
#     def adder(x):
#         """ 
#         Add n to x
#         """
#         return n+x
#     return adder
# # Create custom adders
# add5=make_adder(5)
# add10=make_adder(10)
# add100=make_adder(100)
# print("add5(3) =", add5(3)) #8
# print ("add10(3) =", add10(3)) #13
# print ("add100(3) =", add100(3)) #103
# 
# Make Multiplier
# def make_math_function(multiplier,adder):
#     """ 
#     Creates a function that multiplies by ’multiplier ’
#     then adds ’adder ’
#     """
#     def calculate(x):
#         """ 
#         Multiply x by multiplier, then add adder 
#         """
#         result=x*multiplier+adder
#         return result
#     return calculate
# # Double and add 5: f(x) = 2x + 5
# double_plus_5=make_math_function(2,5)
# # Triple and add 10: f(x) = 3x + 10
# triple_plus_10=make_math_function(3,10)
# print(double_plus_5(3)) # 2*3 + 5 = 11
# print(triple_plus_10(3)) # 3*3 + 10 = 19
# 
# List Basics
# numbers=[10,20,30,40,50]
# print ("Numbers:",numbers)
# print ("Type:",type(numbers))
# print ("\nAccessing elements:")
# print ("First element (index 0):",numbers[0])
# print ("Second element (index 1):",numbers[1])
# print ("Last element (index -1):",numbers[-1])
# print ("Second to last (index -2):",numbers[-2])
# print ("\nList length:",len(numbers))
# print ("\nSlicing:")
# print ("First 3 elements [0:3]: ",numbers[0:3])
# print ("Elements 1-3 [1:4]: ",numbers[1:4])
# print ("Last 2 elements [-2:]:",numbers[-2:])
# print ("Every other element [::2]: ",numbers[::2])
# 
# List Mutation
# shopping=["milk","bread","eggs"]
# print("Original list:",shopping)
# print("List ID in memory:",id(shopping))
# print("\nAdding ’butter ’ to the end ...")
# shopping.append("butter")
# print("After append:",shopping)
# print("List ID:",id(shopping),"← Same ID!")
# print("\nRemoving ’bread ’...")
# shopping.remove("bread")
# print("After remove:",shopping)
# print("\nInserting ’cheese ’ at position 1... ")
# shopping.insert(1,"cheese")
# print("After insert:",shopping)
# print("\nSorting alphabetically ...")
# shopping.sort()
# print("After sort:",shopping)
# print("List ID:",id(shopping),"← Still same ID!")
# 
# String to List Conversion
# sentence="Python is an amazing language"
# print("Original sentence:",sentence)
# words=sentence.split()
# print("Split into words:",words)
# print("Number of words:",len(words))
# csv_data="apple, banana, cherry, date"
# print ("\nCSV data:",csv_data)
# fruits=csv_data.split(",")
# print("Split by comma:",fruits)
# colors=["red","green","blue"]
# print("\nList of colors:",colors)
# # The string before .join() is the separator
# result=" ".join(colors)
# print("Joined with spaces:",result)
# result=",".join(colors)
# print("Joined with commas:",result)
# result="-".join(colors)
# print("Joined with dashes:",result)
# 
# Make Greeting
# def make_greeting(greeting_word):
#     """ 
#     Creates a custom greeting function
#     Example :
#     say_hello = make_greeting (" Hello ")
#     say_hello (" Alice ") returns "Hello , Alice !"
#     """
#     def greet(name):
#         message=greeting_word + ", " + name + "!"
#         return message
#     return greet
# # Test
# say_hello=make_greeting ("Hello")
# say_hi=make_greeting ("Hi")
# say_hey=make_greeting ("Hey")
# print(say_hello("Alice")) # Should print: Hello, Alice!
# print(say_hi("Bob")) # Should print: Hi, Bob!
# print(say_hey("Charlie")) # Should print: Hey, Charlie!
# 
# Double List
# def double_all_elements(numbers):
#     """Double every element in the list (MUTATE the list)"""
#     for i in range(len(numbers)):
#         numbers[i]*=2
# # Test
# my_list = [1, 2, 3, 4, 5]
# print("Before:", my_list)
# double_all_elements(my_list)
# print("After:", my_list)  # Should be [2, 4, 6, 8, 10]
# 
# Count Words
# def count_words(sentence):
#     """Count how many words are in a sentence"""
#     words = sentence.split()
#     return len(words)
# # Test
# print(count_words("Hello world"))             # 2
# print(count_words("Python is awesome"))       # 3
# print(count_words("I love programming"))      # 3
# 
# Make Ranged List
# def make_range_list(start, end):
#     """Create a list of numbers from start to end (inclusive)"""
#     result = []
#     for i in range(start, end + 1):
#         result.append(i)
#     return result
# # Test
# print(make_range_list(1, 5))       # [1, 2, 3, 4, 5]
# print(make_range_list(10, 15))     # [10, 11, 12, 13, 14, 15]
# 
# Average
# def calculate_average(numbers):
#     """Calculate average of numbers in a list"""
#     total = sum(numbers)
#     count = len(numbers)
#     return total / count
# # Test cases
# print(calculate_average([10, 20, 30]))         # 20.0
# print(calculate_average([5, 15, 25, 35]))      # 20.0
# print(calculate_average([100]))               # 100.0
# 
# Max
# def find_maximum(numbers):
#     """Find the largest number without using max()"""
#     current_max = numbers[0]
#     for num in numbers[1:]:
#         if num > current_max:
#             current_max = num
#     return current_max
# # Test
# print(find_maximum([3, 7, 2, 9, 1]))   # 9
# print(find_maximum([15, 8, 23, 4]))    # 23
# 
# Remove Duplicates
# def remove_duplicates(items):
#     """Remove duplicates, keep first occurrence"""
#     result = []
#     for item in items:
#         if item not in result:
#             result.append(item)
#     return result
# # Test
# print(remove_duplicates([1, 2, 2, 3, 1, 4]))   # [1, 2, 3, 4]
# 
# Reverse Words
# def reverse_words(sentence):
#     """Reverse order of words in sentence"""
#     words = sentence.split()       # Step 1: Split
#     reversed_words = words[::-1]   # Step 2: Reverse
#     result = " ".join(reversed_words)  # Step 3: Join
#     return result
# # Test
# print(reverse_words("Hello world"))     # "world Hello"
# print(reverse_words("Python is fun"))   # "fun is Python"
# 
# Count Vowels
# def count_vowels(text):
#     """Return a tuple (num_vowels, num_consonants)"""
#     vowels = "aeiouAEIOU"
#     num_vowels = 0
#     num_consonants = 0

#     for ch in text:
#         if ch.isalpha():
#             if ch in vowels:
#                 num_vowels += 1
#             else:
#                 num_consonants += 1
#     return (num_vowels, num_consonants)
# # Tests
# print(count_vowels("Hello"))         # (2, 3)
# print(count_vowels("Programming"))   # (3, 8)
# 
# Find Common
# def find_common(list1, list2):
#     """Return elements appearing in BOTH lists, no duplicates"""
#     result = []
#     for item in list1:
#         if item in list2 and item not in result:
#             result.append(item)
#     return result
# # Tests
# print(find_common([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]
# print(find_common(['a', 'b'], ['c', 'd']))      # []
# 
# Make Accumulator
# def make_accumulator():
#     total = 0
#     def accumulator(x):
#         nonlocal total
#         total += x
#         return total
#     return accumulator
# # Example
# acc = make_accumulator()
# print(acc(5))    # 5
# print(acc(10))   # 15
# print(acc(3))    # 18
# acc2 = make_accumulator()
# print(acc2(100)) # 100 (separate accumulator)
# 
# CCC 2007 J2
# message=input()
# while message!='TTYL':
#     if message=='CU':
#         print('see you')
#     elif message==':-)':
#         print("I'm happy")
#     elif message==':-(':
#         print("I'm unhappy")
#     elif message==';-)':
#         print('wink')
#     elif message==':-p':
#         print('stick out my tounge')
#     elif message=='(~.~)':
#         print('sleepy')
#     elif message=='TA0':
#         print('totally awesome')
#     elif message=='CCC':
#         print('Canadian Computing Competition')
#     elif message=='CUZ':
#         print('because')
#     elif message=='TY':
#         print('thank-you')
#     elif message=='YW':
#         print("you're welcome")
#     else:
#         print(message)
#     message=input()
# print('talk to you later')
# 
# CCC 2008 J2
# b=int(input())
# playlist="ABCDE"
# while b!=4:
#     n=int(input())
#     for i in range(n):
#         if b==1:
#             playlist=playlist[1:]+playlist[0]
#         elif b==2:
#             playlist=playlist[-1]+playlist[:4]
#         elif b==3:
#             playlist=playlist[1]+playlist[0]+playlist[2:]
#     b=int(input())
# print(*playlist)
# 
# CCC 2011 S2
# n = int(input())
# student = []
# correct = []
# 
# for i in range(n):
#     ans = input()
#     student.append(ans)
# 
# for i in range(n):
#     ans = input()
#     correct.append(ans)
# 
# score = 0
# for i in range(n):
#     if student[i] == correct[i]:
#         score += 1
# 
# print(score)