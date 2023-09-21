'''
Jebish Purbey
Task 2 - Color detection in an image
'''

#First of all import all the required libraries
#We will be using opencv for the detection task

import numpy as np
import pandas as pd
import cv2


#Let's read the image in "img" using opencv
img=cv2.imread('test_1.jpg')

#Let's read the colors available in colors.csv file, which is taken from 'color-names' repo by codebrainz
titles=['color_id','color','HEX','R','G','B']
data_frame=pd.read_csv('colors.csv',names=titles)

#Setting up the variables for use when opencv window is initiated
clicked=False
r=g=b=xpos=ypos=0


#Let's define a function to get the current position of curson when double clicked. The function should set the global variables clicked to True (because the event is triggered), x pos and y pos to current cursor values and b,g,r to the image b,g,r values at the current cursor position
def current_pos(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global clicked,r,g,b,xpos,ypos
        clicked=True
        xpos=x
        ypos=y
        b,g,r=img[y,x]


#Let's setup another function that will take the r,g,b values that was setup above and then return a color name by matching it with the r,g,b values present in data_frame (containing colors.csv).
def color_name(color):
    distance=np.sum((data_frame[['R','G','B']]-color)**2,axis=1)
    color_index=np.argmin(distance)
    colorName=data_frame.color[color_index]
    return colorName



#Let's setup the window name and also callback for mouse that is required.
cv2.namedWindow('COLOR DETECTOR')
cv2.setMouseCallback('COLOR DETECTOR',current_pos)

#The following loop will run till escape key is pressed. We use openCV rectangle and text function to print out the name of color when the user double click on any location within the image
while(True):
    cv2.imshow('COLOR DETECTOR',img)
    if (clicked):
        cv2.rectangle(img,(20,20),(400,60),color=(int(b),int(g),int(r)),thickness=-1)
        text=color_name(np.array([r,g,b]))
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),6,cv2.LINE_AA)
        cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        

        clicked=False
    
    if cv2.waitKey(15) & 0xFF==27:
        break

#destroy instances of all opened windows
cv2.destroyAllWindows()

'''
The END
'''

