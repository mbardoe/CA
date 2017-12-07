class CellularAutomata:
	def__init(self,state,rule,history):
		self.state = state
		self.rule = rule
		self.history = history

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