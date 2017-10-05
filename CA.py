

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
	ans=[0,0,0,0,0,0,0,0]
	for i in range(8):
		digit=number%2
		ans[7-i]=digit
		number=number/2
	return ans

def convertThreeToDecimal(threelist):
	return 4*threelist[0]+2*threelist[1]+threelist[2]

def applyRule(number, binaryList):
	##
	ans=[]

