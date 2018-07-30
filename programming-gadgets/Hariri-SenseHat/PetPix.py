#Pet Avatar

from sense_hat import SenseHat
import time

sense = SenseHat()

p=(204,0,204) #Pink
g=(0,102,102) #Green
w=(200,200,200) #White
y=(204,204,0) #Yellow
e=(0,0,0) #Empty

#set up where each colour will display foe rach image
pet1= [
    e,e,e,e,e,e,e,e,
    p,e,e,e,e,e,e,e,
    e,p,e,e,p,e,p,e,
    e,p,g,g,p,y,y,e,
    e,g,g,g,y,w,y,g,
    e,g,g,g,g,y,y,e,
    e,g,e,g,e,g,e,e,
    e,e,e,e,e,e,e,e,
    ]

pet2= [
    e,e,e,e,e,e,e,e,
    p,e,e,e,e,e,e,e,
    e,p,e,e,p,e,p,e,
    e,p,g,g,p,y,y,e,
    e,g,g,g,y,w,y,g,
    e,g,g,g,g,y,y,e,
    e,e,g,e,g,e,e,e,
    e,e,e,e,e,e,e,e,
    ]
#repeat this two image for 10 times
for i in range(10):
    sense.set_pixels(pet1)
    time.sleep(0.5)
    sense.set_pixels(pet2)
    time.sleep(0.5)
    
    sense.clear()
    
