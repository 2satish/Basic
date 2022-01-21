while True:
	i = 0
	while i < 6:
		num = int(input ("Enter the number: "))
		
		i = i+1
		
		if num >0 and num < 18:
			print(f"You are lower the number and you have {6-i} chances..")
			
		elif num > 18 and num < 30:
			print(f"You are over the number and you have {6-i} chances...")
			
		elif num == 18:
			print(f"You guessed the correct in {6-i}th time.")
			break 
			
	if i > 5:				
		print("Game over..")
		
	print("Do you wanna play another time? Press 'y' or not for playing press 'n'.")
		
	num2 = input("Write 'y' Or 'n': ")
	
	if num2 == 'n':
		break	