#Run_1
#n=int(input('Enter time in seconds= '))
#while n>=0:
#    print(n)
#    n-=1
#print('Blast off!')

#Run_2
#word=input('Enter your word: ')
#c=0
#for char in word:
#    if char in 'aeiou':
#        c+=1
#print('Number of vowels=',c)

#Run_3
#x=int(input('Enter your cube= '))
#guess=0
#while guess**3!=x:
#    guess+=1
#print('Cube root of',x,'is',guess)

#Problem_1
#word=input()
#i=len(word)-1
#reversed=''
#while i<len(word):
#    reversed+=word[i::-1]
#    i+=1
#print(reversed)
#
#Problem_2
#num=7
#i=1
#for i in range(1,11):
#    print('7 x', i,'=',7*i)
#
#Problem_3
#word='datascience'
#c=0
#for char in word:
#    if char in 'aeiouy':
#        c+=1
#print('Number of consonants:',c)
#
#Problem_4
#num = 0
#found=False
#while found==False:
#    num += 1
#    if num % 6 == 0 and num % 9 == 0:
#        found=True
#print(f"The smallest number divisible by both 6 and 9 is: {num}")
#
# Password_Strength_Checker
#password = input("Enter password: ")
#has_upper = False
#has_lower = False
#has_digit = False
#
#for char in password:
#    if char.isupper():
#        has_upper = True
#    elif char.islower():
#        has_lower = True
#    elif char.isdigit():
#        has_digit = True
#
#if has_upper and has_lower and has_digit:
#    print('Strong Password')
#elif not has_upper:
#    print("Missing at least one uppercase letter.")
#elif not has_lower:
#    print("Missing at least one lowercase letter.")
#elif not has_digit:
#    print("Missing at least one digit.")
#else:
#    print("Weak Password")
#
# CCC Secret Message Decoder
#s=input()
#vowels=''
#for char in s:
#    if char in 'aeiou':
#        vowels+=char
#print(vowels)
#if vowels=='':
#    print('NO VOWELS')
#
# CCC Lucky Ticket Guess
#first_total=0
#second_total=0
#t=input()
#first_half=t[:int(len(t)/2)]
#second_half=t[int(len(t)/2):]
#for char in first_half:
#    first_total+=int(char)
#for char in second_half:
#    second_total+=int(char)
#if first_total==second_total:
#    print('LUCKY')
#else:
#    print('UNLUCKY')