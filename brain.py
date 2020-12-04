import random
import numpy as np

class logic():
 
    #this class defines a recurrent neural network that for 
    numIn = 8 #number of inputs
	#enemy angle
    #enemy X distance
	#enemy Y distance
    #detect wall angle
    #detect wall X distance
	#detect wall Y distance
    #get turn boolean
    #bias

    hiddenLayer = 3

    numOut = 3 # change in angle, and speed, and turn speed    

    steps = 50 

    stepNumber = 0

    mutationRate = .1 # the mutation increments

    confidence = 100 # the current weights get multiplied by this before averaging with mutated weights
    


    def __init__(self):
        self.logicSequence = np.random.random_sample((self.steps, self.hiddenLayer, self.numIn)) 

    # returns the next steo that a bot will take based on the logic sequence
    def step(self, inputs):

        if self.stepNumber == self.steps:
            self.stepNumber = 0

        output = [1,0,1]
        output[0] = 2**(1+np.dot(inputs, self.logicSequence[self.stepNumber][0])*100/self.numIn)
        output[1] = np.tanh(np.dot(inputs, self.logicSequence[self.stepNumber][1])*100/self.numIn)
        output[2] = 2**(1/(1+np.exp(np.dot(inputs, self.logicSequence[self.stepNumber][2])*100/self.numIn)))

        self.stepNumber += 1

        return output 

    # generates a mutated versimon of the logic sequence
    def mutateRandom(self):
        self.logicSequence =  (self.logicSequence * self.confidence + ( np.random.random_sample((self.steps, self.numOut, self.numIn))-.5)) / (self.confidence + 1) 

    # this is used to get the average logic of all the winning bots
    def avgLogic(self, group):
        scoreSum = 0

        for i in group:
            scoreSum += i.score
        for i in group:
            self.logicSequence += ((i.logic.logicSequence * i.score) / scoreSum)
            