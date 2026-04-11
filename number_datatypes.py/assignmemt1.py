import random

''''''''''
scond = 2*2*2*2*2*2*2*2*2
a = 'python' 
b = 'py'+ 'thon'
print(b is b)
print(b)
c= 2**(3**2)
print(c)
d= 2+3*5
print(d)
e= 2**3
print(e)
f=x,y=12,"3"
print(f)
x= 12
y = '3'
#print(x+y)

First_Name = 'Tochukwu'
Last_Name = "Henry"
part1 = First_Name[::2]
part2 = Last_Name[:3]
import random
otp_number= round(random.random() *10000)
print(otp_number)

password = part1+part2+str(otp_number)
#print(password)
print("generate pasword:", password)


print(5+5*2)

x=5
y=2
print(x//y)
print(4**2)
'''''''''''


# to get password that contains first and secound name plus otp numbers
'''''''''
import random
first_name = 'chukwudi'
last_name = "miracle"
first3_letters = first_name[::2]
three_letters = last_name[:3]
OTP = round(random.random() *10000)
print(first3_letters+three_letters+ str(OTP))

n = 20



print(n <<2)

'''

'''''''''
name = "nuel"
check = name[::]
lastcheck =check[::-1]
print(lastcheck)
print(check)
print(name==lastcheck)

'''

#i want to check if these words are palindrome:
#1. racecar
#2. hello
#3. Nuel
#4. madam
#5. level
#who can do it?
''''''''''
firstline = 'racecar'
check = firstline[::]
check2 =firstline[::-1]
print(check==check2)
'''''

''''''''''''''''
name = 'hello'
check1 = name[::]
check2 = name[::-1]
print(check1==check2)

'''''''''''


'''''''''''''''
name = 'madam'
check1 = name[::]
check2 = name[::-1]
print(check1==check2)
'''''''''''



'''''''''''''''
name = 'level'
check1 = name[::]
check2 = name[::-1]
print(check1==check2)
'''''''''''


# to know if spell dackward if it will give the same spelling
num = 12321
check1 = str(num)[::]
reversed = str(num)[::-1]
print(reversed==check1)

c= 2**(3**2) # this means 2*2*2*2*2*2*2*2*2 (2 into 9 paces)
print(c)






# to know if spell dackward if it will give the same spelling
name = 'ekitike'
b = name[::]
c = name[::-1]
print(c==b)

# python quiz
number = [0,1,2,3,4,5,6,7,8,9]
print(number[::-2]) # to pick 2 number from back to the end

number1 = [1,2,3,4] 
number1[:2]=[8,9]
print(number1)

num=5.9
print(int(num))


x=5
y=2
print(x//y) #to remove remainder
print(x/y) # to divide
print(x%y) # print only the remainder
print(4**2)

# count number the variable are
num2 = [5,10,15,20,25]
val = num2
print(len(num2))

num2 = [5,10,15,20,25]
print(num2[1])

num=5.9
print(int(num))

a = [1,2,3]
b =a
b+=[4]
print(a)
print(5>3 and 2<1)

d= 5*3**5
print(d)