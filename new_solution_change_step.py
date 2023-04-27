import csv
import matplotlib.pyplot as plt
import math
import random

# @Author  : Ryan
# @Email   : ryan1057@csu.edu.cn
# @File    : new_solution.py
# @Software: PyCharm
# @Time    : 2023-04-27 16:34
# @Github  : https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform
# @using   : 精准霍夫变换,步长可调

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


# 误差引入(稳定性分析时启动)
# for i in range(len(x)):
#     x[i] += 3 * random.random()-random.randint(0,1)
#     y[i] += 3 * random.random()-random.randint(0,1)

# 构建投票矩阵 两条直线的theta取值0.785、2.356，取theta步长0.05
# theta_1     [0.7---------------0.9]
# theta_2     [2.2---------------2.4]

# 设置步长
step = 0.05

theta_1 = []
theta_2 = []
temp = 0.7
while temp <= 0.901:
    theta_1.append(temp)
    temp = temp + step
temp = 2.2
while temp <= 2.401:
    theta_2.append(temp)
    temp = temp + step
print(theta_1)
print(theta_2)

vote_list = [[0] * 341 for _ in range(len(theta_1)*2)]
# rho 取值0-340
# 下面是投票过程
for j in range(0, length_zu):
    for i in theta_1:
        vote_rho = round(x[j] * math.cos(i) + y[j] * math.sin(i))
        vote_list[round((i-0.7)/step)][vote_rho] += 1

for j in range(0, length_zu):
    for i in theta_2:
        vote_rho = round(x[j] * math.cos(i) + y[j] * math.sin(i))
        vote_list[round((i-2.2)/step)+len(theta_1)][vote_rho] += 1
# 展示投票结果
for _ in vote_list:
    print(_)
# 找出最多票的点
max_vote_1 = -1
theta_1_select = 0
rho_1_select = 0
for i in range(0,len(theta_1)):
    for j in range(len(vote_list[0])):
        if vote_list[i][j] > max_vote_1:
            max_vote_1 = vote_list[i][j]
            theta_1_select = i * step + 0.7
            rho_1_select = j
print(max_vote_1)
print(theta_1_select)
print(rho_1_select)

# 另一组的点
max_vote_2 = -1
theta_2_select = 0
rho_2_select = 0
for i in range(len(theta_1),len(theta_1) * 2):
    for j in range(len(vote_list[0])):
        if vote_list[i][j] > max_vote_2:
            max_vote_2 = vote_list[i][j]
            theta_2_select = (i - len(theta_1)) * step + 2.2
            rho_2_select = j
print(max_vote_2)
print(theta_2_select)
print(rho_2_select)

last_rho = [rho_1_select,rho_2_select]
last_theta = [theta_1_select,theta_2_select]
print(last_rho)
print(last_theta)
lineK = []
lineB = []
for i in range(len(last_theta)):
    lineB.append(last_rho[i] / math.sin(last_theta[i]))
    lineK.append(-1 * math.cos(last_theta[i] ) / math.sin(last_theta[i] ))
print(lineK)
print(lineB)

list_line = []
for i in range(10000):
    list_line.append(-50 + 0.01 * i)
line1 = []
line2 = []
for i in list_line:
    line1.append(lineK[0] * i + lineB[0])
    line2.append(lineK[1] * i + lineB[1])
# 画笛卡尔点图、霍夫直线
plt.scatter(list_line,line1,s=1**2,c='y',alpha=0.5)
plt.scatter(list_line,line2,s=1**2,c='y',alpha=0.5)
plt.scatter(x, y,s=2**2,alpha=0.4,c='g')
plt.ylim((170, 240))
ax = plt.gca()
ax.set_aspect(1)

select_line1_x = []
select_line1_y = []
select_line2_x = []
select_line2_y = []
for i in range(len(x)):
    if abs(y[i] - lineB[0] - lineK[0] * x[i]) / math.sqrt(1 + lineK[0] * lineK[0]) < 0.6:
        select_line1_x.append(x[i])
        select_line1_y.append(y[i])
    if abs(y[i] - lineB[1] - lineK[1] * x[i]) / math.sqrt(1 + lineK[1] * lineK[1]) < 0.6:
        select_line2_x.append(x[i])
        select_line2_y.append(y[i])
# 根据霍夫直线选了两组点
plt.scatter(select_line1_x, select_line1_y,s=2**2,alpha=0.6,c='r')
# plt.scatter(select_line2_x, select_line2_y,s=2**2,alpha=0.6,c='r')
plt.ylim((170, 240))
ax = plt.gca()
ax.set_aspect(1)

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
line1_b = (len(select_line1_x) * sigma_line1_xi_yi - sigma_line1_yi * sigma_line1_xi)/(len(select_line1_x) * sigma_line1_xi_2 - sigma_line1_xi * sigma_line1_xi)

sigma_line2_xi_2 = 0
sigma_line2_yi = 0
sigma_line2_xi = 0
sigma_line2_xi_yi = 0
for i in range(len(select_line2_x)):
    sigma_line2_xi_2 += select_line2_x[i] * select_line2_x[i]
    sigma_line2_xi += select_line2_x[i]
    sigma_line2_yi += select_line2_y[i]
    sigma_line2_xi_yi += select_line2_x[i] * select_line2_y[i]
line2_a = (sigma_line2_xi_2 * sigma_line2_yi - sigma_line2_xi * sigma_line2_xi_yi)/(len(select_line2_x) * sigma_line2_xi_2 - sigma_line2_xi * sigma_line2_xi)
line2_b = (len(select_line2_x) * sigma_line2_xi_yi - sigma_line2_yi * sigma_line2_xi)/(len(select_line2_x) * sigma_line2_xi_2 - sigma_line2_xi * sigma_line2_xi)

# 最小二乘法更新后的k与b
lineK[0] = line1_b
lineK[1] = line2_b
lineB[0] = line1_a
lineB[1] = line2_a
print(lineK)
print(lineB)

# 程序运行时间打印
# end = time.clock()
# print(end-start)

for i in range(len(lineK)):
    if lineK[i] > 0:
        can_b = abs(lineB[i]) / math.sqrt(1 + lineK[i] * lineK[i]) + 140 + 90 * math.cos(math.radians(90 - math.atan(lineK[i]) / math.pi * 180))
        print('导高为：', end='')
        print(can_b)
        print("角度为：", end='')
        jiaodu = 90 - math.atan(lineK[i]) / math.pi * 180
        print(jiaodu, end='')
        print('度')
    else:
        can_a = 700 - abs(lineB[i]) / math.sqrt(1 + lineK[i] * lineK[i]) - 46 - 90 * math.sin(math.radians(90 - math.atan(lineK[i]) / math.pi * 180))
        print('拉出值为：',end='')
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
# plt.scatter(list_line,line1,s=1**1,c='g',alpha=0.5)
# plt.scatter(list_line,line2,s=1**1,c='g',alpha=0.5)
# plt.scatter(x, y,s=2**2,alpha=0.4)
plt.show()  # 显示
