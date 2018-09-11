# RaspPiSe Assignments

The Raspberry Pi Sense HAT project (RaspPiSe) aims to engage and motivate students learning programming in Python at the University of Cape Town. The target students are Computer Science students in the CSC1010H course, and Physics students in the PHY1023H course. We aim to engage the CS students by replacing some of their traditional assignments with games that they would implement on the Raspberry Pi and Sense HAT. The Physics students will be performing experiments implementing code on the Raspberry Pi and SenseHAT for recording data from the sensors and then completing questions based on the experiments. We hope that the students will enjoy these practicals more than the traditional ones, and thus engage the content more, leading to improved programming skill.

This repo contains the assignments for use in the CSC1010H course, (or any introductory programming course that uses Python).

### Project webpage

The project webiste will be online soon. The literature review, proposal, and final report will be available on the website.

# The assignments

There are 4 assignments: tic-tac-toe, ball maze, snake, and tic-tac-toe revisited. Each assignment is meant to test a certain programming construct. Instructions to the student, scaffolding code, and a model answer are provided for all assignments.

## Tic-tac-toe

![tic-tac-toe screenshot](/tttScreenshot.png "Tic-tac-toe on the Sense HAT LED matrix. This screenshot created using a Sense HAT emulator")

The first assignment uses the game tic-tac-toe to provide the students with an
introduction to working with the RPi and SH. The game has been adapted to work on the
LED matrix by replacing the 'X's and 'O's used in the paper version of the game with
simple red or green squares. The user selects the square in the grid where they wish
to play by moving a marker LED with the joystick, and then pressing the middle
joystick button to make their mark. When a player has won or it is a tie, a suitable
message is displayed on the matrix.

This assignment tests the use of variables, lists, and functions (user-defined and
library functions).

The instructions to the student begin with a short explanation of the RPi and SH (what
they are, why they exist) and how to connect to the RPi via [VNC Viewer](https://www.realvnc.com/en/). VNC
Viewer is a piece of software that allows one to access another computer remotely, and
it allows one to see the GUI of the remote computer. VNC is being used because it is
not feasible to give each student a monitor, keyboard, and mouse along with the RPi,
but as each student has a laptop, which they can use to access the RPi's interface.
  
Then there is a brief explanation of how the game will be implemented and the
scaffolding code, and then instructions for what the student has to do are given.
There are three tasks for the student to complete: moving the marker LED around the
board, setting the LEDs in the board to the correct colour when the user presses the
middle joystick button, and making a new game start after the end of the current game.
As this is meant to be a simple introduction to working with the RPi and SH, the tasks
are simple.

## Ball Maze

![ball maze screenshot](/ballMazeScreenshot.png "An example ball maze on the Sense HAT LED matrix. This screenshot created using a Sense HAT emulator")

The next assignment is based on a ball maze (also called marble maze). A ball maze is
a handheld game where the goal is to get a small ball from one side of a box to
another by tilting the box to make the ball roll. There are walls that enforce the
maze and holes that the ball can fall into. This game provides an opportunity for
using the IMU, which is an input to the computer that students are unlikely to have seen
before.

The game has been adapted so that different coloured LEDs represent different parts of
the maze. The ball is an orange LED, the wall are blue, holes are red, and the end of
the maze is a green LED. The RPI continuously reads the IMU to obtain its orientation,
and depending on the values the ball "rolls" around the matrix. When the user wins
(the ball rolls to the end of the maze) or dies (rolls off the edge of the matrix or
into a hole), an appropriate message is displayed. The shortest time taken to complete
the maze successfully is stored in a text file

The maze layouts (positions of walls, holes, start and end points) are stored in a
text file, as this allows for several maze designs to be created and stored easily.
Again, scaffolding code is provided, created in the same way as in the tic-tac-toe
assignment. There are two functions in a module that provide for reading the maze
layouts, and writing the shortest time to complete the maze in a text file.

It is up to the student to read the IMU and move the ball around the LED matrix,
determine what type of move occurred (did the ball roll into a wall, or into a hole,
or off the edge, or onto the end-of-maze LED?), and then make sure that the ball
behaves accordingly or a suitable message is displayed to the user. The instructions
to the student also include a short tutorial concerning the IMU.

This assignment tests the use of lists, both one and two dimensional, if statements,
and boolean conditions. It can also be expanded to include file input and output
(requiring that the student writes the code for reading the maze layout and storing
the shortest time to complete the maze).

## Snake

![snake screenshot](/snakeScreenshot.png "Snake on the Sense HAT LED matrix. This screenshot created using a Sense HAT emulator")

The classic game snake has also been used as one of the assignments. The game needed
no adaptation in order to work on the LED matrix. The user controls the snake via the
joystick, aiming for a green LED which represents the "food." When the snake eats
the food, it grows one LED longer. If the snake goes off the edge of the LED matrix or
into itself, it dies.

This game was implemented using a class that represents the snake. The snake class is
list of the co-ordinates of the LEDs that make up the snake's body, and the direction in
which the LEDs
are moving. There are methods for changing the snake's direction of movement,
obtaining a list of the co-ordinates of the LED in the snake, and making the snake
move.

The scaffolding code creates an instance of the snake class, and provides several
functions that the student must complete to get the game working. The functions are:
displaying the snake and the food LED on the LED matrix, making the snake change
direction, generating a new random location for the food once it is eaten, making the
game end when the snake slithers into itself or off the edge of the LED matrix, and making
the game stop when the middle joystick button is pressed.

This assignment tests the use of for and while loops, and some simple object oriented-
programming principles.

## Tic-tac-toe Revisited

Based heavily on the first assignment, tic-tac-toe revisited adds functionality that
allows the user to play against the computer. The student must implement parts of the
code for the algorithm to complete the assignment.

The algorithm is a variant of the minimax algorithm. Each possible result of the game
is given a score: 10 for computer wins, -10 for computer loses, and 0 for a tie. If
there is no result yet, the move is also scored 0. The computer scans the board,
assigning each possible move a score, and selects the move that will maximise its
score and minimise its opponent's score. It does this by applying each possible move
for itself, then calling the function recursively with the new board to determine the
best move for the player. This continues until the game ends. If implemented
correctly, the computer will never lose a game[2](https://medium.freecodecamp.org/building-an-ai-algorithm-for-the-tic-tac-toe-challenge-29d4d5adee07). The algorithm is quite
slow, so the game starts with two moves already have been played.
It was chosen because it is a good way to introduce recursion to the
students.

There are four tasks that the student must complete: drawing the board on the LED
matrix after a player or the computer has made a move, implementing the code that
makes the computer play, obtaining a list of available places on the board where the
computer can play, and implementing the algorithm for determining the best place to
play.

The assignment instructions provide first a general overview of how the algorithm
works, and then more detailed instructions for the algorithm implementation.

This assignment introduces recursive functions, as well as reinforcing the other
content that has been covered before.


