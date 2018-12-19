import MotorOperation
import TraceControl
import time
import view
import cv2

ts = 3
time.sleep(5)

while (1):
    pos = view.recog()
    key = cv2.waitKey(30) & 0xff
    if key == 27:
            break
    #print(pos[0],pos[1],pos[2],pos[3])
    #print(type(pos))
    para = view.trans(pos[0],pos[1],pos[2],pos[3])
    velosity = TraceControl.velcontrol(para[0],para[2])
    vel = TraceControl.driven(velosity)
    MotorOperation.motor(ts,vel[0],vel[1],vel[2],vel[3])
    print('velosity:\t'+str(vel[0])+'\t'+str(vel[1])+'\t'+str(vel[2])+'\t'+str(vel[3])+'\n')
view.cam.release()
cv2.destroyAllWindows()
    

