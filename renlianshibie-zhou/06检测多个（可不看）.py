import cv2 as cv
# 建立检测函数
def face_detect_demo():
    gary=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detect=cv.CascadeClassifier(r'D:\anaconda\envs\yolov5\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    # r用来表示原生字符，用cv2自带的分类器
    face=face_detect.detectMultiScale(gary)
    # 这个函数是关键改进地方
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        cv.imshow('result',img)
img=cv.imread("C:/Users/16248/vanli/StudyGit/renlianshibie-zhou/face2.png")
# 检测函数
face_detect_demo()
# 按下英文输入法q退出
while True:
    if ord('q')==cv.waitKey(0):
        break
# 释放内存
cv.destroyAllWindows()