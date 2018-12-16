import collections
N=int(input())
m=[]
for i in range(N):
    m.append(input())
pre_ans=collections.Counter(m)#
print(pre_ans.most_common()[0][0])#最も多い要素をカウントしてそれを返す
