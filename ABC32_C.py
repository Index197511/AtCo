import sys
n,k=map(int,input().split())
s=[int(input()) for i in range(n)]
if 0 in s:
    print(n)
    sys.exit()
pr=0
st=1
j=0
#尺取り法
for i in range(n):#iは右端の座標
    st*=s[i]#左端から右端までの積をstに代入していく
    if st<=k:#積が規定値よりも小さい間はそれまでの長さを比較して代入していく
        pr=max(pr,i-j+1)
    else:#積が規定値よりも大きい場合は積の和を左端の値で割って入っていないこととする。
        st=st//s[j]
        j+=1#スタート地点(左端の座標)を一つ右にずらす
print(pr)
