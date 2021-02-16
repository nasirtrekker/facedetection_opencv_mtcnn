### Face detection with HaarCascade and MTCNN.

How to use:
- Clone this repo
- Create new virtulenv with conda: conda env create cv2vision-env.yml
- execute python scripts as follows:


1. Download the this repository and haarcascade_frontalface_default.xml file
2. Execute python file:

Detecting face:
	 - image_facedetect.py --> detect face from image file using OpenCV HaarCascade
	 - video_facedetect.py --> detect face from video file using OpenCVHaarCascade
	 - mtcnn_facedetect_image.py-->detect face with Facenets MTCNN
	 
Detect and blurring face:
	- faceblurring.py --> detect face from image file using opencv HaarCascade and detected faces blurred out using a simple pixellation technique
	- faceblurring_mtcnn_img+vid.py--> detect and blurred face with Facenets MTCNN


	 

References:
MTCNN:Multi-task Cascaded Convolutional Neural Networks for Face Detection, based on TensorFlow.
(https://pypi.org/project/mtcnn/ 
OpenCV:https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html 
FaceNEt: https://arxiv.org/abs/1503.03832
Blogs: https://machinelearningmastery.com/how-to-perform-face-detection-with-classical-and-deep-learning-methods-in-python-with-keras/

