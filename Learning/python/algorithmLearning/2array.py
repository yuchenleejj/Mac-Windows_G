## 基本觀念
# 連續，隨機存取，插入刪除移動整體，浪費，擴充搬家
# 讀取O(1)，插入O(n)，刪除O(n)，搜尋O(logn)
# array module type code bhilq(12248不同長度的整數)fd(浮點數) 有號小寫無號大寫

## ch2-1 建立陣列

# # i => typecode 有號長整數
# from array import *

# x = array('i',range(5,46,10))
# for data in x:
#     print(data)

## ch2-2 存取陣列內容

# from array import *

# x = array('i',range(5,46,10))
# print(x[0])
# print(x[2])

## ch2-3 建立陣列將資料100插入索引位置2裡

# from array import *

# x = array('i',range(5,46,10))
# x.insert(2,100)
# for data in x:
#     print(data)

## ch2-4 在陣列末端插入100

# from array import *

# x = array('i',range(5,46,10))
# x.append(100)
# for data in x:
#     print(data)

## ch2-5 刪除陣列元素35

# from array import *

# x = array('i',range(5,46,10))
# x.remove(35)
# for data in x:
#     print(data)

## ch2-6 用pop()及pop(2)回傳和刪除元素

# from array import *

# x = array('i',range(5,46,10))
# print('刪除了',x.pop())
# for data in x:
#     print(data)
# print('刪除了',x.pop(2))
# for data in x:
#     print(data)

## ch2-7 找出陣列35之索引值

# from array import*

# x = array('i',range(5,46,10))
# print(x.index(5))

## ch2-8 更改索引2的內容為100

# from array import*

# x = array('i',range(5,46,10))
# x[2] = 100
# for data in x:
#     print(data)

## ex2-1 為1.0 2.0 5.0 6.5 7.0建立陣列

# from array import*

# x = array('f',[float(i) for i in '1.0 2.0 5.0 6.5 7.0'.split(' ')])
# for data in x:
#     print(type(data),data)

## ex2-2 用1,11,22,33,44,55建立陣列，請使用者輸入玉山刪除資料索引，如果不屬於陣列索引範圍則回應輸入錯誤

# from array import *

# x = array('i',[1,11,22,33,44,55])
# for data in x :
#     print(data)
# i = int(input('請輸入欲刪除之索引值：'))
# print('輸入錯誤') if i not in range(len(x)) else x.pop(i)
# for data in x :
#     print(data)

## ex2-3 用1,11,22,33,44,55建立陣列，要求使用者輸入0-5間的索引數字和欲插入的索引及數字，如果不在索引範圍內回傳錯誤

from array import *
import sys

x = array('i',[1,11,22,33,44,55])
for data in x :
    print(data)
i = int(input('請輸入欲插入之索引值：'))
if i not in range(len(x)):
    print('輸入錯誤') 
    sys.exit()
n = int(input('請輸入欲插入之值：'))
x.insert(i,n)
print('\n'.join(map(str,x)))

