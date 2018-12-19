import cv2
import TraceControl

mouse_haar = cv2.CascadeClassifier("data/cascade.xml")
cam = cv2.VideoCapture(0)

def recog():
        _, img = cam.read()
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mouse = mouse_haar.detectMultiScale(gray_img, 1.2, 20)
        #print(mouse[0],mouse[1])
        #print(type(mouse))
        #print(mouse)
        if mouse is ():
                x = TraceControl.pic_wid * 0.5
                y = TraceControl.pic_len * 0.5
                w = 100
                h = 100
        else:
                for mouse_x,mouse_y,mouse_w,mouse_h in mouse:
                        print(mouse_x,mouse_y,mouse_w,mouse_h)
                        x = mouse_x
                        y = mouse_y
                        w = mouse_w
                        h = mouse_h
                        cv2.rectangle(img, (mouse_x, mouse_y), (mouse_x+mouse_w, mouse_y+mouse_h), (0,255,0), 2)
        cv2.imshow('img', img)
        return [x,y,w,h]

def trans(x,y,w,h):
        center_x = x + w/2
        center_y = y + h/2
        radius = (w+h)/2
        return [center_x,center_y,radius]

if __name__=='__main__':
        while True:
                recog()


