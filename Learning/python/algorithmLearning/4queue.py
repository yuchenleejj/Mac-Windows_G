##FIFO 

## ch4-1 為佇列建立三筆資料然後列出佇列長度

# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self,data):
#         self.queue.insert(0,data) # 關鍵
#     def size(self):
#         return len(self.queue)

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print('佇列長度',q.size())

## ch4-2 讀取4次佇列並觀察執行結果

# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, data):
#         self.queue.insert(0,data)
#     def size(self):
#         return len(self.queue)
#     def dequeue(self):
#         if len(self.queue):
#             return self.queue.pop()
#         return "佇列是空的"

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print('讀取佇列:',q.dequeue())
# print('讀取佇列:',q.dequeue())
# print('讀取佇列:',q.dequeue())

## ch4-3 建立與列印佇列

# from queue import Queue
# q = Queue()
# for i in range(3):
#     q.put(i)
# while not q.empty():
#     print(q.get())

## ex4-1 插入資料至佇列

# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self,data):
#         self.queue.insert(0,data)
#         print(f"成功插入 {data} 至佇列")
#     def dequeue(self):
#         if len(self.queue):
#             return self.queue.pop()
#         return "佇列空了"
#     def size(self):
#         return len(self.queue)
    
# q = Queue()
# q.enqueue("Grape")
# q.enqueue("Mango")
# q.enqueue("Apple")
# print("佇列長度:",q.size())

## ex4-2 同ex4-1

# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self,data):
#         self.queue.insert(0,data)
#         print(f"成功插入 {data} 至佇列")
#     def dequeue(self):
#         if len(self.queue):
#             return self.queue.pop()
#         return "佇列空了"
#     def size(self):
#         return len(self.queue)

# q1 = Queue()
# q1.enqueue("漢堡")
# q1.enqueue("薯條")
# q1.enqueue("可樂")
# print("佇列輸出")
# print(q1.dequeue())
# print(q1.dequeue())
# print(q1.dequeue())