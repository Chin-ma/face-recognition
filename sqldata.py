import numpy as np
import cv2, os
from PIL import Image
import pickle
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def recognition():
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	recognizer.read("C:\\Users\\chinm\\OneDrive\\Documents\\Major-Project-Third-Year\\New-Face-ecog\\recognizer\\trainingData.yml")
	faceDetect = cv2.CascadeClassifier('C:\\Users\\chinm\\OneDrive\\Documents\\Major-Project-Third-Year\\New-Face-ecog\\haarcascade_frontalface_default.xml')
	path = 'dataSet'
	def getProfile(Id):
		# conn = sqlite3.connect("C:\\Users\\chinm\\OneDrive\\Documents\\Major-Project-Third-Year\\New-Face-ecog\\FaceBase.db")
		# conn = mysql.connector.connect(host='localhost', database='facebase', user='root', password='')
		# cmd = "SELECT * FROM people"
		# cursor = conn.execute(cmd)
		# profile = None
		# for row in cursor:
		# 	profile = row
		# conn.close()
		# return profile
		try:
			conn = mysql.connector.connect(host='localhost', database='facebase', user='root', password='')
			cmd = "SELECT * FROM people"
			cursor = conn.cursor()
			cursor.execute(cmd)
			profile = None
			for row in cursor:
				profile = row
			conn.commit()
			cursor.close()
		except mysql.connector.Error as error:
			print("Failed to display row {}".format(error))
		return profile

	cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
	# cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
	if not cam.isOpened():
		cam.open(0)

	font = cv2.FONT_HERSHEY_SIMPLEX
	fontscale = 1
	fontcolor = (0,255,255)
	stroke = 2
	profiles = {}
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
			
			
			if (conf<50):
				if(Id==1):
					Id="Chinmay"
				elif(Id==2):
					Id=""
				elif(Id==3):
					Id=""
				elif(Id==4):
					Id="Elon"
				elif(Id==5):
					Id=""
				elif(Id==6):
					Id=""
				elif(Id==7):
					Id=""
				elif(Id==8):
					Id=""

			else:
				Id="Unknown"
			
			profile = getProfile(Id)
			if (profile!=None):
				# cv2.putText(frame, "Name: " +profile[1], (x,y+h+30), font, fontscale, fontcolor, stroke)
				cv2.putText(frame, "Name: " +str(Id), (x,y+h+30), font, fontscale, fontcolor, stroke)
		

		cv2.imshow("frame", frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break	

	cam.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	recognition()
