import csv
import matplotlib.pyplot as plt
import math

# @Author  : Ryan
# @Email   : ryan1057@csu.edu.cn
# @File    : hofu.py
# @Software: PyCharm
# @Time    : 2023-04-14 16:43
# @Github  : https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform
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
    ax.plot(theta,rho,alpha = 1/100,c='g')
    del rho


theta = []
temp = 0
while temp < 3.14:
    theta.append(temp)
    # 0.01 为角度西塔的步长
    temp = temp + 0.01

rho = []
temp = -50
while temp < 350:
    rho.append(temp)
    temp = temp + 1

# 绘制网格
# for i in theta:
#     ax.axvline(x=i, ymin=-50, ymax=350)
# for i in rho:
#     ax.axhline(y=i, xmin=0, xmax=3.15)

# 选出票数大于200的点
max_val = [293, 287, 283, 258, 248, 244, 228, 220, 201]
max_theta = [77, 79, 78, 76, 234, 235, 232, 233, 236]
max_rho = [175, 178, 176, 173, 179, 178, 182, 181, 176]

for i in range(len(max_val)):
    max_rho[i] = max_rho[i] - 50
    max_theta[i] = max_theta[i] / 100
    max_val[i] = max_val[i] / 100 * 3
for i in range(len(max_val)):
    plt.scatter(max_theta[i], max_rho[i],s=max_val[i]**2,c='b')

# 绘制加权平均点
last_rho = [125.56021409455843, 129.24276950043821]
last_theta = [0.7753434433541481, 2.3397370727432076]
plt.scatter(last_theta, last_rho,s=8**2,c='r')

plt.show()  # 显示
# plt.savefig('xx4.jpg')
