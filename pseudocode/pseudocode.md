This is to give an idea of the steps the porgram will take. The actual program will vary because of class definitions,  and general syntax of python.

# Initialize variables
* start a pygame session
* window parameters
* load the data for the bots

# define function determines that who's turn it is and displays it with a timer

# define wall class
* define wall.init
* define wall.update
* define wall.display
    * randomize position

# define bot class
* define bot.init
* define collision functions
* define bot.update
    * detect collisions
    * move
* define bot.display
    * randomize position

# Main Loop
* ## create environment

* ## if q press quit

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

# exit pygame
# quit