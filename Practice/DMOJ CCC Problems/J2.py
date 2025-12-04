# CCC 2018 J2
# parking_spaces=int(input())
# spaces_taken_yesterday=input()
# spaces_taken_today=input()
# count=0
# for i in range(5):
#     if spaces_taken_yesterday[i]=='C' and spaces_taken_today[i]=='C':
#         count +=1
# print(count)

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

# CCC 2002 J2
# word=input()
# while word != 'quit!':
#     if len(word)>4 and word[-3] not in 'aeiouy' and word[-2:]=='or':
#         print(word[:len(word)-2]+'our')
#     else:
#         print(word)
#     word=input()

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

# CCC 2003 J2
# c=int(input())
# result=""
# while c!=0:
#     minimum=999999
#     best_col=0
#     best_row=0
#     for row in range(1,c+1):
#         for col in range(1,c+1):
#             if row*col==c:
#                 if 2*(row+col)<minimum:
#                     best_row=row
#                     best_col=col
#                     minimum=(2*(row+col))
#     result+=f"Minimum perimeter is {minimum} with dimensions {best_row} x {best_col}\n"
#     c=int(input())
# print(result,end="")

# # CCC '17 J2 - Shifty Sum
# N=int(input())
# k=int(input())
# sum=0
# for i in range(k+1):
#     sum+=N
#     N*=10
# print(sum)

# CCC '25 J2 - Donut Shop
# D=int(input())
# E=int(input())
# for i in range(E):
#     symbol=input()
#     Q=int(input())
#     if symbol=='+':
#         D+=Q
#     elif symbol=='-':
#         D-=Q
# if D<0:
#     D=0
# R=D
# print(R)

# CCC '25 J3 - Product Codes
# N=int(input())
# for _ in range(N):
#     code=input()
#     new_code=''
#     total=0
#     for i in range(len(code)):
#         if code[i].isupper():
#             new_code+=code[i]
#         elif code[i].isdigit():
#             total+=int(code[i])
#         if code[i].isdigit() and code[i+1].isdigit():
#             total+=int(code[i]+code[i+1])
#     print(f'{new_code}{total}')

# CCC '23 J2 - Chili Peppers
# N=int(input())
# SHU=0
# for i in range(N):
#     pepper=input()
#     if pepper=='Poblano':
#         SHU+=1500
#     elif pepper=='Mirasol':


# CCC '23 J3 - Special Event
N=int(input())
attendable={}
for _ in range(N):
    availability=input()
    for i in range(len(availability)):
        if availability[i]=='Y':
            if i not in attendable:
                attendable[i]=0
            attendable[i]+=1
