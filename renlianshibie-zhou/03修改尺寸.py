import cv2 as cv
img=cv.imread(r"renlianshibie-zhou/face1.png")
resize_img=cv.resize(img,dsize=(200,200))
# 修改尺寸
cv.imshow('img',img)
# 显示原图
cv.imshow('resize_img',resize_img)
# 显示修改后的
print('未修改:',img.shape)
# 打印原图尺寸大小
print('修改后:',resize_img.shape)
# 打印修改后的大小
while True:
    if ord('q')==cv.waitKey(0):
        break
# 按下英文输入法q退出
cv.destroyAllWindows()
# 释放内存