# CCC 2022 J1
# r=int(input('Please enter number of regular boxes = '))
# s=int(input('Please enter number of small boxes = '))
# students=28
# cupcakes=(8*r)+(s*3)
# leftover=cupcakes-students
# print(leftover,'cupcakes were leftover')

# CCC 2020 J1
# s=int(input('Please enter the number of small treats = '))
# m=int(input('Please enter the number of medium treats = '))
# l=int(input('Please enter the number of large treats = '))
# happiness=(1*s)+(2*m)+(3*l)
# print(happiness)
# if happiness>=10:
#     print('Happy!')
# else:
#     print('Sad:(')

# CCC 2019 J1
# apples_three_point=int(input('Please enter the number of 3-points by Apples = '))
# apples_two_point=int(input('Please enter the number of 2-points by Apples = '))
# apples_one_point=int(input('Please enter the number of 1-points by Apples = '))
# bananas_three_point=int(input('Please enter the number of 3-points by Bananas = '))
# bananas_two_point=int(input('Please enter the number of 2-points by Bananas = '))
# bananas_one_point=int(input('Please enter the number of 1-points by Bananas = '))
# apple_total=(apples_three_point*3)+(apples_two_point*2)+(apples_one_point)
# banana_total=(bananas_three_point*3)+(bananas_two_point*2)+(bananas_one_point)
# if apple_total>banana_total:
#     print('A')
# elif apple_total<banana_total:
#     print('B')
# else:
#     print('T')

# CCC 2018 J1
# num_1=int(input('Pleae enter the first digit = '))
# num_2=int(input('Pleae enter the second digit = '))
# num_3=int(input('Pleae enter the third digit = '))
# num_4=int(input('Pleae enter the fourth digit = '))
# if num_1==8 or num_1==9 and num_4==8 or num_4==9 and num_2==num_3:
#     print('Ignore!')
# else:
#     print('Answer!')

# CCC 2017 J1
# x=int(input('Please enter the x-coordinate = '))
# y=int(input('Please enter the y-coordinate = '))
# if x>0:
#     if y>0:
#         print('Quadrant 1')
#     else:
#         print('Quadrant 4')
# elif y>0:
#     print('Quadrant 2')
# else:
#     print('Quadrant 3')

# CCC 2005 J1
# daytime=int(input())
# evening=int(input())
# weekend=int(input())
# plan_a=(evening*0.15)+(weekend*0.2)+max((0,daytime-100))*0.25
# plan_b=(evening*0.35)+(weekend*0.25)+max((0,daytime-250))*0.45
# plan_a=round(plan_a,2)
# plan_b=round(plan_b,2)
# print(f"Plan A costs {plan_a}")
# print(f"Plan B costs {plan_b}")
# if plan_a<plan_b:
#     print(f"Plan A is cheapest.")
# elif plan_b<plan_a:
#     print(f"Plan B is cheapest.")
# else:
#     print(f"Plan A and B are the same price.")

# CCC 2015 J1
# month=int(input('Please enter the month = '))
# day=int(input('Please enter the day = '))
# if month<2 or (month==2 and day<18):
#     print('Before')
# elif month==2 and day==18:
#     print('Special')
# else:
#     print('After')

# CCC 2016 J1
# result_1=input('Please enter a Win or Loss: ')
# result_2=input('Please enter a Win or Loss: ')
# result_3=input('Please enter a Win or Loss: ')
# result_4=input('Please enter a Win or Loss: ')
# result_5=input('Please enter a Win or Loss: ')
# result_6=input('Please enter a Win or Loss: ')
# wins=(result_1=='W')+(result_2=='W')+(result_3=='W')+(result_4=='W')+(result_5=='W')+(result_6=='W')
# if wins>=5:
#     print('1')
# elif wins>=3:
#     print('2')
# elif wins>=1:
#     print('3')
# else:
#     print('-1')