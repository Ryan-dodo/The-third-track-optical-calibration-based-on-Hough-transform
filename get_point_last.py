import csv
import matplotlib.pyplot as plt
import numpy as np
import math

# @Author  : Ryan
# @Email   : ryan1057@csu.edu.cn
# @File    : solve.py
# @Software: PyCharm
# @Time    : 2023-03-14 13：58
# @Github  : https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform
# @using   : 投票找点

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
# -50,250, -50-349 300

for j in range(0, length_zu):
    rho = []
    for i in theta:
        rho.append(x[j] * math.cos(i) + y[j] * math.sin(i))
    for i in range(len(rho)):
        rho[i] = round(rho[i]) + 50

    for i in range(len(rho)):
        vote_list[i][rho[i]] += 1

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
for i in range(len(max_rho)):
    max_rho[i] -= 50
print(len(max_rho))

select = []
if select == [] and max_val != []:
    select.append(max_theta[0])
for i in max_theta:
    find = False
    for j in select:
        if abs(j - i) < 10:
            find = True
            break
    if not find:
        select.append(i)
print(select)
last_theta = []
last_rho = []
for i in range(len(select)):
    vote_sum = 0
    theta_sum = 0
    rho_sum = 0
    for j in range(len(max_val)):
        if abs(max_theta[j] - select[i]) < 10:
            vote_sum += max_val[j]
            theta_sum += max_val[j] * max_theta[j]
            rho_sum += max_rho[j] * max_val[j]
    last_theta.append((theta_sum + 0.0) / vote_sum)
    last_rho.append((rho_sum + 0.0) / vote_sum)
print(last_rho)
print(last_theta)
lineK = []
lineB = []
for i in range(len(last_theta)):
    lineB.append(last_rho[i] / math.sin(last_theta[i] / 100))
    lineK.append(-1 * math.cos(last_theta[i] / 100) / math.sin(last_theta[i] / 100))
print(lineK)
print(lineB)
for i in range(len(lineK)):
    if lineK[i] > 0:
        can_b = abs(lineB[i]) / math.sqrt(1 + lineK[i] * lineK[i]) + 140
        print('参数B为：', end='')
        print(can_b)
        print("测算角度为：", end='')
        print(90 - math.atan(lineK[i]) / math.pi * 180, end='')
        print('度')
    else:
        can_a = 700 - abs(lineB[i]) / math.sqrt(1 + lineK[i] * lineK[i]) - 46
        print('参数A为：',end='')
        print(can_a)
