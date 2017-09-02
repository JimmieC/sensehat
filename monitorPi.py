from sense_hat import SenseHat
import time
import random
import psutil

s = SenseHat()
s.low_light = False;

coreValues = [25,54,77,43]
diskValue = 0
ramValue = 0


#core value
def cv():
  global coreValues
  for i in range(0,1):
	coreValues = psutil.cpu_percent(interval=1, percpu=True)  	

def dv():
  global diskValue
  diskValue = psutil.disk_usage('/').percent
  
def rv():
  global ramValue
  ramValue = psutil.virtual_memory().percent
  print ramValue

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
  coreValue = coreValues[0]
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
    cv()
    dv()
    rv()
    time.sleep(2)
