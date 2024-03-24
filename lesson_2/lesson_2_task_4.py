def fizz_buzz(n):  
	result = [] 

	for i in range(1, n + 1): 

		if i % 3 == 0 and i % 5 == 0: 
			print("FizzBuzz") 
		elif i % 3 == 0: 
			print("Fizz") 
		elif i % 5 == 0: 
			print("Buzz") 
		else: 
			print(str(i)) 

	return result 
n = 17
result = fizz_buzz(n) 

