import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataSet'
def getImagesWithId(path):
	imagePaths = [os.path.join(path, f) for f in os.listdir(path)] 
	print(imagePaths)
	faces = []
	Ids = []
	for imagePath in imagePaths:
		faceImg = Image.open(imagePath).convert("L")
		faceNp = np.array(faceImg, 'uint8')
		Id = int(os.path.split(imagePath)[-1].split('.')[1])
		faces.append(faceNp)
		print(Id)
		Ids.append(Id)
		cv2.imshow("training", faceNp)
		cv2.waitKey(10)
	return np.array(Ids), faces
ids, faces = getImagesWithId(path)
recognizer.train(faces,ids)
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()