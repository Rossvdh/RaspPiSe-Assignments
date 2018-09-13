# Tic tac Toe Revisited: adding a computer player
# Ross van der Heyde VHYROS001
# Univeristy of Cape Town Computer Science Honours CSC4000W
# 1 August 2018

import random, time
import sense_hat
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import ttt


# colour is the colour to make the square. array of 3 values bewteen 0 and 255
# corresponding to red, green and blue
# row and col are the co-ords of the LED in the top left corner of the ttt
# grid square
def colourSquare(colour, col, row):
    row = int(row)#row and col might be floats
    col = int(col)
    sense.set_pixel(col, row, colour)
    sense.set_pixel(col+1, row, colour)
    sense.set_pixel(col, row+1, colour)
    sense.set_pixel(col+1, row+1, colour)

def pushed_up(event):
    """What happens when the joystick is pushed up. The marker moves up
    to the next square"""
    if event.action == ACTION_RELEASED:
        # set previous marker pixel to correct square colour
        sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
        
        #move marker to next square
        marker[1] = (marker[1] - 3) % 9
        #set marker pixel to blue
        sense.set_pixel(marker[0], marker[1], blue)

def pushed_down(event):
    """What happens when the joystick is pushed up. The marker moves 
    down to square below the current one"""
    if event.action == ACTION_RELEASED:
        sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
        marker[1] = (marker[1] + 3) % 9
        sense.set_pixel(marker[0], marker[1], blue)

def pushed_left(event):
    """What happens when the joystick is pushed up. The marker moves to
    the square left of the current one"""
    if event.action == ACTION_RELEASED:
        sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
        marker[0] = (marker[0] - 3) % 9
        sense.set_pixel(marker[0], marker[1], blue)

def pushed_right(event):
    """What happens when the joystick is pushed up. The marker moves to
    the square right of the current one"""
    if event.action == ACTION_RELEASED:
        sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
        marker[0] = (marker[0] + 3) % 9
        sense.set_pixel(marker[0], marker[1], blue)

