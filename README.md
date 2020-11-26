# NaturalSelection
An Evolutionary simulator where two teams compete to evolve.

## How it works
There are two teams with an equal amount of either red or green "bots". Each team takes turns trying to kill the other team. Each turn is a session lasting 5 seconds. At the end of each session, random mutations will occur to the team with less bots. When only one team is left, the winning teams logic will be copied to the losing team. 

## Todo:
  - Use rect and collision detection
  - Kill function for bots
  - Add clock based delay.
  - Display info for timer, round number, and each teams current mode
  - Add walls
  - Probably add more documentation.
  - Implement DQN.
  - Possibly add a popup text box to explain the simulation
  
  
## prerequisites: 
As of now, pygame must be installed which is only supported up to python 3.8
A neural network framework will be used the future to utilize DQN.
