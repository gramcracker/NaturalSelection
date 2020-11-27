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

    mutationRate = .7

    confidence = 2
    


    def __init__(self):
        self.logicSequence = np.random.random_sample((self.steps, self.hiddenLayer, self.numIn))
        # self.hiddenweights = np.random.random_sample((self.steps, self.hiddenLayer, self.numIn))
        # self.outWights = np.random.random_sample((self.steps, self.numOut, self.hiddenLayer ))



    def step(self, inputs):

        if self.stepNumber == self.steps:
            self.stepNumber = 0

        output = [1,0,1]
        
        output[0] = 1/(1+np.exp(np.dot(inputs, self.logicSequence[self.stepNumber][0]/self.numIn)))
        output[1] = np.tanh(np.dot(inputs, self.logicSequence[self.stepNumber][1])/self.numIn)
        output[2] = abs(np.dot(inputs, self.logicSequence[self.stepNumber][2]/self.numIn))
        #  (self.logicSequence)
        #  (inputs)
        #  (output)
        self.stepNumber += 1
        return output 

    def mutateRandom(self):
        self.logicSequence =  (self.logicSequence * self.confidence + (self.mutationRate * np.random.random_sample((self.steps, self.numOut, self.numIn)))) / (self.confidence + 1) 

    def avgLogic(self, group):
        scoreSum = 0

        for i in group:
            scoreSum += i.score
        for i in group:
            self.logicSequence += ((i.logic.logicSequence * i.score) / scoreSum)
            