import cv2 as cv
img=cv.imread(r"renlianshibie-zhou\face1.png")
cv.imshow("read_img",img)
# 展示
cv.waitKey(0)
# 停留秒数
cv.destroyAllWindows()
# 释放内存