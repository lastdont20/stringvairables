#quick task:

#1. use input() function to get a list of 5 numbers.
#calculate the total sum, average, biggest and the smallest of the numbers.

#2. names = ["Alice", "Bob", "Charlie", "Diana"] replace Bob with anything else

#3. remove the last name in names.

num1 = int(input(("Enter first numer:")))
num2 = int(input(('Enter secound number:')))
num3 = int(input(("Enter third number:")))
num4 = int(input(("Enter forth number:")))
num5 = int(input(("Enter fifth number:")))
total_sum= num1+num2+num3+num4+num5
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(total_sum)

average = total_sum/5
biggest_num = max(num1,num2,num3,num4,num5)
smallest_num = min(num1,num2,num4,num3,num5)

names= ['Alice', 'Bob','Charlie','Daina']
names[1]='michael'
name1 = names.append['Daina']
print(average)
print(names)