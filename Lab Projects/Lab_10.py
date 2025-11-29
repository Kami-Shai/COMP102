# CCC '02 J1 - 0123456789


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