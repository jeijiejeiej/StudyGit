import cv2 
# 摄像头
cap=cv2.VideoCapture(0)
falg=1
num=1
while(cap.isOpened()):# 检测石是否在开启状态
    ret_flag,Vshow=cap.read()#得到每帧图像
    cv2.imshow('Capture_Test',Vshow)#显示图像
    k=cv2.waitKey(1) & 0xFF
    if k==ord('s'):#按键判断:按s保存
        cv2.imwrite("renlianshibie-zhou/jm/"+str(num)+".zhou"+".jpg",Vshow)
        print("success to save"+str(num)+'.jpg')
        print("---------------------------")
        num+=1
    elif k==ord(' '):#空格退出
        break
# 释放摄像头
cap.release()
# 释放内存
cv2.destroyAllWindows()