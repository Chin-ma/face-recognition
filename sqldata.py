#!/usr/bin/python

from cv2 import CAP_V4L2
import numpy as np
import cv2, os
from PIL import Image
import pickle
import threading
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import time
from invoice import invoiceGenerate
from mailService import sendMail

run_once = 9
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer/trainingData.yml")
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
path = 'dataSet'
def getProfile(Id):
	try:
		conn = mysql.connector.connect(host='localhost', database='facebase', user='root', password='')
		cmd = "SELECT * FROM people WHERE Id="+str(Id)
		cursor = conn.cursor()
		cursor.execute(cmd)
		profile = None
		for row in cursor:
			profile = row
		conn.commit()
		cursor.close()
		return profile
	except mysql.connector.Error as error:
		print("Failed to display row {}".format(error))

cam = cv2.VideoCapture(2, CAP_V4L2)
# cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
if not cam.isOpened():
	cam.open(2)

font = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (0,255,255)
stroke = 2
while(True):
	ret, frame = cam.read()
	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		break

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceDetect.detectMultiScale(gray,1.3,5)
	for(x,y,w,h) in faces:
		Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
		# print(conf)
		# print(Id)
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),2)
			
		if (conf < 55):
			profile = getProfile(Id)
			if (profile!=None):
				cv2.putText(frame, "Name: " +str(profile[1]), (x,y+h+30), font, fontscale, fontcolor, stroke)
				# cv2.putText(frame, "Name: " +str(Id), (x,y+h+30), font, fontscale, fontcolor, stroke)
				person = str(profile[1])
				mailId = str(profile[2])
				invoiceGenerate(person)
				for i in range(10):
					run_once=i
					if run_once == 9:
						t1 = threading.Thread(target=sendMail(mailId))
						break
					
		else:
			cv2.putText(frame, "Unknown", (x,y+h+30), font, fontscale, fontcolor, stroke)

	cv2.imshow("frame", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break	

cam.release()
cv2.destroyAllWindows()

