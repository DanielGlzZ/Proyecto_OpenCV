
import cv2

class Muneca():
    def __init__(self):
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

        muneca = cv2.CascadeClassifier('muneca.xml')

        while True:
                
            ret,frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            accesorio = muneca.detectMultiScale(gray,
            scaleFactor = 6,
            minNeighbors = 95,
            minSize=(39,39))

            for (x,y,w,h) in accesorio:
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(frame,'Muneca',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

            cv2.imshow('frame',frame)
                
            if cv2.waitKey(1) == 27:
                break
        cap.release()
        cv2.destroyAllWindows()	
