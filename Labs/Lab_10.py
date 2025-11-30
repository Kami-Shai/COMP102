# CCC '02 J1 - 0123456789 (Hard)
# N=int(input())
# for _ in range(N):
#     num=input()
#     for char in num:
#         if char=='0' and len(num)>1:
#             continue
#         number=int(char)
# 
#         if number==0:
#             print(" * * *")
#             print("*     *")
#             print("*     *")
#             print("*     *")
#             print("")
#             print("*     *")
#             print("*     *")
#             print("*     *")
#             print(" * * *")
# 
#         if number==1:
#             print("")
#             print("*")
#             print("*")
#             print("*")
#             print("")
#             print("*")
#             print("*")
#             print("*")
#             print("")
# 
#         if number==2:
#             print(" * * *")
#             print("      *")
#             print("      *")
#             print("      *")
#             print(" * * *")
#             print("*")
#             print("*")
#             print("*")
#             print(" * * *")
# 
#         if number==3:
#             print(" * * *")
#             print("      *")
#             print("      *")
#             print("      *")
#             print(" * * *")
#             print("      *")
#             print("      *")
#             print("      *")
#             print(" * * *")
# 
#         if number==4:
#             print("")
#             print("*     *")
#             print("*     *")
#             print("*     *")
#             print(" * * *")
#             print("      *")
#             print("      *")
#             print("      *")
#             print("")
# 
#         if number==5:
#             print(" * * *")
#             print("*")
#             print("*")
#             print("*")
#             print(" * * *")
#             print("      *")
#             print("      *")
#             print("      *")
#             print(" * * *")
# 
#         if number==6:
#             print(" * * *")
#             print("*")
#             print("*")
#             print("*")
#             print(" * * *")
#             print("*     *")
#             print("*     *")
#             print("*     *")
#             print(" * * *")
# 
#         if number==7:
#             print(" * * *")
#             print("      *")
#             print("      *")
#             print("      *")
#             print("")
#             print("      *")
#             print("      *")
#             print("      *")
#             print("")
# 
#         if number==8:
#             print(" * * *")
#             print("*     *")
#             print("*     *")
#             print("*     *")
#             print(" * * *")
#             print("*     *")
#             print("*     *")
#             print("*     *")
#             print(" * * *")
# 
#         if number==9:
#             print(" * * *")
#             print("*     *")
#             print("*     *")
#             print("*     *")
#             print(" * * *")
#             print("      *")
#             print("      *")
#             print("      *")
#             print(" * * *")
#     print()

# CCC '03 J2 - Picture Perfect
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

# CCC '03 S1 - Snakes and Ladders
# position=1
# roll=int(input())
# while roll!=0 and position!=100:
#     position+=roll
# 
#     if position==9:
#         position=34
#     elif position==40:
#         position=64
#     elif position==67:
#         position=86
#     
#     if position==54:
#         position=19
#     elif position==90:
#         position=48
#     elif position==99:
#         position=77
# 
#     if position>100:
#         position-=roll
# 
#     print(f"You are now on square {position}")
#     if position!=100:    
#         roll=int(input())
# 
# if position==100:
#     print("You Win!")
# elif roll==0:
#     print("You Quit!")