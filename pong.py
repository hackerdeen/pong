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

def print_screen():
  print("--Pong--")
  #print(grid_height)
  for pixel_row in pixels:
    for pixel in pixel_row:
      #s += elem
      print(pixel, end = '')
    print("")

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
    os.system("clear")
    print_screen()
    pixels[1][1] = loops
    loops += 1
    time.sleep(0.2)
