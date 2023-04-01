####基本資料結構=========
## basic data structure-----------

# a,b = 3,2
# print(a/b) # 1.5
# print(a//b) # 1 無條件捨去
# print(a%b) # 1
# print(a**b) # 9

## boolean order-----------

# # () > not > and > or
# print(None or 0 or 0.0 or '' or [] or {} or set()) # 全部都是false

## string-----------

# # string is immutable
# # string 的表示法
# print('s',"s",'''s''',"""s""",str(5),'s'+'n')
# # 空白字元 \n \s \t

# # 用法
# y = '  "s"this is lazy\thhh\nhello '
# z = '   this is a test\t\n'
# k = 'smartphone'
# print(y)
# print(z)
# print(z.strip()) # 移除空白字元
# print(k.startswith('smart'))
# print(k.find('phone'))
# print(k.replace('smart','stupid'))
# print('sm' in k)

## 關鍵字 None-----------

# def f():
#     x = 2
# print(f() is None) #T
# print('' == None) #F
# print(0 == None) #F

####容器資料結構=========
###list+++++++++
## 關鍵字 is-----------

# y = x = 3
# print(x is y) #T
# print([3] is [3]) #F => list is mutable

## 添加元素

# l = [2,2,3]
# l.append(4)
# print(l)
# l.insert(7,2)
# print(l)
# print(l+[8,9])

## 移除元素

# l = [1,2,3,4]
# l.remove(1)
# print(l)
# l.pop(2)
# print(l)

## 反轉及排序列表

# l = [1,2,3,4]
# l.reverse()
# print(l)
# l.sort()
# print(l)

## 索引操作 

# l = [2,2,3,4]
# print(l.index(2,1))

### set集合+++++++++
## 集合

# # 在set中的元素都是可雜湊的(immutable)，也就是list不能放進去
# hero = 'Harry'
# print(hash(hero))
# l1 = ['justin']
# l2 = ['Christine']
# teams = {l1,l2}

## unique

# 每個元素都滿足hash(x)!=hash(y)

### 字典dict+++++++++
## 基本用法

# grocery = {'apple':20,'banana':30}
# print(grocery.keys())
# print(grocery.values())
# print(grocery.items()) # 轉成tuple

## 成員檢查in

# set 的檢查速度比list快，set的實作有點像dict，所以python內部搜索過程像是字典一樣

### lambda匿名函式

print((lambda x: x+3)(4))
x = lambda y: y+4
print(x(5))




