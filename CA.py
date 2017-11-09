# import pyglet

# class Window(pyglet.window.window):
# 	def__init__(self):
# 		super(window,self).__init__()
# 		self.set_size(480,480)

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

def applyRule(number, binaryList):
    #binarylist is what I will be seeing
	# This function should do the following:
	#applyRule(120, [1,1,1,0,1,0,0,1,0,0,0,0,1])
	#[0,1,0,1,1,0,1,0,0,1,0,0,0]
	#applyRule(0, [1,1,0,0])
	#[0,0,0,0]
	
	# if number in convertNumberToRule(number) == 0:
	# 		new_binary_list = 0
	# elif number in convertNumberToRule(number) == 255:
	# 		new_binary_list = 1
	# else:
    ans=[]
    rule=convertNumberToRule(number)
    newBinaryList=[0,0]+binaryList
    #print(newBinaryList)
    for x in range(len(binaryList)):
        segment=newBinaryList[x:x+3]
        rulenumber=convertThreeToDecimal(segment)
        #print(x,segment,rule[rulenumber])
        ans.append(rule[7-rulenumber])
    return ans


def main():
    #print(convertNumberToRule(120))
    #print(len([1,1,1,0,1,0,0,1,0,0,0,0,1]))
    x=applyRule(120, [1,1,1,0,1,0,0,1,0,0,0,0,1])
    #print(len(x))
    print(x)
    x=applyRule(0, [1,1,1,0,1,0,0,1,0,0,0,0,1])
    print(x)
    x=applyRule(255, [1,1,1,0,1,0,0,1,0,0,0,0,1])
    print(x)


main()