def buttonPushed(event):
    """What happens when the middle joystick button is pushed. The board
    variable is updated and the square is coloured with the
    appropriate colour"""
    # update board matrix
    #draw board on LEDs
    global redTurn
    if event.action == ACTION_RELEASED:
        #print("redTurn: ",redTurn,"x:", red,"marker[0]:",marker[0], ". marker[1]:",marker[1])

        if sense.get_pixel(marker[0], marker[1]+1) == [0,0,0]:
            if redTurn:
                board[marker[1]//3][marker[0]//3] = red
            else:
                board[marker[1]//3][marker[0]//3] = green
                
            redTurn = not redTurn
            drawBoard(board)

            result = ttt.checkForWinner(board)
            if result == "red":
                sense.show_message("Red wins")
                playAgain()
            elif result == "green":
                sense.show_message("Green wins")
                playAgain()
            elif result == "tie":
                sense.show_message("Tie")
                playAgain()
            else:
                computerPlay()

def shuffle(lst): #seems ok
    """Shuffles to array of moves and their scores"""
    for i in range(len(lst)-1, 0, -1):
        rand = random.randint(0, i)
        lst[i], lst[rand] = lst[rand], lst[i]
    return lst

def playAgain():
    """Restarts the game"""
    global board, redTurn
    time.sleep(0.5)
    redTurn = True
    sense.set_pixels(grid)
    sense.set_pixel(marker[0], marker[1], blue)

    #reset board
    board = [[red, blank, blank],
    [blank, green, blank],
    [blank, blank, blank]]

    drawBoard(board)

"""Draws the board on the LED matrix"""
def drawBoard(board):
    for row in range(3):
        for col in range(3):
            colourSquare(board[col][row], row*3, col*3)

def copyBoard(board): #seems ok
    """Creates a copy of the given board"""
    copy = []
    for row in board:
        newRow = []
        for col in row:
            newRow.append(list(col))
        copy.append(newRow)

    return copy

def getAvailableMoves(board): #seems ok
    """"Returns a list of blank grid sqaures"""
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == blank:
                moves.append((row, col))

    return moves


def getPlayMove(moves):
    """Returns the best move from the given dict[move]=score
    where move is a 2-tuple (row, col). Best move is the one with the highest
    score. If there are multiple moves with the same highest score, one is
    chosen randomly."""
    

def getBestMove(board, colour):
    """Returns the best move ((row, col), score) for the given colour on the given board"""
    moves = getAvailableMoves(board)
    movesAndScores = {}

    if len(moves) == 1:#only one available move,
    #so return immediately (this is the base case)
        #create a copy of the board
        copy = copyBoard(board)

        #apply an available move to the board
        copy[moves[0][0]][moves[0][1]] = colour

        #see what happens
        result = ttt.checkForWinner(copy)

        if result == "red" or result == "green":
            movesAndScores[moves[0]] = 10
            return (moves[0], 10)
        else:
            movesAndScores[moves[0]] = 0
            return (moves[0], 0)

    for move in moves:
        #create a copy of the board
        copy = copyBoard(board)

        #apply an available move to the board
        copy[move[0]][move[1]] = colour

        #see what happens
        result = ttt.checkForWinner(copy)
        score = 0
        if result == "red" or result == "green":
            score = 10
            return (move, 10)
        elif result == "tie":
            score = 1
        else:
            #result is "none", no winner or tie yet
            otherColour = green if colour == red else red

            #recursive call on new board, with other colour, to find best
            #move for user
            temp = getBestMove(copy, otherColour)
            score = temp[1] * -1

        if move in movesAndScores:
            movesAndScores[move] += score
        else:
            movesAndScores[move] = score

    lst = list(movesAndScores.items()) # list is [((row, col), score), ..]

    #shuffle
    #lst = shuffle(lst)

    #sort descending on score(scaffold) 
    lst.sort(key=(lambda i : i[1]), reverse=True)
    
    return lst[0]
          

"""Performs the computer's move"""
def computerPlay():
    global redTurn

    colour = red if redTurn else green
    
    move = getBestMove(board, colour)

    board[move[0][0]][move[0][1]] = colour
    drawBoard(board)

    #computer has made its move, so flip turn
    redTurn = not redTurn

    result = ttt.checkForWinner(board)
    if result == "red":
        sense.show_message("Red wins")
        playAgain()
    elif result == "green":
        sense.show_message("Green wins")
        playAgain()
    elif result == "tie":
        sense.show_message("Tie")
        playAgain()
    #else:
        #wait for joystick event

# MAIN-------------------------------------------------
if __name__ == "__main__":
    # set up sense hat
    sense = sense_hat.SenseHat()
    sense.low_light = True
    #sense.set_rotation(180)

    #set functions for joystick buttons
    sense.stick.direction_up = pushed_up
    sense.stick.direction_down = pushed_down
    sense.stick.direction_left = pushed_left
    sense.stick.direction_right = pushed_right
    sense.stick.direction_middle = buttonPushed
    #~ sense.stick.direction_any = checkWinner

    #define some colours
    red = [255,0,0]
    green = [0,255,0]
    blue = [0,0,255]
    blank = [0,0,0]
    white = [255,255,255]

    # define the empty Tic Tac Toe grid
    grid=[blank,blank,white,blank,blank,white,blank,blank,
      blank,blank,white,blank,blank,white,blank,blank,
      white,white,white,white,white,white,white,white,
      blank,blank,white,blank,blank,white,blank,blank,
      blank,blank,white,blank,blank,white,blank,blank,
      white,white,white,white,white,white,white,white,
      blank,blank,white,blank,blank,white,blank,blank,
      blank,blank,white,blank,blank,white,blank,blank]

    # matrix representing the TTT grid
    board = [[red, blank, blank],
       [blank, green, blank],
       [blank, blank, blank]]


    #sense.show_message("Get ready!")
    # set grid
    sense.set_pixels(grid)
    drawBoard(board)

    # set position marker to top left corner
    marker=[0,0]
    sense.set_pixel(marker[0], marker[1], blue)

    #red (user) plays first
    redTurn = True

    print("about to pause")
    pause() #stop execution and wait for event


















#
