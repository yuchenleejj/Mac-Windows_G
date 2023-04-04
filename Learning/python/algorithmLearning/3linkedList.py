# 插入資料O(1)、刪除資料O(1)、查詢資料O(n):順序查詢
# 連結串列 單向連結串列、雙向連結串列、循環連結串列

## ch3-1 含三個節點的鏈結串列，並印出來

# class Node():
#     def __init__(self,data=None):
#         self.data = data
#         self.next = None

# n1 = Node(5)
# n2 = Node(6)
# n3 = Node(7)

# n1.next = n2
# n2.next = n3
# ptr = n1

# while ptr:
#     print(ptr.data)
#     ptr = ptr.next

## ch3-2 建立linkedlist

# class Node():
#     def __init__(self,data=None):
#         self.data = data
#         self.next = None

# class Linked_list():
#     def __init__(self):
#         self.head = None
#     def print_list(self):
#         ptr = self.head
#         while ptr:
#             print(ptr.data)
#             ptr = ptr.next

# link = Linked_list()
# link.head = Node(5)
# n2 = Node(6)
# n3 = Node(7)
# link.head.next = n2
# n2.next = n3
# link.print_list()

## ch3-3 插入資料100在串列頭上

# class Node():
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class Linked_list():
#     def __init__(self):
#         self.head = None
#     def print_list(self):
#         ptr = self.head
#         while ptr:
#             print(ptr.data)
#             ptr = ptr.next
#     def beginning(self, newData):
#         new_node = Node(newData)
#         new_node.next = self.head
#         self.head = new_node

# link = Linked_list()
# link.head = Node(5)
# n2 = Node(6)
# n3 = Node(7)
# link.head.next = n2
# n2.next = n3
# link.print_list()
# print('插入100在串列頭')
# link.beginning(100)
# link.print_list()

## ch3-4 在串列末端插入新的節點

# class Node():
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class Linked_list():
#     def __init__(self):
#         self.head = None
#     def print_list(self):
#         ptr = self.head
#         while ptr:
#             print(ptr.data)
#             ptr = ptr.next
#     def ending(self, newData):
#         last_data = Node(newData)
#         if not(self.head):
#             self.head = last_data
#             return
#         last_ptr = self.head
#         while last_ptr.next:
#             last_ptr = last_ptr.next
#         last_ptr.next = last_data

# link1 = Linked_list()
# link1.head = Node(5)
# n2 = Node(15)
# n3 = Node(25)
# link1.head.next = n2
# n2.next = Node(35)
# link1.print_list()
# print('插入新的值在尾端')
# link1.ending(100)
# link1.print_list()
# print('在完全空的linkedlist中插入值在尾端')
# link2 = Linked_list()
# link2.ending(200)
# link2.ending(20)
# link2.print_list()

## ch3-5 在中間插入新的節點

# class Node():
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class Linked_list():
#     def __init__(self):
#         self.head = None
#     def print_list(self):
#         ptr = self.head
#         while ptr:
#             print(ptr.data)
#             ptr = ptr.next
#     def between(self, prenode, newData):
#         if prenode == None: ## 要none才行，不然有其他非物件也能放入會出錯
#             print('缺插入節點的前個節點')
#             return
#         new_node = Node(newData)
#         new_node.next = prenode.next
#         prenode.next = new_node

# link = Linked_list()
# link.head = Node(5)
# n2 = Node(15)
# n3 = Node(25)
# link.head.next = n2
# n2.next = n3
# link.print_list()
# print("插入值在串列中間")
# link.between(n2, 200)
# link.print_list()
# link.between(n3.next, 300)

## ch3-6 刪除元素

