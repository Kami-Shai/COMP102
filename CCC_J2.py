# CCC 2007 J1
# weight_1=int(input('Please enter the first weight = '))
# weight_2=int(input('Please enter the second weight = '))
# weight_3=int(input('Please enter the third weight = '))
# if weight_1>=weight_2>=weight_3 or weight_3<=weight_2<=weight_1:
#     middle=weight_2
# elif weight_2>=weight_1>=weight_3 or weight_3<=weight_1<=weight_2:
#     middle=weight_1
# else:
#     middle=weight_3
# print(middle)
# 
# CCC 2006 J1
# burger=int(input())
# side=int(input())
# drink=int(input())
# dessert=int(input())
# calories=0
# 
# if burger==1:
#     calories+=461
# elif burger==2:
#     calories+=431
# elif burger==3:
#     calories+=420
# 
# if side==1:
#     calories+=100
# elif side==2:
#     calories+=57
# elif side==3:
#     calories+=70
# 
# if drink==1:
#     calories+=130
# elif drink==2:
#     calories+=160
# elif drink==3:
#     calories+=118
# 
# if dessert==1:
#     calories+=167
# elif dessert==2:
#     calories+=266
# elif dessert==3:
#     calories+=75
# 
# print('Your total calorie count is = ',calories)
# 
# CCC 2018 J2
# parking_spaces=int(input())
# spaces_taken_yesterday=input()
# spaces_taken_today=input()
# count=0
# for i in range(5):
#     if spaces_taken_yesterday[i]=='C' and spaces_taken_today[i]=='C':
#         count +=1
# print(count)
# 
# CCC 2021 J2
# bids=int(input())
# max_bid=0
# for i in range(bids):
#     name=input()
#     bid_amount=int(input())
#     if bid_amount>max_bid:
#         max_bid+=bid_amount
#         richest=name
# print(richest)
# 
# CCC 2015 J2
# message=input()
# happy=0
# sad=0
# for i in message:
#     if i==')':
#         happy+=1
#     elif i=='(':
#         sad+=1
# 
# if happy>sad:
#     print('happy')
# elif sad>happy:
#     print('sad')
# elif happy==sad:
#     print('unsure')
# else:
#     print('none')
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
# CCC 2002 J2
# word=input()
# while word != 'quit!':
#     if len(word)>4 and word[-3] not in 'aeiouy' and word[-2:]=='or':
#         print(word[:len(word)-2]+'our')
#     else:
#         print(word)
#     word=input()
# 
# CCC 2009 J2
# trout_p=int(input())
# pike_p=int(input())
# pickerel_p=int(input())
# total_allowed=int(input())
# c=0
# output=""
# for trout in range(total_allowed//trout_p+1):
#     for pike in range(total_allowed//pike_p+1):
#         for pickerel in range(total_allowed//pickerel_p+1):
#             total=trout*trout_p+pike*pike_p+pickerel*pickerel_p
#             if total<=total_allowed and (trout+pike+pickerel)>0:
#                 print(f"{trout} Brown Trout, {pike} Northern Pike, {pickerel} Yellow Pickerel")
#                 c+=1
# print(f"Number of ways to catch fish: {c}")
# 
# CCC 2000 J2
# m=int(input())
# n=int(input())
# c=0
# for i in range(m,n+1):
#     flag=True
#     rotated=""
#     for j in str(i):
#         if j=="1":
#             rotated+="1"
#         elif j=="6":
#             rotated+="9"
#         elif j=="8":
#             rotated+="8"
#         elif j=="9":
#             rotated+="6"
#         else:
#             flag=False
#             break
#     if flag and rotated[::-1]==str(i):
#         c+=1
# print(c)
# 
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
# 
# CCC 2005 J2
# start=int(input())
# end=int(input())
# rsa=0
# for i in range(start,end+1):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==4:
#         rsa+=1
# print(f"The number of RSA numbers between {start} and {end} is {rsa}")
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