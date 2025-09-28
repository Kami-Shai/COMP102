# Question_1
# num=int(input('Please enter your number = '))
# print('The square of',num,'is',num*num)
# print('The cube of',num,'is',num*num*num)
# print('The square of',num,'is',num**4)

# Question_2
# from math import pi
# radius=int(input('Please enter the radius of the circle i meters here = '))
# area=pi*(radius**2)
# circumference=2*pi*radius
# volume=(4/3)*pi*(radius**3)
# surface_area=4*pi*(radius**2)
# print('The area of this circle is:',str(round(area))+'m²')
# print('The circumference of this circle is:',str(round(circumference))+'m')
# print('The volume of this circle is:',str(round(volume))+'m³')
# print('The surface area of this circle is:',str(round(surface_area))+'m²')
#
# Question_3
# Method_1
# num=input('Please enter a number between 1000 & 99999= ')
# final_num=''
# for i in num:
#     if i != ',':
#         final_num+=i
# print('Here is the number without its comma:',final_num)
# Method_2
# num=input('Please enter a number between 1000 & 99999= ')
# if len(num)==5:
#     final_num=num[0]+num[2:]
# elif len(num)==6:
#     final_num=num[:2]+num[3:]
# elif len(num)==7:
#     final_num=num[:3]+num[4:]
# print('Here is the number without its comma:',final_num)
#
# Question_4
# months=(
#     "January   "
#     "February  "
#     "March     "
#     "April     "
#     "May       "
#     "June      "
#     "July      "
#     "August    "
#     "September "
#     "October   "
#     "November  "
#     "December  "
# )
# month_number=int(input('Please enter a month number from 1-12 = '))
# start=(month_number-1)*10
# end=(month_number*10)
# print(months[start:end].strip())