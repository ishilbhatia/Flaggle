import numpy as np
import cv2
import os
import random
z=os.scandir("h240")
flags=[]
black=np.zeros([240,611,3],'uint8')
for i in z:
    flags.append(i.name)
mynum=random.randint(0,len(flags))
myflag=flags[mynum]
myimg=str("h240/"+myflag)
myflag=myflag.replace(".png","")
#print (myflag)

img=cv2.imread(myimg)

h=img.shape[0]
w=img.shape[1]
for i in range(h):
    for j in range(w):
        for k in range(3):
            if img[i,j,k]>200:
                img[i,j,k]=255
            elif img[i,j,k]>130:
                img[i,j,k]=150
            elif img[i,j,k]>80:
                img[i,j,k]=100
            elif img[i,j,k]>50:
                img[i,j,k]=50
            elif img[i,j,k]>0:
                img[i,j,k]=0
black[0:h,0:w,::]=img[0:h,0:w,::]
'''def select(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(img[y,x])'''
cv2.namedWindow("Image")
#cv2.setMouseCallback("Image", select)
while True:
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
    a=input("Enter your guess ")
    guess=str("h240/"+a+".png")
    guessim=cv2.imread(guess)
    h1=guessim.shape[0]
    w1=guessim.shape[1]
    guessimg=np.zeros([240,611,3],'uint8')
    guessimg[0:h1,0:w1,::]=guessim[0:h1,0:w1,::]
    #guessimg.resize((h,w,3))
    cv2.imshow("Your Guess",guessimg)
    if a==myflag:
        print("Congrats! you guessed the flag!")
        break
    for i in range(h):
        for j in range(w):
            for k in range(3):
                if guessimg[i,j,k]>200:
                    guessimg[i,j,k]=255
                elif guessimg[i,j,k]>130:
                    guessimg[i,j,k]=150
                elif guessimg[i,j,k]>80:
                    guessimg[i,j,k]=100
                elif guessimg[i,j,k]>50:
                    guessimg[i,j,k]=50
                elif guessimg[i,j,k]>0:
                    guessimg[i,j,k]=0
    for i in range(h):
        for j in range(w):
            if guessimg[i,j,0]==img[i,j,0] and guessimg[i,j,1]==img[i,j,1] and guessimg[i,j,2]==img[i,j,2]:
                guessimg[i,j]=[100,255,0]
            else:
                guessimg[i,j]=[0,0,0]
    cv2.imshow("Actual Flag",guessimg)


print(myflag)
cv2.destroyAllWindows()
