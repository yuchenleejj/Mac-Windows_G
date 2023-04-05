## 實作stack有原本的list可以用也可以自己實作 元素要有pop append(push) len(size) isEmpty 
## 程式函式的運作呼叫流程就是用stack

## ch5-1 append模擬push,pop模擬pop()
# fruits = ['mango','banana','grava','grape']
# fruits.append('strawberry')
# fruits.append('apple')
# print('列印fruits',fruits)
# print('pop操作',fruits.pop())
# print('pop操作',fruits.pop())
# print('pop操作',fruits.pop())

## ch5-2 將水果列表push進入stack，然後輸出多少種水果在stack中

# class Stack():
#     def __init__(self):
#         self.stack = []
#     def myPush(self, data):
#         self.stack.append(data)
#     def myPop(self):
#         return self.stack.pop()
#     def size(self):
#         return len(self.stack)
    
# fruits = ['mango','banana','grava','grape']
# stack = Stack()
# for fruit in fruits:
#     stack.myPush(fruit)
#     print(f'將 {fruit} push進stack裡')
# print('pop操作:',stack.myPop())
# print(f'總共{stack.size()}種水果')

## ch5-3 將5-2多加一個isempty method

# class Stack():
#     def __init__(self):
#         self.stack = []
#     def myPush(self, data):
#         self.stack.append(data)
#     def myPop(self):
#         return self.stack.pop()
#     def size(self):
#         return len(self.stack)
#     def isEmpty(self):
#         return self.stack == []

# fruits = ['mango','banana','grava','grape']
# stack = Stack()
# for fruit in fruits:
#     stack.myPush(fruit)
#     print(f'將 {fruit} push進stack裡')
# print(f'總共{stack.size()}種水果')
# # print('pop操作:',stack.myPop())
# # print('pop操作:',stack.myPop())
# # print('stack是空的嗎?',stack.isEmpty())
# # print('pop操作:',stack.myPop())
# # print('pop操作:',stack.myPop())
# # print('stack是空的嗎?',stack.isEmpty())

# # 用stack isEmpty 性質去把stack中的東西取出
# while not stack.isEmpty():
#     print('pop操作:',stack.myPop())

## ch5-4 階乘函式用註解去了解其callback的過程

# def factorial(n):
#     global fact
#     if n == 1:
#         print(f'factorial({n})呼叫前 {n}! = {fact}')
#         print('到達遞迴終止條件 n = 1')
#         fact = 1
#         print(f'factorial({n})呼叫後 {n}! = {fact}')
#         return fact
#     else:
#         print(f'factorial({n})呼叫前 {n}! = {fact}')
#         fact = n * factorial(n-1)
#         print(f'factorial({n})呼叫後 {n}! = {fact}')
#         return fact

# fact = 0
# N = eval(input('輸入階乘數:'))
# print(f'{N}的階乘是 {factorial(N)}')

## ex5-1 stack 實作push get pop 

# class Stack():
#     def __init__(self):
#         self.stack = []
#     def myPush(self, data):
#         self.stack.append(data)
#     def myGet(self):
#         return self.stack[-1]
#     def myPop(self):
#         return self.stack.pop()

# stack = Stack()
# fruits = ['mango','banana','grava','grape']
# for fruit in fruits:
#     stack.myPush(fruit)
# print(f'堆疊取出 {stack.myGet()}，同時不刪除')
# print(stack.myPop())

## ex5-2 增加cls method 

class Stack():
    def __init__(self):
        self.stack = []
    def myPush(self, data):
        self.stack.append(data)
    def myGet(self):
        return self.stack[-1]
    def myPop(self):
        return self.stack.pop()
    def mySize(self):
        return len(self.stack)
    def isEmpty(self):
        return self.stack == []
    def myCls(self):
        while not self.isEmpty():
            self.myPop()

stack = Stack()
fruits = ['mango','banana','grava','grape']
for fruit in fruits:
    stack.myPush(fruit)
    print(f'將{fruit} push進入stack')
print(f'堆疊有 {stack.mySize()} 種水果')
stack.myCls()
if stack.isEmpty :
    print('程式結束')