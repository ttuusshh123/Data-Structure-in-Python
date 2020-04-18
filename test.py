# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.prev = None
# 		self.next = None

# 	def __str__(self):
# 		return "data->{}".format(self.data)
# p = Node(5)
# q = p
# q = Node(7)
# print(p.data)
# print(q.data)
# print(p.data)

###########################################
# arr = [2,3,7,8,10]
# memo = list(range(len(arr)))
# k = 11
##################################################
# n, m, g = map(int, input().split())
# t = list(map(int, input().split()))
# a = list(map(int, input().split()))
# time = []
# for i in range(len(t)-1):
#     time.append(t[i+1]-t[i])
# # print(time)
# init = len(a)
# for i in time:
#     for j in a:
#         if i >= j:
#             a.pop(j)
# fin = len(a)
# # print(fin)
# print(init-fin)
###########################################################
n,q = map(int, input().split())
l_ = [0 for i in range(n)]
for i in range(q):
    c,a,b = map(int, input().split())
    if c==0:
        for i in range(a, b+1):
            c[i]+=1
    elif c==1:
        count=0
        for i in range(a, b+1):
            if c[i]%3==0:
                count+=1
        print(count)   

