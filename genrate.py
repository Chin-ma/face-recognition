import cv2
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

cam = cv2.VideoCapture(0)
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
			

id = input('Enter id: ')
name = input('Enter name: ')
email = input('Enter email: ')
insertOrUpdate(id, name, email)
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