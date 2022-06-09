def factorial(num):
	if num == 1:
		return 1
	return num * factorial(num - 1)

def palindrome(string):
	if len(string) <= 1:
		return True
	return string[0] == string[len(string) - 1] and palindrome(string[1: len(string) - 1])
	

def bottles(num):
	if (num == 1):
		return 'Take one down and pass it around, 1 bottle of beer on the wall. 1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.';
	else :
		print(f"{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num - 1} bottles of beer on the wall.")
		return bottles(num - 1)
	

def roman_num(num):
	
	for i,j in [(1000, "M"), (944, "CMXLIV"), (500, "D"), (100, "C"), (50, "L"), (44, "XLIV"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1,"I")] :
		if num >= i :
			print(j)
			print(roman_num(num - i))
			return j + roman_num(num - i)
		
	return ""




