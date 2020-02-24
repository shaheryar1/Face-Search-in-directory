import os
import face_recognition
import numpy
import cv2

from shutil import copyfile,copy
from Utils.ImageUtils import drawBoxes
from datetime import datetime
RESIZE_FACTOR=0.25
import sys


# compare face with a single target image

def findInImg(known_encodings,target_img,threshold =0.6):

    h,w,c=target_img.shape
    print(target_img.shape)
    target_img_locations=face_recognition.face_locations(target_img)

    target_encodings=face_recognition.face_encodings(target_img,target_img_locations)
    # print("Target image has",len(target_img_locations),"faces")
    for target_encoding in target_encodings:
        # dist = face_recognition.face_distance([known_encodings], target_encoding)
        results = face_recognition.compare_faces([known_encodings],target_encoding,tolerance=threshold)
        # results=True
        # print(results[0],dist[0])
        if(results[0]==True):
            return True

    return False


#iterate through folder to search
def searchFaceFromFolder(input_img_path, folder_path,destination_folder_path,output_label=None):


    total=0;
    copied=0;
    input_img = face_recognition.load_image_file(input_img_path)
 
    locations = face_recognition.face_locations(input_img)
    if (len(locations) > 1):
        print("Multiple Faces")
        return None,None
    known_encodings = face_recognition.face_encodings(input_img, known_face_locations=locations)[0]
    dir = os.listdir(folder_path)
    for target_img_path in dir:
        total = total + 1
        if(str.lower(target_img_path[-3:])=='jpg' or str.lower(target_img_path[-4:])=='jpeg' or str.lower(target_img_path[-3:])=='png'):
            progress=("Progress : "+str(round(total/len(dir)*100))+"%")
            output_label.setText(progress)
            try:
                target_img=face_recognition.load_image_file(os.path.join(folder_path,target_img_path))
                isPresent=findInImg(known_encodings,target_img)
                if(isPresent):
                    copied=copied+1
                    # print("Found face in",target_img_path)
                    src=(os.path.join(folder_path,target_img_path))
                    copy(src,destination_folder_path)
            except :
                e = sys.exc_info()
                print(e)
                pass
    return total,copied
