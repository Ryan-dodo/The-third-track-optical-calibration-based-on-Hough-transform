import csv
import matplotlib.pyplot as plt
import numpy as np
import math

# @Author  : Ryan
# @Email   : ryan1057@csu.edu.cn
# @File    : alpha_try.py
# @Software: PyCharm
# @Time    : 2023-04-11 16:12
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
        can_b = abs(lineB[i]) / math.sqrt(1 + lineK[i] * lineK[i]) + 140 + 90 * math.cos(math.radians(90 - math.atan(lineK[i]) / math.pi * 180))
        print('参数B为：', end='')
        print(can_b)
        print("测算角度为：", end='')
        jiaodu = 90 - math.atan(lineK[i]) / math.pi * 180
        print(jiaodu, end='')
        print('度')
    else:
        can_a = 700 - abs(lineB[i]) / math.sqrt(1 + lineK[i] * lineK[i]) - 46 - 90 * math.sin(math.radians(90 - math.atan(lineK[i]) / math.pi * 180))
        print('参数A为：',end='')
        print(can_a)

list_line = []
for i in range(10000):
    list_line.append(-50 + 0.01 * i)
line1 = []
line2 = []
for i in list_line:
    line1.append(lineK[0] * i + lineB[0])
    line2.append(lineK[1] * i + lineB[1])
# 画笛卡尔点图、霍夫直线
plt.scatter(list_line,line1,s=1**2,c='y',alpha=0.1)
plt.scatter(list_line,line2,s=1**2,c='y',alpha=0.1)
plt.scatter(x, y,s=2**2,alpha=0.4)
plt.ylim((170, 240))
ax = plt.gca()
ax.set_aspect(1)

select_line1_x = []
select_line1_y = []
select_line2_x = []
select_line2_y = []
for i in range(len(x)):
    if abs(y[i] - lineB[0] - lineK[0] * x[i]) / math.sqrt(1 + lineK[0] * lineK[0]) < 0.3 :
        select_line1_x.append(x[i])
        select_line1_y.append(y[i])
    if abs(y[i] - lineB[1] - lineK[1] * x[i]) / math.sqrt(1 + lineK[1] * lineK[1]) < 0.3 :
        select_line2_x.append(x[i])
        select_line2_y.append(y[i])
# 根据霍夫直线选了两组点
# plt.scatter(select_line1_x, select_line1_y,s=2**2,alpha=0.09,c='r')
# plt.scatter(select_line2_x, select_line2_y,s=2**2,alpha=0.09,c='r')
plt.ylim((170, 240))
ax = plt.gca()
ax.set_aspect(1)
plt.show()  # 显示

sigma_line1_xi_2 = 0
sigma_line1_yi = 0
sigma_line1_xi = 0
sigma_line1_xi_yi = 0
for i in range(len(select_line1_x)):
    sigma_line1_xi_2 += select_line1_x[i] * select_line1_x[i]
    sigma_line1_xi += select_line1_x[i]
    sigma_line1_yi += select_line1_y[i]
    sigma_line1_xi_yi += select_line1_x[i] * select_line1_y[i]
line1_a = (sigma_line1_xi_2 * sigma_line1_yi - sigma_line1_xi * sigma_line1_xi_yi)/(len(select_line1_x) * sigma_line1_xi_2 - sigma_line1_xi * sigma_line1_xi)
print(line1_a)
