This is to give an idea of the steps the porgram will take. The actual program will vary because of class definitions,  and general syntax of python.

# Initialize variables
* timer
* load 2 png files for 2 types of bots
* set number of bots on a team
* load genome for bot class (just a series of weights from previous runs)

# define wall class
* define wall.init
* define wall.update
* define wall.display
    * randomize position

# define bot class
* define bot.init
* define bot.update
    * (bulk of the logic lives here)
    * may add a separate pseudocode file for the bot's update code
* define bot.display
    * randomize position

# Main Loop
* ## create environment
    * for each wall 
        * wall.init
    * 2x for each bot:
        * bot.init(green or red)

* ## start timer

* ## update everything
    * wall.update
    * for each bot
        * bot.update
    * timer +=1

* ## display everything
* ## restart loop