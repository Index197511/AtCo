#ABC036_C
n=int(input())
a=[int(input()) for i in range(n)]
s=sorted(set(a))
d={x:i for i,x in enumerate(s)}
for i in a:
    print(d[i])
#座標圧縮問題
'''
与えられた数字を圧縮する問題。
ソートした後に、setで重複を削除し、
二分探索で元の数字のインデックスを調べる
'''
