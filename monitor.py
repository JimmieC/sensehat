from sense_hat import SenseHat
import time
import random

s = SenseHat()
s.low_light = False;

coreValues = [25,54,77,43]
diskValue = 0
ramValue = 0

#random core values
def rcv():
  global coreValues
  for i in range(0,3):
    coreValues[i] = random.randint(1,101)
  print coreValues
  
def rdv():
  global diskValue
  diskValue = random.randint(50,71)
  
def rrv():
  global ramValue
  ramValue = random.randint(10, 101)

MED_LOAD = 66
LOW_LOAD = 33

green = (0, 255, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
orange = (255, 120, 0)
nothing = (0,0,0)

#Set Core Color
def scc(coreNum):
  coreValue = coreValues[coreNum]
  if coreValue < 33: return green
  if coreValue < 66: return yellow
  return red
  
#Set Disk Color
def sdc(level):
  if diskValue > level: return blue
  return nothing
  
#Set Ram Color
def src(level):
  if ramValue > level: return orange
  return nothing
  


white = (255,255,255)
pink = (255,105, 180)

def cores():
    O = white
    N = nothing
    logo = [
    scc(0), scc(0), scc(1), scc(1), N, sdc(100), src(100), src(100),
    scc(0), scc(0), scc(1), scc(1), N, sdc(87.5), src(87.5), src(87.5),
    scc(2), scc(2), scc(3), scc(3), N, sdc(75), src(75), src(75),
    scc(2), scc(2), scc(3), scc(3), N, sdc(62.5), src(62.5), src(62.5),
    O, O, O, O, N, sdc(50), src(50), src(50),
    O, O, O, O, N, sdc(37.5), src(37.5), src(37.5),
    O, O, O, O, N, sdc(25), src(25), src(25),
    O, O, O, O, N, sdc(12.5), src(12.5), src(12.5),
    ]
    return logo

while True: 
    s.set_pixels(cores())
    rcv()
    rdv()
    rrv()
    time.sleep(.75)