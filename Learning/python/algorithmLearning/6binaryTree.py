## 建立binary tree 記得左大右小，從根節點開始
## 建立binary tree 需要元素有 建立 刪除 搜尋
## binary tree 種類有 
## full binary tree 除了子葉以外都有兩個子節點
## complete binary tree 除了最深層的以外其他曾節點全滿
## balanced binary tree 每個節點的2個子節點深度不可差超過一
## perfect binary tree 全滿
## 每i層有最多2^(i-1個節點) 
## 一顆完美二元樹深度為節點數為2^k-1
## n個節點總共有logn +1 層
## 搜尋時間為 O(logn)
## 左子節點 = 2*index + 1(右:+2)
## 父節點 = floor((index -1)/2)

## ch6-1 用6個隨機數字建立一個二元樹，列印出資料及索引

# def create_btree(tree, data):
#     for i in range(len(data)):
#         level = 0 # 代表在樹中移動的index
#         # 判斷大小比對，決定左移或是右移
#         while tree[level]:
#             if data[i] > tree[level]:
#                 level = level*2 + 2
#             else:
#                 level = level*2 + 1
#         tree[level] = data[i]
#         print(i,tree)

# tree = [0]*8
# data = [10, 21, 5, 9, 13, 28]
# create_btree(tree,data)
# # tree會被函式影響
# for i in range(len(tree)):
#     print(f'二元樹陣列tree[{i}] = {tree[i]}')

## ch6-2 用串列建立tree並用中序列印

# 中序列印:左中右，由小到大排好

# class Node():
#     def __init__(self, data=None):
#         self.data = data
#         self.left = None
#         self.right = None
#     def insert(self, data):
#         # 三層考量+recursive call:先check有無根結點
#         # 再check要往左還是往右，最後確認是否存在該節點
#         if self.data:
#             if data < self.data:
#                 if self.left:
#                     self.left.insert(data)
#                 else:
#                     self.left = Node(data)
#             else:
#                 if self.right:
#                     self.right.insert(data)
#                 else:
#                     self.right = Node(data)
#         else:
#             self.data = data
#     def inorder(self):
#         if self.left:
#             self.left.inorder()
#         print(self.data)
#         if self.right:
#             self.right.inorder()
#             # 進入到inorder後只要該節點左邊沒東西就會把自己印出來
# # 用node內部去chain不是像前面寫linkedlist是用外部去建立node
# tree = Node()
# datas = [10, 21, 5, 9, 13, 28]
# for i in datas:
#     tree.insert(i)
# tree.inorder()

## ch6-3 用前序列印實作tree

# class Node():
#     def __init__(self, data=None):
#         self.data = data
#         self.left = None
#         self.right = None
#     def insert(self, data):
#         if self.data:
#             if self.data > data:
#                 if self.left:
#                     self.left.insert(data)
#                 else:
#                     self.left = Node(data)
#             else:
#                 if self.right:
#                     self.right.insert(data)
#                 else:
#                     self.right = Node(data)
#         else:
#             self.data = data
#     def preorder(self):
#         print(self.data)
#         if self.left:
#             self.left.preorder()
#         if self.right:
#             self.right.preorder()

# tree = Node()
# datas = [10, 21, 5, 9, 13, 28]
# for i in datas:
#     tree.insert(i)
# tree.preorder()

## ch6-4 用後序列印實作tree

# # 所謂前後中序列印，指的是存取到該node時，該node值被印出的順序
# class Node():
#     def __init__(self, data=None):
#         self.data = data
#         self.left = None
#         self.right = None
#     def insert(self, data):
#         if self.data:
#             if self.data > data:
#                 if self.left:
#                     self.left.insert(data)
#                 else:
#                     self.left = Node(data)
#             else:
#                 if self.right:
#                     self.right.insert(data)
#                 else:
#                     self.right = Node(data)
#         else:
#             self.data = data
#     def postorder(self):
#         if self.left:
#             self.left.postorder()
#         if self.right:
#             self.right.postorder()
#         print(self.data)

# tree = Node()
# datas = [10, 21, 5, 9, 13, 28]
# for i in datas:
#     tree.insert(i)
# tree.postorder()

## ch6-5 建立樹並且增加search method

class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data
    def search(self, data):
        # 第一層考量大小值比對，確認是否存在並繼續recursive call
        if self.data > data:
            if not self.left:
                # 因為只有一條路徑如果該點不存在就必定不存在
                return str(data)+"不存在"
            return self.left.search(data)
        elif self.data < data:
            if not self.right:
                return str(data)+"不存在"
            return self.right.search(data)
        else:
            return str(data)+"找到了"
        
tree = Node()
datas = [10, 21, 5, 9, 13, 28]
for i in datas:
    tree.insert(i)
print(tree.search(21))
print(tree.search(100))
