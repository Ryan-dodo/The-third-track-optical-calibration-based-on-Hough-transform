import csv
import matplotlib.pyplot as plt
import numpy as np

# @Author  : Ryan
# @Email   : ryan1057@csu.edu.cn
# @File    : plot.py
# @Software: PyCharm
# @Time    : 2023/3/12 19:59
# @Github  : https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform

exampleFile = open('4.csv')      # 打开csv文件
exampleReader = csv.reader(exampleFile)  # 读取csv文件
exampleData = list(exampleReader)  # csv数据转换为列表
length_zu = len(exampleData)  # 得到数据行数
length_yuan = len(exampleData[0])  # 得到每行长度

# 打印所有点
# for i in range(1,length_zu):
#     print(exampleData[i])

x = list()
y = list()

for i in range(0, length_zu):  # 从第一行开始读取
    x.append(float(exampleData[i][0]))  # 将第一列数据从第一行读取到最后一行赋给列表x
    y.append(float(exampleData[i][1]))  # 将第二列数据从第一行读取到最后一行赋给列表y


# 绘制x,y的散点图
plt.scatter(x, y)
# plt.slim((-50, 50))
# plt.Alim((150, 250))
# my_x_ticks = np.arrange(-50, 50, 10)
# my_y_ticks = np.arrange(150, 250, 10)
# plt.sticks(my_x_ticks)
# plt.ticks(my_y_ticks)
ax = plt.gca()
ax.set_aspect(1)
# plt.saving('test.jpg')
plt.show()  # 显示
