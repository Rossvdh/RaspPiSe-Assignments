# Implementing Snake game on SenseHat
# UCT Computer Science CSC4000W RaspPiSe project
# Ross van der Heyde
# 2 July 2018

# REVISED ASSIGNMENT

import sense_hat
import time
import random
import SnakeClass

#define some colours
blue = [0,0,255]
red = [255,0,0]
green = [0,255,0]
blank = [0,0,0]

# direction constants
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def up(event):
    """When the joystick is pushed up, change the snake's direction
    of movement to upwards"""
    if event.action == sense_hat.ACTION_RELEASED:
        snake.changeDirection(UP)

def down(event):
    """When the joystick is pushed down, change the snake's direction
    of movement to downwards"""
    if event.action == sense_hat.ACTION_RELEASED:
        snake.changeDirection(DOWN)
        
def right(event):
    """When the joystick is pushed right, change the snake's direction
    of movement to the right"""
    if event.action == sense_hat.ACTION_RELEASED:
        snake.changeDirection(RIGHT)

def left(event):
    """When the joystick is pushed left, change the snake's direction
    of movement to the left"""
    if event.action == sense_hat.ACTION_RELEASED:
        snake.changeDirection(LEFT)

def stopGame(event):
    """When the middle joystick button is pressed, stop the game"""
    if event.action == sense_hat.ACTION_RELEASED:
        global playAgain, alive
        playAgain = False
        alive = False

def generateFood():
    """Places the food (target LED) on a random LED in the matrix
    that is not in the snake"""
    temp = [random.randint(0,7), random.randint(0,7)]

    snakePixels = snake.getPixels()

    #check that the food does not fall in the snake
    while temp in snakePixels:
        temp = [random.randint(0,7), random.randint(0,7)]

    return temp

def updateMatrix(food, snake):
    """Draws the snake and food in the new positions on the LED matrix"""
    sense.clear()
    # draw food
    sense.set_pixel(food[0], food[1], green)
    
    # draw snake
    snakePixels = snake.getPixels()
    for pixel in snakePixels:
        if 0 <= pixel[0] <= 7 and 0 <= pixel[1] <= 7:
            sense.set_pixel(pixel[0], pixel[1], blue)
        else:
            die()
            return

    # blink snake's head
    for i in range(2):
        x = snake.head()[0]
        y = snake.head()[1]
        sense.set_pixel(x, y, blank)
        time.sleep(0.1)
        sense.set_pixel(x, y, blue)
        time.sleep(0.1)

    


def die():
    """When the snake dies by going off the grid or into itself"""
    global alive
    alive = False
    sense.show_message("You died", text_colour=[255,51,0])
##    sense.show_message("Final length: "+ str(snake.getLength()))

#MAIN
#set up the senseHat stuff
sense = sense_hat.SenseHat()
sense.stick.direction_down = down
sense.stick.direction_up = up
sense.stick.direction_left = left
sense.stick.direction_right = right
sense.stick.direction_middle = stopGame


playAgain = True #we want to play again after dying

while playAgain:
    snake = SnakeClass.SnakeClass()
    alive = True

    #countdown
    sense.show_letter("3")
    time.sleep(1)
    sense.show_letter("2")
    time.sleep(1)
    sense.show_letter("1")
    time.sleep(1)
    
    food = generateFood()

    #start game play
    while alive: #while snake is alive, keep moving and updating the matrix
        updateMatrix(food, snake)
        result = snake.slither(food)
        if result == "eat":
            print("eat")
            food = generateFood()
        elif result == "die":
            print("die")
            die()

    

sense.clear()
print("end")


























###
