import csv
import matplotlib.pyplot as plt
import numpy as np
import math

# @Author  : Ryan
# @Email   : ryan1057@csu.edu.cn
# @File    : solve.py
# @Software: PyCharm
# @Time    : 2023-03-13 00:59
# @Github  : https://github.com/Ryan-dodo/Chinese_License_plate_recognition
# @using   : 统计法 vote

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

# 0,200,0.01
# 0,3.14,0.01

# -50 250

vote_list = [[0] * 300] * 314

theta_index = 0  # 0,3.14,0.01 0-313 314
rho_index = -51  # -50,250, -50-249 300

while theta_index < 314:
    for i in range(0, length_zu):
        rho_index = -51
        while rho_index < 249:
            rho_index += 1
            if abs(x[i] * math.cos(theta_index / 0.01) + y[i] * math.sin(theta_index / 0.01) - rho_index) <= 0.5:
                vote_list[theta_index][rho_index] += 1
                # print('theta_index:', end='')
                # print(theta_index)
                # print('rho_index:', end='')
                # print(rho_index)

                break

    theta_index += 1
print(vote_list)
