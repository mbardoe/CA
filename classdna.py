class DNA:
	def__init__(self,nucleotides)
		self.nucleotides = nucleotides
		self.isoperating = True

	def convertToBinary(self,string):
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

	def SetNucleotides(self,nucleotides):
		#just taking in a string and it just whatever i put in becomes self.nucleotides

	def SetNucleotidesFromBinary():
		#it would convert a binary string back to letters and put that as the set of nucleotides