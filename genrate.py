import cv2
from cv2 import CAP_V4L
from cv2 import CAP_V4L2
import mysql.connector
from tkinter import *
import tkinter as tk
from mysql.connector import Error
from mysql.connector import errorcode

cam = cv2.VideoCapture(2, CAP_V4L2)
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def insertOrUpdate(Id, Name, Email):
	# conn = sqlite3.connect("FaceBase.db")
	# conn = mysql.connector.connect(host='localhost', database='facebase', user='root', password='')
	# cmd = "SELECT COUNT(*) FROM people"
	# cursor = conn.cursor()
	# count = cursor.execute(cmd)
	# it=1
	# isRecordExist=0
	# for i in count:
	# 	# isRecordExist=1
	# 	# if (isRecordExist==1):
	# 	# 	cmd = "UPDATE people SET Name='"+(Name)+"', Email='"+(Email)+"' WHERE Id="+(Id)+""
	# 	# else:
	# 	cmd="INSERT INTO people(Id,Name,Email) VALUES("+(Id)+",'"+(Name)+"','"+(Email)+"')",it
	# 	cursor.execute(cmd)
	# conn.commit()
	# print(cursor.rowcount, "Row inserted")
	# cursor.close()
	# conn.close()
	try:
		conn = mysql.connector.connect(host='localhost', database='facebase', user='root', password='')
		cmd = "INSERT INTO people(Id,Name,Email) VALUES("+(Id)+",'"+(Name)+"','"+(Email)+"')"
		cursor = conn.cursor()
		cursor.execute(cmd)
		conn.commit()
		print(cursor.rowcount, "Record inserted")
		cursor.close()
	except mysql.connector.Error as error:
		print("Failed to insert row {}".format(error))
	finally:
		if (conn.is_connected()):
			conn.close()
			print("Mysql connection is closed")

# newWindow = Tk()
# newWindow.title("Add new face data")
# newWindow.geometry("400x400")
# i = tk.Label(newWindow, text="Id").grid(row=0, column=0)
# n = tk.Label(newWindow, text="Name").grid(row=1, column=0)
# e = tk.Label(newWindow, text="Email").grid(row=2, column=0)
# faceId = tk.Entry(newWindow).grid(row=0, column=1)
# faceName = tk.Entry(newWindow).grid(row=1, column=1)
# faceEmail = tk.Entry(newWindow).grid(row=2, column=1)
# insertOrUpdate(faceId, faceName, faceEmail)
# btn = tk.Button(newWindow, text="Add face", command=insertOrUpdate(faceId, faceName, faceEmail)).grid(row=3, column=0)
# btn = tk.Button(newWindow, text="Add face", command=).grid(row=3, column=0)
id = input("Enter id: ")
name = input("Enter name: ")
email = input("Enter email: ")
insertOrUpdate(id, name, email)
# mainloop()


sampleNum = 0
while(True):
	ret, frame = cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceDetect.detectMultiScale(gray,1.3,5)
	for(x,y,w,h) in faces:
		sampleNum = sampleNum + 1
		cv2.imwrite("dataSet/user."+id+'.'+ str(sampleNum) +".jpg",frame[y:y+h,x:x+w])
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),2)
		
	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()
