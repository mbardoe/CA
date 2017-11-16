#import matplotlib.pyplot as plt
import numpy as np
from time import sleep
# import pyglet

# class Window(pyglet.window.window):
# 	def__init__(self):
# 		super(window,self).__init__()
# 		self.set_size(480,480)

class CA(object):
    def __init__(self, number, DNA, memory=25):
        self.number=number
        self.rule=self.convertNumberToRule(self.number)
        self.memory=memory
        self.state=np.array([0,0]+self.convertToBinary(DNA))
        #plt.ion()
        #self.fig=plt.figure(1)
        self.setup_grid()

        #self.setup_graphics()

    def state(self, state):
        self.state=state

    def setup_graphics(self):

        self.axes=self.fig.add_subplot(111)


    def display_plot(self):
        plt.draw()

    def update_graphics(self):
        self.axes.pcolor(self.grid, cmap='binary')

    def setup_grid(self):
        self.grid=np.zeros((self.memory, len(self.state)))
        self.grid[0]=self.state
        self.gen=0

    def update_grid(self, newstate):
        if self.gen+1<self.memory:
            self.gen+=1
            self.grid[self.gen]=newstate
        else:
            self.gen+=1
            self.grid[0:self.memory-1]=self.grid[1:]
            self.grid[self.memory-1]=newstate

    def run(self):

        self.applyRule()
        #self.display_plot()
        sleep(.01)






    def convertToBinary(self, string):
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

    def convertNumberToRule(self, number):
        '''This turns a number from 0 to 256 to a list of 0's and 1's.'''
        ans=[0,0,0,0,0,0,0,0]
        for i in range(8):
            digit=number%2 # even or odd
            ans[7-i]=digit # save answer to even or odd
            number=int(number/2) # deal with smaller number
        return ans

    def convertThreeToDecimal(self, threelist):

        return 4*threelist[0]+2*threelist[1]+1*threelist[2]

    def applyRule(self,):
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

        #print(newBinaryList)
        for x in range(len(self.state)-2):
            segment=self.state[x:x+3]
            rulenumber=self.convertThreeToDecimal(segment)
            #print(x,segment,rule[rulenumber])
            ans.append(self.rule[7-rulenumber])
        self.state=ans+[0,0]
        self.update_grid(self.state)
        return self.state


def main():
    ca=CA(120, "ACTGTCATTTAA")
    ca.run()
main()







