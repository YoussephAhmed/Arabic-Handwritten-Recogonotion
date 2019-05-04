import cv2
import numpy as np
from keras.datasets import mnist

j = 1

#erosion for white characters
kernel = np.ones((2,2),np.uint8)
for i in range (13440):
    a = "../train/id_"+str(i+1)+"_label_"+str(j)+".png"
    img = cv2.imread(a)
    img = cv2.erode(img,kernel,iterations = 1)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    img = cv2.bitwise_not(img)

    cv2.imwrite("id_"+str(i+1+13440)+"_label_"+str(j)+".png",img)
    if (i+1) % 8 == 0:
        if j+1 == 29:
            j = 1
        else:
            j = j + 1


# translation
for i in range (13440):
    a = "../train/id_"+str(i+1)+"_label_"+str(j)+".png"
    img = cv2.imread(a)
    rows,cols,depth = img.shape
    M = np.float32([[1,0,5],[0,1,5]])
    img = cv2.warpAffine(img,M,(cols,rows))
    img = cv2.bitwise_not(img)
    cv2.imwrite("id_"+str(i+1+(13440)*2)+"_label_"+str(j)+".png",img)
    if (i+1) % 8 == 0:
        if j+1 == 29:
            j = 1
        else:
            j = j + 1


#rotation
for i in range (13440):
    a = "../train/id_"+str(i+1)+"_label_"+str(j)+".png"
    img = cv2.imread(a)
    rows,cols,depth = img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),30,1)
    img = cv2.warpAffine(img,M,(cols,rows))
    img = cv2.bitwise_not(img)
    cv2.imwrite("id_"+str(i+1+(13440)*3)+"_label_"+str(j)+".png",img)
    if (i+1) % 8 == 0:
        if j+1 == 29:
            j = 1
        else:
            j = j + 1



#load numbers
# (X_train, y_train), (X_test, y_test) = mnist.load_data()
# b = 0
# c = 0
#
#
# print(y_test[0])
# print(y_test[1])
#
# print(y_test[2])
#
# print(y_test[3])
# #adjust the size
# width = 32
# height = 32
# normal_train = []
# for i in range (X_train.shape[0]):
#
#
#     normal_train.append(cv2.resize(X_train[i],(width,height)))
#
# x_train = np.array(normal_train)
# # erosion
# for i in range (x_train.shape[0]):
#     img = cv2.erode(x_train[i],kernel,iterations = 1)
#     img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#     img = cv2.bitwise_not(img)
#
#     cv2.imwrite("id_"+str(i+1+(13440)*4)+"_label_"+str(y_train[i] + 29)+".png",img)
#     b = i+1+(13440)*4
#
# # translation
# for i in range (x_train.shape[0]):
#     rows,cols = x_train[i].shape
#     M = np.float32([[1,0,5],[0,1,5]])
#     img = cv2.warpAffine(x_train[i],M,(cols,rows))
#     img = cv2.bitwise_not(img)
#
#     cv2.imwrite("id_"+str(i+1+b)+"_label_"+str(y_train[i] + 29)+".png",img)
#     c = i + 1 + b
#
# #rotation
# for i in range (x_train.shape[0]):
#     rows,cols = x_train[i].shape
#     M = cv2.getRotationMatrix2D((cols/2,rows/2),30,1)
#     img = cv2.warpAffine(x_train[i],M,(cols,rows))
#     img = cv2.bitwise_not(img)
#
#     cv2.imwrite("id_"+str(i+1+c)+"_label_"+str(y_train[i] + 29)+".png",img)
