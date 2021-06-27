
import cv2

class Palma():
    def __init__(self):
        palma_cascade = cv2.CascadeClassifier('palma.xml')
        cap = cv2.VideoCapture(0)

        while( True ):
            _, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            palma = palma_cascade.detectMultiScale(gray, 1.1, 10)

            for (x, y, w, h) in palma:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
                cv2.putText(img, 'Palma', (x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 0, 0), 3)

            cv2.imshow('camara', img)

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        cap.release()