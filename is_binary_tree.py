# Is binary Search Tree or not

class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
arr_input=[1,2,3,4,5,6,7]

def balance(b):
    if(b is None):
        return -1
    if(not b.left is None):
        left=1+balance(b.left)
    if (not b.right is None):
        right=1+balance(b.right)
    if(abs(left-right)==2):
        if(left<right):
            if(b.right.left is None):
                b.right.left=b
            else:
                temp=b.right.left
                b.right.left = b
                b.left.right=temp
        elif(left>right):
            if (b.right.right is None):
                b.left.right = b
            else:
                temp = b.left.right
                b.left.right = b
                b.right.left = temp
    return left if(left>right) else right
def insert(t,data):
    cur=t
    print(cur.data)
    while(not cur is None):
        if(cur.data>data):
            if(cur.left is None):
                temp=node(data)
                cur.left=temp
                break
            else:
                cur=cur.left
                continue
        elif(cur.data<data):
            if(cur.right is None):
                temp=node(data)
                cur.right=temp
                break
            else:
                cur=cur.right
                continue

# Balanced Binary Tree (sorted)
for i in range(0,len(arr_input)):
    if(i==0):
        temp = node(arr_input[i])
        head=temp
    else:
        insert(head,arr_input[i])
        balance(head)
# Preorder Traversal in Iterative

arr_cur=[head]
visited=[]
while(not arr_cur is None):
    cur = arr_cur.pop(-1)
    if(not cur.left is None):
        if(not cur.left in visited):
            arr_cur.extend(cur,cur.left)
            continue
    else:
        print(cur.data,end="")
        visited.append(cur)
        continue
    if(not cur.right is None):
        if(not cur.right in visited):
            arr_cur.extend(cur.right)
    else:
        print(cur.data,end="")
        visited.append(cur)
