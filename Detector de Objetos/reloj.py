
import cv2

class Reloj(): 
	def __init__(self):
		
			cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

			reloj = cv2.CascadeClassifier('reloj.xml')

			while True:
					
				ret,frame = cap.read()
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

				accesorio = reloj.detectMultiScale(gray,
				scaleFactor = 5,
				minNeighbors = 91,
				minSize=(40,40))

				for (x,y,w,h) in accesorio:
					cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
					cv2.putText(frame,'Reloj',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

				cv2.imshow('frame',frame)
					
				if cv2.waitKey(1) == 27:
					break
			cap.release()
			cv2.destroyAllWindows()	