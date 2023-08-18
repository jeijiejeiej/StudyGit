import cv2 as cv
img=cv.imread("C:/Users/16248/vanli/StudyGit/renlianshibie-zhou/face1.png")
# r声明原生字符串
gray_img=cv.cvtColor(img,cv.COLOR_BAYER_BG2GRAY)
# 灰度转换
cv.imshow("gray",gray_img)
# 显示灰度
cv.imwrite("gray_face11.jpg",gray_img)
# 保存图
cv.imshow("read_img",img)
# 展示
cv.waitKey(0)
# 停留秒数
cv.destroyAllWindows()
# 释放内存