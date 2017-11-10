def convertToBinary(string):
	ans=[]
	for letter in string:
		if letter=='A':
			ans+=[0,0]
		elif letter=='T':
			ans+=[1,1]
		elif letter=='G':
			ans+=[0,1]
		else:
			ans+=[1,0]
	return ans

def convertNumberToRule(number):
	'''This turns a number from 0 to 256 to a list of 0's and 1's.'''
	ans=[0,0,0,0,0,0,0,0] 
	for i in range(8):
		digit=number%2 # even or odd
		ans[7-i]=digit # save answer to even or odd
		number=int(number/2) # deal with smaller number
	return ans

def convertThreeToDecimal(threelist):
	return 4*threelist[0]+2*threelist[1]+1*threelist[2]

def applyRule(number, binaryList): #binarylist is what I will be seeing 
	# This function should do the following:
	#applyRule(120, [1,1,1,0,1,0,0,1,0,0,0,0,1])
	#[0,1,0,1,1,0,1,0,0,1,0,0,0]
	#applyRule(0, [1,1,0,0])
	#[0,0,0,0]
	new_binary_list = []
	rule = convertNumberToRule(number)
	binaryList = [0,0] + binaryList

	for i in range(0,len(binaryList)-2):
		triples = binaryList[i:i+3]
		#print(triples)
		answer = convertThreeToDecimal(triples)
		new_binary_list.append(rule[7-answer])
		
	return new_binary_list
		#Rule 120 
		# if binaryList[i] == 0:
		# 	if binaryList[i+1] == 0:
		# 		new_binary_list.append(0)
		# 	elif binaryList[i+1] == 1:
		# 		new_binary_list.append(1)
		# elif binaryList[i] == 1:
		# 	if binaryList[i+1] == 1 and binaryList[i+2] == 1:
		# 		new_binary_list.append(0)
		# 	else:
		# 		new_binary_list.append(1)

def main():
	print(applyRule(120, [1,1,1,0,1,0,0,1,0,0,0,0,1]))
	print(applyRule(0, [1,1,1,0,1,0,0,1,0,0,0,0,1]))
	print(applyRule(255, [1,1,1,0,1,0,0,1,0,0,0,0,1]))
	

main()



