#find occurance of character in a string 
#result shoulb in a order how they comes.
#ex: aaabbc 	result=a3b2c

#SolutionL
def CountOccurance(S):
	"""
	arg : Funciton takes input as a string
	return: returns the occurance of char in a string in order how they comes
	"""
	#initilizing dict to store char and number of occurance
	chars = {}
	for c in S:
		#it will check for char in dict, if it is exists then +1 count else 0
		if c not in chars:
			chars[c] = 0
		
		chars[c] += 1
	
	#empty string to store the char and occurances
	result = ""
	#we need in order how it was originally
	for c in S:
		if c in chars:
			#if char exists in String then it will add value to the result string.
			result += c+str(chars.pop(c))
	return result
S = input("Enter Here: ")
out = CountOccurance(S)
print(out)

#T = int(input())
#for i in range(T):
#	S = input()
#	out = CountOccurance(S)
#	print(out)
