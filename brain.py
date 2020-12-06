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

    hiddenLayer = [1,0,1]

    numHidden = 3

    numOut = 3 # change in angle, and speed, and turn speed    

    steps = 10   

    stepNumber = 0

    mutationRate = .5 # the mutation increments

    confidence = 10 # the current weights get multiplied by this before averaging with mutated weights
    


    def __init__(self):
        self.logicSequence = np.random.random_sample((self.steps, self.numHidden, self.numIn)) 
        self.hiddenWeights = np.random.random_sample((self.numHidden, self.numHidden))
        self.outputWeights = np.random.random_sample((self.numHidden, self.numOut))


    # returns the next steo that a bot will take based on the logic sequence
    def step(self, inputs):

        if self.stepNumber == self.steps:
            self.stepNumber = 0

        output = [0,0,0]

        self.hiddenLayer[0] = np.around(np.tanh((np.dot(inputs, self.logicSequence[self.stepNumber][0])/self.numIn)+(np.dot(self.hiddenLayer, self.hiddenWeights[0])/self.numHidden)), 3 )
        self.hiddenLayer[1] = np.around(np.tanh((np.dot(inputs, self.logicSequence[self.stepNumber][1])/self.numIn)+(np.dot(self.hiddenLayer, self.hiddenWeights[1])/self.numHidden)), 3)
        self.hiddenLayer[2] = np.around(np.tanh((np.dot(inputs, self.logicSequence[self.stepNumber][2])/self.numIn)+(np.dot(self.hiddenLayer, self.hiddenWeights[2])/self.numHidden)), 3)
        output[0] = 2**(1+np.dot(self.hiddenLayer, self.outputWeights[0])*100/self.numHidden)
        output[1] = 2*(np.tanh(np.dot(self.hiddenLayer, self.outputWeights[1])*100/self.numHidden))
        output[2] = (1/(1+np.exp(np.dot(self.hiddenLayer, self.outputWeights[2])*100/self.numHidden)))

        self.stepNumber += 1

        return output 

    # generates a mutated versimon of the logic sequence
    def mutateRandom(self):
        self.logicSequence =  (self.logicSequence * self.confidence + ( np.random.random_sample((self.steps, self.numOut, self.numIn))-.5)) / (self.confidence + 1) 
        self.hiddenWeights =  (self.hiddenWeights * self.confidence + ( np.random.random_sample((self.numHidden, self.numHidden))-.5)) / (self.confidence + 1) 
        self.outputWeights =  (self.outputWeights * self.confidence + ( np.random.random_sample((self.numHidden, self.numOut))-.5)) / (self.confidence + 1) 



    # this is used to get the average logic of all the winning bots
    def avgLogic(self, group):
        scoreSum = 0

        for i in group:
            scoreSum += i.score
        for i in group:
            self.logicSequence += ((i.logic.logicSequence * i.score) / scoreSum)
            self.hiddenWeights += ((i.logic.hiddenWeights * i.score) / scoreSum)
            self.outputWeights += ((i.logic.outputWeights * i.score) / scoreSum)
            