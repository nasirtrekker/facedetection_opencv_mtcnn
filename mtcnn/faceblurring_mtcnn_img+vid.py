from mtcnn.mtcnn import MTCNN
import cv2
import glob
import argparse
import os, sys
from os import listdir, makedirs
import shutil
import numpy as np

# execute: python faceblurring_mtcnn_img+vid.py -i [image/video] -o [outputfolder]
img_path = "./img"


def reset(reset_path):
    path = reset_path
    if os.path.isdir(path):
        shutil.rmtree(path)
        makedirs(path)
    else:
        makedirs(path)


def video_to_images(video, path_output_dir):
	vidcap = cv2.VideoCapture(video)
	count = 0
	while vidcap.isOpened():
	    success, image = vidcap.read()
	    if success:
	        cv2.imwrite(os.path.join(path_output_dir, '%04d.png') % count, image)
	        count += 1
	    else:
	        break
	cv2.destroyAllWindows()
	vidcap.release()


if __name__=="__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("--source_video", "-i", type=str)
	parser.add_argument("--output_blur_img_folder", "-o", type=str)
	args = parser.parse_args()

	blur_path = args.output_blur_img_folder

	reset(blur_path)
	reset(img_path)
	
	video_to_images(args.source_video, img_path)
	print(args.source_video)
	source_path = sorted(glob.glob("./img/*.png"))


	for i, fi in enumerate(source_path):
		print(fi)
		img = cv2.imread(fi)
		blur = img.copy()

		detector = MTCNN()
		if not detector.detect_faces(img) == []:
			for j in range(len(detector.detect_faces(img))):
				pos = detector.detect_faces(img)[j]["box"]
				blur[pos[1]:pos[1]+pos[3], pos[0]:pos[0]+pos[2]] = cv2.blur(blur[pos[1]:pos[1]+pos[3], pos[0]:pos[0]+pos[2]], (40,40))

		cv2.imwrite(blur_path+"/%05d.jpg"%i, blur)