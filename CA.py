

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
		number=number/2 # deal with smaller number
	return ans

def convertThreeToDecimal(threelist):
	
	return 4*threelist[0]+2*threelist[1]+1*threelist[2]

def applyRule(number, binaryList):
	rule_str = format(rule, '#010b') [2:] #github.com #Choate library

	rule = {
        (2, 2, 2): int(rule_str[0]) + 1,
        (2, 2, 1): int(rule_str[1]) + 1,
        (2, 1, 2): int(rule_str[2]) + 1,
        (2, 1, 1): int(rule_str[3]) + 1,
        (1, 2, 2): int(rule_str[4]) + 1,
        (1, 2, 1): int(rule_str[5]) + 1,
        (1, 1, 2): int(rule_str[6]) + 1,
        (1, 1, 1): int(rule_str[7]) + 1
    }

	return rule
