# 8x8 pong
# https://wiki.57north.org.uk/index.php/Projects:LED_Ping_Pong_Pong
# https://docs.python.org/3/tutorial/inputoutput.html
#
#
#grid_height = 8
#grid_width = 8
import os
import time

pixels = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

direction_of_travel = "ne"

def print_screen():
  print("----------Pong-----------")
  #print(grid_height)
  for pixel_row in pixels:
    for pixel in pixel_row:
      #s += elem
      print(" ", pixel, end = '')
    print(" ")

print_screen()

pixels[1][1] = 2

#pixels = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1]]
print_screen()


print("hello1")

#os.system("clear")

print("hello2")

loops = 0
while loops < 10:
    #print(loops)
    pixels[1][1] = loops

    #for pixel_row in pixels:
    #  for pixel in pixel_row:
    #    pixel = 3

    os.system("clear")
    print_screen()
    
    # increment the loop variable
    loops += 1

    # have a wee sleep
    time.sleep(0.2)
