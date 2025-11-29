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

# CCC '04 J4 - Simple Encryption
key=input()
message=input()
for char in message:
    if char.isalpha():
        