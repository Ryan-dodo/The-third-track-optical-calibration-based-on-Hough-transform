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

exampleFile = open('4.csv')  # 打开csv文件
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
while temp < 3.14:
    theta.append(temp)
    # 0.01 为角度西塔的步长
    temp = temp + 0.01

vote_list = [[0] * 401 for _ in range(315)]
# -50,250, -50-249 300

for j in range(0, length_zu):
    rho = []
    for i in theta:
        rho.append(x[j] * math.cos(i) + y[j] * math.sin(i))
    for i in range(len(rho)):
        rho[i] = round(rho[i]) + 50

    for i in range(len(rho)):
        vote_list[i][rho[i]] += 1

    for i in range(len(rho)):
        vote_list[i][round(rho[i]) + 50] += 1
    #
    del rho
# for i in vote_list:
#     print(i)

max_theta = []
max_rho = []
max_val = []

for i in range(40):
    max_temp = -1
    temp_rho = 0
    temp_theta = 0
    for i in range(len(vote_list)):
        for j in range(len(vote_list[0])):
            if vote_list[i][j] > max_temp:
                max_temp = vote_list[i][j]
                temp_rho = j
                temp_theta = i
    if max_temp >= 200:
        max_theta.append(temp_theta)
        max_rho.append(temp_rho)
        max_val.append(max_temp)
        vote_list[temp_theta][temp_rho] = 0
print(max_val)
print(max_theta)
print(max_rho)
print(len(max_val))
print(len(max_theta))
print(len(max_rho))
