# 8x8 pong
# https://wiki.57north.org.uk/index.php/Projects:LED_Ping_Pong_Pong
# https://docs.python.org/3/tutorial/inputoutput.html
#
#
#grid_height = 8
#grid_width = 8
import os
import time
import getch
import random

left_paddle_x = 3
right_paddle_x = 3
frame = 0
ball_x = 4
ball_y = 4
ball_direction = "--"
game_state = 0
message = "TBC"

def print_screen():
  #os.system("clear")
  print("--Pong--")
  #print(grid_height)
  for pixel_row in pixels:
    for pixel in pixel_row:
      #s += elem
      if pixel == 0:
        pixel = " "
      #print(" ", pixel, end = '')
      print(pixel, end = '')
      # TODO: add logic to set the LEDs
    print(" ")
  print(" ")
  print("Debug:")
  print("frame: ", frame)
  print("ball_x: ", ball_x)
  print("ball_y: ", ball_y)
  print("left_paddle_x: ", left_paddle_x)
  print("right_paddle_x: ", right_paddle_x)
  print("ball_direction: ", ball_direction)
  print("ball_direction: ", ball_direction[0])
  print("ball_direction: ", ball_direction[1])

def left_paddle_up():
  global left_paddle_x
  pixels[left_paddle_x][0] = 0
  if left_paddle_x > 0:
    left_paddle_x -= 1
  pixels[left_paddle_x][0] = "|"
  
def left_paddle_down():
  global left_paddle_x
  pixels[left_paddle_x][0] = 0
  if left_paddle_x < 7:
    left_paddle_x += 1
  pixels[left_paddle_x][0] = "|"

def right_paddle_up():
  global right_paddle_x
  pixels[right_paddle_x][7] = 0
  if right_paddle_x > 0:
    right_paddle_x -= 1
  pixels[right_paddle_x][7] = "|"
  
def right_paddle_down():
  global right_paddle_x
  pixels[right_paddle_x][7] = 0
  if right_paddle_x < 7:
    right_paddle_x += 1
  pixels[right_paddle_x][7] = "|"

def move_ball():
  global ball_x
  global ball_y
  global ball_direction
  global pixels
  if ball_direction == "--":
    if bool( random.getrandbits(1) ):
      ball_direction = "se"
    else:
      ball_direction = "sw"

  #print("ball_direction: ", ball_direction)

  pixels[ball_x][ball_y] = 0

  if ball_direction[1] == "e":
    ball_y += 1
  if ball_direction[1] == "w":
    ball_y -= 1

  if ball_direction[0] == "n":
    ball_x -= 1
  if ball_direction[0] == "s":
    ball_x += 1

  if check_edge():
    pixels[ball_x][ball_y] = "o"


def check_edge():
  global ball_x
  global ball_y
  global ball_direction
  global pixels
  global game_state
  if (ball_y == 0):
    game_state = "r"
  elif (ball_y == 7):
    game_state = "l"
  
  if game_state:
    return 0
  else:
    return 1



def check_game_state():
  global pixels
  global game_state
  if game_state == "l":
    pixels = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,"l","e","f","t",0,0],[0,0,0,0,0,0,0,0],[0,0,"w","i","n","s",0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
  elif game_state == "r":
    pixels = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,"r","i","g","h","t",0],[0,0,0,0,0,0,0,0],[0,0,"w","i","n","s",0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]



pixels = [["-","-","-","X","X","X","X","X"],["X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X"]]
print_screen()
# have a wee sleep
time.sleep(1)

pixels = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
print_screen()
time.sleep(0.3)

# print 1
pixels = [[0,0,0,0,0,0,0,0],[0,"X","X","X","X","X","X",0],[0,0,0,0,"X",0,0,0],[0,0,0,"X","X",0,0,0],[0,0,0,0,0,"X",0,0],[0,0,0,0,0,0,"X",0],[0,"X","X","X","X","X",0,0],[0,0,0,0,0,0,0,0]]
print_screen()
time.sleep(0.3)

# print 2
pixels = [[0,0,0,0,0,0,0,0],[0,"X","X","X","X","X",0,0],[0,0,0,0,0,0,"X",0],[0,0,0,0,0,0,"X",0],[0,0,"X","X","X","X",0,0],[0,"X",0,0,0,0,0,0],[0,"X","X","X","X","X","X",0],[0,0,0,0,0,0,0,0]]
print_screen()
time.sleep(0.3)

# print 3
pixels = [[0,0,0,0,0,0,0,0],[0,0,0,"X","X",0,0,0],[0,0,"X","X","X",0,0,0],[0,0,0,"X","X",0,0,0],[0,0,0,"X","X",0,0,0],[0,0,0,"X","X",0,0,0],[0,0,"X","X","X","X",0,0],[0,0,0,0,0,0,0,0]]
print_screen()
time.sleep(0.3)

#direction_of_travel = "ne"



#print_screen()

#pixels[1][1] = 2

pixels = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],["|",0,0,0,0,0,0,"|"],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
print_screen()


#print("hello1")

#os.system("clear")

#print("hello2")


while frame < 20:
    #print(loops)
    #pixels[0][0] = frame

    #for pixel_row in pixels:
    #  for pixel in pixel_row:
    #    pixel = 3

    keypress1 = getch.getch()
    keypress2 = getch.getch()
    pixels[0][2] = keypress1
    pixels[0][4] = keypress2


    left_pressed = 0
    right_pressed = 0


    if keypress1 == "a" and left_pressed == 0:
      left_paddle_up()
      left_pressed = 1

    if keypress1 == "z" and left_pressed == 0:
      left_paddle_down()
      left_pressed = 1

    if keypress2 == "a" and left_pressed == 0:
      left_paddle_up()
      left_pressed = 1

    if keypress2 == "z" and left_pressed == 0:
      left_paddle_down()
      left_pressed = 1

    if keypress1 == "k" and right_pressed == 0:
      right_paddle_up()
      right_pressed = 1

    if keypress1 == "m" and right_pressed == 0:
      right_paddle_down()
      right_pressed = 1

    if keypress2 == "k" and right_pressed == 0:
      right_paddle_up()
      right_pressed = 1

    if keypress2 == "m" and right_pressed == 0:
      right_paddle_down()
      right_pressed = 1

    move_ball()

    

    #check_paddle_hit()

    #pixels[7][1] = left_paddle_x
    #pixels[7][6] = right_paddle_x

    check_game_state()

    print_screen()
    
    if game_state:
      quit()
    
    # increment the loop variable
    frame += 1

    # have a wee sleep
    time.sleep(1)
