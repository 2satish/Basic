print("Introduction:- My name is Satish Das and I am a Python Coder. The below calculator is made by me.")


num1 = int(input("Put Your first number:" ))
num2 = int(input("Put your 2nd number:" ))
num3 = input("The instructor you want to choose +, -, *, /,**")


if num1 == 45 and num2 == 3 and num3 =='*':
	print("555")
	

if num1 == 56 and num2 == 9 and num3 =='+':
	print("77")
	

if num1 == 56 and num2 == 6 and num3 =='/':
	print("4")
	
if num3 == '+':
	print(num1+num2)
	
if num3 == '-':
	print(num1-num2)
	
if num3 == '*':
	print(num1*num2)
	
if num3 == '/':
	print(num1/num2)
	
if num3 == '**':
	print(num1**num2)


	
print("If you want to know a truth enter the password to know")

password = int(input("Write Password:- "))

if password == 742137 :
	print(" You are using a absolute calculator but due to exam some marks are coded as wrong so do not cheat")
	
else:
	print("Wrong password!")
	
print("Thanks to use this Calculator.")