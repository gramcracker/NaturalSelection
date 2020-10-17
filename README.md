# NaturalSelection
An Evolutionary simulator where two teams compete to evolve.

## How it works
There are two teams with an equal amount of either red or green "bots". Each team takes turns trying to kill the other team. Each turn is a session lasting 15 seconds. At the end of each session, random mutations will occur to the team with less bots. When only one team is left, the winning teams logic will be copied to the losing team. 

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
as of now, pygame must be installed and some neural network framework in the future to utilize DQN.
