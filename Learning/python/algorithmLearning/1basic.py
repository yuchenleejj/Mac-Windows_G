## ch1-1 階乘公式

# def factorial(n):
#     if n == 1:
#         return 1
#     elif n > 1:
#         return n*factorial(n-1)

# N = eval(input("請輸入階乘數： "))
# print(f'{N}!={factorial(N)}')

## ch1-2 給定n筆資料，最差的情況要多少年才能獲得由小排到大的結果（枚舉法）

# 假設電腦每秒可處理 10000000000000
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return (n*factorial(n-1))

# N = eval(input('請輸入您的資料個數： '))
# times = 10000000000000
# day_secs = 60*60*24
# year_secs = 365*day_secs
# combinations = factorial(N)
# years = combinations/(year_secs*times)
# print('資料個數%d, 數列組合%d' % (N,combinations))
# print('需要%d年才可獲得結果' % years)

## ch1-3 列出串列1,2,3 的所有可能組合

# import itertools

# x = [1,2,3]
# perm = itertools.permutations(x)
# for i in perm:
#     print(i)

## 補充包：log 使用

# import math

# print(math.log(4,2)) # 底數為2，指數為4
# print(math.log(2)) # 底數為e
# print(math.log2(4))

## ch1-4 繪製O(1,log n,n)之圖形，x座標從1-10

# import matplotlib.pyplot as plt
# import numpy as np

# xpt = np.linspace(1,10,10)
# ypt1 = xpt/xpt
# ypt2 = np.log2(xpt)
# ypt3 = xpt
# plt.plot(xpt, ypt1, '-o', label="O(1)")
# plt.plot(xpt, ypt2, '-o', label="O(logn)")
# plt.plot(xpt, ypt3, '-o', label="O(n)")
# plt.legend(loc='best')
# plt.show()

## ch1-5 繪製O(1,logn,n,nlogn,n^2)比較圖

# import matplotlib.pyplot as plt
# import numpy as np

# xpt = np.linspace(1,10,10)
# ypt1 = xpt/xpt
# ypt2 = np.log2(xpt)
# ypt3 = xpt
# ypt4 = xpt*ypt2
# ypt5 = xpt*xpt

# plt.plot(xpt,ypt1,'-o',label='O(1)')
# plt.plot(xpt,ypt2,'-o',label='O(logn)')
# plt.plot(xpt,ypt3,'-o',label='O(n)')
# plt.plot(xpt,ypt4,'-o',label='O(nlogn)')
# plt.plot(xpt,ypt5,'-o',label='O(n^2)')
# plt.legend(loc='best')
# plt.show()

## ex1-1 計算20筆數據之排列組合有多少個

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return (n*factorial(n-1))

# print('%d比資料排列組合共有%d個' %(20,factorial(20)))

## ex1-2 延續上題產生上述排列組合需要多少時間，如果產生一個需要0.0000000001秒

# time = 0.0000000001
# print('產生20比資料的所有排列組合需要 %d秒' %(factorial(20)*time))

## ex1-3 列印出元素abcdef的所有組合方式

# import itertools

# abcdef = ['a','b','c','d','e','f']
# perms = itertools.permutations(abcdef)
# for i in perms:
#     print(i)

## ex1-4 列出北京 天津 上海 廣州 武漢拜訪順序有幾種順便列出所有拜訪順序

# import itertools

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)

# visits = '北京 天津 上海 廣州 武漢'.split(' ')
# perms = itertools.permutations(visits)
# for i in perms:
#     print(i)
# print(f'總共有{factorial(len(visits))}種')

