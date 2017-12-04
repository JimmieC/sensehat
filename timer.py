from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def blink(interval):
  layer = interval / 10
  for i in range(0,8):
    if s.get_pixel(i, int(layer))[0] == 0:
      s.set_pixel(i, int(layer), 255,0,0)
    else:
      s.set_pixel(i, int(layer), 0,0,0)

def buildLogo(interval):
  logo = []
  for i in range(0,64):
    if(i < interval):
      logo.append(red)
    else:
      logo.append(nothing)
  return logo

def breakTime():
  logo = []
  for i in range(0,64):
    logo.append(yellow)
  s.set_pixels(logo)
  time.sleep(60 * 10)
  
def refresh():
    s.clear()
    
#s.stick.direction_any = refresh


count = 0
logo = buildLogo(40)
interval = 40
s.set_pixels(logo)
while True: 
    time.sleep(1)
    blink(interval)
    count += 1
    if count % 60 == 0:
      interval -= 8
      print interval
      if interval <= 0:
        interval = 40
        count = 0
        breakTime()
      s.set_pixels(buildLogo(interval))
    
    
