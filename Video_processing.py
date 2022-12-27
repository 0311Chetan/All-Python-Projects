import cv2
import numpy as np

#Video Uploading

cap = cv2.VideoCapture("Users\Hp\Image processing\video.mp4")

min_Width=80
min_Height=80

count_line_pos = 600

#Intialize Substructor

algo = cv2.bgsegm.createBackgroundSubtractorMOG()

def Center(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx=x+x1
    cy=y+y1
    return cx,cy
    
detect = []

offset=6
counter=0

while True:
    ret,frame1=cap.read()
    grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(3,3),5)
    
    # Applying on each frame
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub,np.ones((5,5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada,cv2.MORPH_CLOSE,kernel)
    countershape,h=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    
    cv2.line(frame1,(25,count_line_pos),(1200,count_line_pos),(255,127,0),3)
    
    
    for (i,c) in enumerate(countershape):
        (x,y,w,h)=cv2.boundingRect(c)
        validate_count = (w >= min_Width) and (h>= min_Height)
        if not validate_count:
            continue
            
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        
        centre=Center(x,y,w,h)
        detect.append(centre)
        cv2.circle(frame1,centre,4,(0,0,255),-1)
        
        for (x,y) in detect:
            if y<(count_line_pos+offset) and y>(count_line_pos-offset):
                counter+=1
            cv2.line(frame1,(25,count_line_pos),(1200,count_line_pos),(0,127,255),3)
            detect.remove((x,y))
            print("Vechicle Counter:"+str(counter))
            
    cv2.putText(frame1,"Vechilce counter :"+str(counter),(450,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)
    
    
    #cv2.imshow("video Original",dilatada)
    cv2.imshow("video Original",frame1)
    
    if cv2.waitKey(1) == 13:
        break
        
cv2.destroyAllWindows()
cap.release()