# # 分三種狀況在最前方、在中間(含在最後)、不在裡面
# class Node():
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class Linked_list():
#     def __init__(self):
#         self.head = None
#     def print_list(self):
#         ptr = self.head
#         while ptr:
#             print(ptr.data)
#             ptr = ptr.next
#     def ending(self, NewData):
#         new_node = Node(NewData)
#         if self.head == None:
#             self.head = new_node
#             return
#         last_ptr = self.head
#         while last_ptr.next:
#             last_ptr = last_ptr.next
#         last_ptr.next = new_node
#     def rm_node(self, rmkey):
#         ptr = self.head
#         # if ptr:
#         #     if ptr.data == rmkey:
#         #         self.head = ptr.next
#         #         return
#         #     while ptr:
#         #         if ptr.data == rmkey:
#         #             break
#         #         prev = ptr
#         #         ptr = ptr.next
#         #     prev.next = ptr.next
#         #     return
#         # return
#         # 上面是錯的因為沒考慮到如果遇到沒有存在的節點會在190出問題
#         if ptr:
#             if ptr.data == rmkey:
#                 self.head = ptr.next
#                 return
#         while ptr:
#             if ptr.data == rmkey:
#                 break
#             prev = ptr
#             ptr = ptr.next
#         if ptr == None:
#             return
#         prev.next = ptr.next
# link = Linked_list()
# link.head = Node(5)
# n2 = Node(15)
# n3 = Node(25)
# link.head.next = n2
# n2.next = n3
# link.print_list()
# print('刪除15的節點')
# link.rm_node(15)
# link.print_list()
# print('刪除不存在節點')
# link.rm_node(15)
# link.print_list()
# print('刪除第一個節點')
# link.rm_node(5)
# link.print_list()
# print('刪除一個空串列中的一點')
# link1 = Linked_list()
# link1.rm_node(5)
# link1.print_list()

## ch3-7 建立循環串列3個節點，並印完

# class Node():
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# n1 = Node(5)
# n2 = Node(6)
# n3 = Node(7)
# n1.next = n2
# n2.next = n3
# n3.next = n1
# ptr = n1
# count = 1
# while count <= 3:
#     print(ptr.data)
#     ptr = ptr.next
#     count+=1

## ch3-8 建立雙向鏈結串列

# class Node():
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#         self.previous = None

# class Double_linked_list():
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def add_double_list(self, new_node):
#         if isinstance(new_node, Node):
#             if self.head == None:
#                 self.head = new_node
#                 self.tail = new_node
#             else:
#                 self.tail.next = new_node
#                 new_node.previous = self.tail
#                 self.tail = new_node
#     def print_list_from_head(self):
#         ptr = self.head
#         while ptr:
#             print(ptr.data)
#             ptr = ptr.next
#     def  print_list_from_tail(self):
#         ptr = self.tail
#         while ptr:
#             print(ptr.data)
#             ptr = ptr.previous
# link = Double_linked_list()
# n1 = Node(5)
# n2 = Node(6)
# n3 = Node(7)
# for i in [n1, n2, n3]:
#     link.add_double_list(i)
#     print("從頭部列印雙向串列")
#     link.print_list_from_head()
# print('從尾端列印雙向串列')
# link.print_list_from_tail()

## ex 3-1 把ch 3-2 的linked_list類別增加length()方法計算鏈結串列長度

# class Node():
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class Linked_list():
#     def __init__(self):
#         self.head = None
#     def print_list(self):
#         ptr = self.head
#         while ptr:
#             print(ptr.data)
#             ptr = ptr.next
#     def length(self):
#         count = 0
#         ptr = self.head
#         while ptr:
#             count+=1
#             ptr = ptr.next
#         print(count)

# link = Linked_list()
# link.head = Node(3)
# n2 = Node(4)
# n3 = Node(5)
# link.head.next = n2
# n2.next = n3
# link.length()

## ex 3-2 建立連結串列，並設計method可以判別搜索號碼出現幾次

# class Node():
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class Linked_list():
#     def __init__(self):
#         self.head = None
#     def print_list(self):
#         ptr = self.head
#         while ptr:
#             print(ptr.data)
#             ptr = ptr.next
#     def search(self, value):
#         ptr = self.head
#         count = 0
#         while ptr:
#             if ptr.data == value:
#                 count+=1
#             ptr = ptr.next
#         print(f'{value} 出現 {count} 次')

# link = Linked_list()
# link.head = Node(6)
# n2 = Node(7)
# n3 = Node(8)
# n4 = Node(7)
# link.head.next = n2
# n2.next = n3
# n3.next = n4
# link.print_list()
# link.search(6)
# link.search(7)

## ex 3-3 建立雙向串列，瀏覽一個星期，從頭瀏覽，及從尾瀏覽

class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

class Double_linked_list():
    def __init__(self):
        self.head = None
        self.tail = None
    def add_double_linked_list(self,node):
        new_node = node
        if isinstance(new_node,Node):
            if self.head == None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node
        return
    def print_list_from_head(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
    def print_list_from_tail(self):
        ptr = self.tail
        while ptr:
            print(ptr.data)
            ptr = ptr.previous

week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
link = Double_linked_list()
for day in week:
    new_node = Node(day)
    link.add_double_linked_list(new_node)
print('從頭列印')
link.print_list_from_head()
print('從尾端列印')
link.print_list_from_tail()
        
