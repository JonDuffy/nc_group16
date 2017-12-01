
from PIL import Image
import numpy as np
# import scipy
import matplotlib.pyplot as plt
filename='/Users/yawensun/darknet/tensortest/2007_000027.jpg'
def ImageToMatrix(filename):
    # 读取图片
    im = Image.open(filename)
    # 显示图片
    #     im.show()
    width,height = im.size
    im = im.convert("L")
    data = im.getdata()
    data = np.matrix(data,dtype='float')
    #new_data = np.reshape(data,(width,height))
    new_data = np.reshape(data,(height,width))
    return new_data
#     new_im = Image.fromarray(new_data)
#     # 显示图片
#     new_im.show()
def MatrixToImage(data):
    data = data*255
    new_im = Image.fromarray(data.astype(np.uint8))
    return new_im




data = ImageToMatrix(filename)
print (data)
new_im = MatrixToImage(data)
plt.imshow(data, cmap=plt.cm.gray, interpolation='nearest')
new_im.show()
new_im.save('lena_1.bmp')

fout = open("main.txt",'w')  # 打开输出文件
for i in range(len(data)):
    fout.write(str(data[i]))
    fout.write('\n')
fout.close()  # 最后关闭文件



