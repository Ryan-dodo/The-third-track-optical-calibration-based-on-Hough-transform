import csv
import matplotlib.pyplot as plt
import numpy as np
import math

# @Author  : Ryan
# @Email   : ryan1057@csu.edu.cn
# @File    : hofu.py
# @Software: PyCharm
# @Time    : 2022/6/4 16:04
# @Github  : https://github.com/Ryan-dodo/Chinese_License_plate_recognition
# @using   : 绘制霍夫空间

exampleFile = open('4.csv')      # 打开csv文件
exampleReader = csv.reader(exampleFile)  # 读取csv文件
exampleData = list(exampleReader)  # csv数据转换为列表
length_zu = len(exampleData)  # 得到数据行数
length_yuan = len(exampleData[0])  # 得到每行长度

x = list()
y = list()

for i in range(0, length_zu):  # 从第一行开始读取
    x.append(float(exampleData[i][0]))  # 将第一列数据从第一行读取到最后一行赋给列表x
    y.append(float(exampleData[i][1]))  # 将第二列数据从第一行读取到最后一行赋给列表y

theta = []
temp = 0
while (temp<3.15):
    theta.append(temp)
    # 0.01 为角度西塔的步长
    temp = temp + 0.001

# 新建空白图
fig, ax = plt.subplots()

for j in range(0, length_zu):
    rho = []
    for i in theta:
        rho.append(x[j]*math.cos(i)+y[j]*math.sin(i))
    ax.plot(theta,rho)
    del rho
plt.show()  # 显示
# plt.savefig('霍夫空间.jpg')