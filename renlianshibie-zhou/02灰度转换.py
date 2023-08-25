import cv2 as cv
img=cv.imread(r"renlianshibie-zhou\face1.png")

gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 灰度转换
cv.imshow("gray",gray_img)
# 显示灰度
cv.imwrite(r"renlianshibie-zhou\gray_face11.png",gray_img)
# 保存图
# cv.imshow("read_img",img)
# 展示
cv.waitKey(0)
# 停留秒数
cv.destroyAllWindows()
# 释放内存