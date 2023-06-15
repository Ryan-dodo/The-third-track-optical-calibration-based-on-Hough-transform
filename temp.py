import csv
import matplotlib.pyplot as plt
import numpy as np

# @Author  : liuzhihong
# @File    : print(1).py
# @Software: PyCharm
# @Time    : 2023年6月9日19:46:38

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

exampleFile = open(r'e:\data.csv')      # 打开csv文件
exampleReader = csv.reader(exampleFile)  # 读取csv文件
exampleData = list(exampleReader)  # csv数据转换为列表
length_zu = len(exampleData)  # 得到数据行数
length_yuan = len(exampleData[0])  # 得到每行长度

# 打印所有点
for i in range(0, length_zu) :
    print(exampleData[i])

x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_list1 = []
y_list2 = []
y_list3 = []
y_list4 = []

for i in range(12) :
    if i >= 2 :
        y_list1.append(int(exampleData[0][i]))
        y_list2.append(int(exampleData[1][i]))
        y_list3.append(int(exampleData[2][i]))
        y_list4.append(int(exampleData[3][i]))

min_idx1 = np.argmin(y_list1)
min_idx2 = np.argmin(y_list2)
min_idx3 = np.argmin(y_list3)
min_idx4 = np.argmin(y_list4)

plt.plot(x_list[min_idx1], y_list1[min_idx1], 'ko')
plt.plot(x_list[min_idx2], y_list2[min_idx2], 'ko')
plt.plot(x_list[min_idx3], y_list3[min_idx3], 'ko')
plt.plot(x_list[min_idx4], y_list4[min_idx4], 'ko')

plt.title("不同规模矩阵最优线程数示意图")
plt.plot(x_list, y_list1, label = '500规模')
plt.plot(x_list, y_list2, label = '700规模')
plt.plot(x_list, y_list3, label = '900规模')
plt.plot(x_list, y_list4, label = '1200规模')

plt.legend()#添加图例

plt.show()
