import cv2 as cv
img=cv.imread("C:/Users/16248/vanli/StudyGit/renlianshibie-zhou/face1.png")
# r声明原生字符串
cv.imshow("read_img",img)
# 展示
cv.waitKey(0)
# 停留秒数
cv.destroyAllWindows()
# 释放内存