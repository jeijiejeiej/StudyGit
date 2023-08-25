import cv2
import numpy as np
import os
# coding=utf-8
import urllib
import urllib.request
import hashlib
# 此程序按空格键退出，详情间最后的while
# 看上面一条
# 看上面一条前面信息录入也是这么搞的









#加载训练数据集文件
recogizer=cv2.face.LBPHFaceRecognizer_create() # type: ignore
recogizer.read(r'renlianshibie-zhou\trainer\trainer.yml')
names=[]
warningtime = 0
def face_detect_demo(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_detector=cv2.CascadeClassifier(r'renlianshibie-zhou\haar\haarcascade_frontalface_alt2.xml')
    face=face_detector.detectMultiScale(gray)
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        cv2.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,0),thickness=1)
        # 人脸识别
        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        # print('标签id:',ids,'置信评分：', confidence)
        if confidence > 80:
            global warningtime
            warningtime += 1
            if warningtime > 100:
               warningtime = 0
            cv2.putText(img, 'unkonw', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        else:
            cv2.putText(img,str(names[ids-1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
    cv2.imshow('result',img)
    #print('bug:',ids)
def name():
    path = r'renlianshibie-zhou\jm'
    #names = []
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    for imagePath in imagePaths:
       name = str(os.path.split(imagePath)[1].split('.',2)[1])
       names.append(name)


cap=cv2.VideoCapture(r'renlianshibie-zhou\1.mp4')
name()
while True:
    flag,frame=cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord(' ') == cv2.waitKey(10):
        break
cv2.destroyAllWindows()
cap.release()
#print(names)
