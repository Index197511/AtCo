A[::-1]#文字列Aを反転させる
A=list()
m=[]#リストの作成
if 3 in A#リストAの中に3があるかサーチする
A[1:4]#リスト内のインデックスが1,2,3のものを返す
A.append()#()内の値をリストの最後尾に追加する
A.insert(1,'A')#Aをインデックスが1の部分に挿入する
A.remove('A')#リストA内の'A'という値を削除する。複数個ある場合は一番前のみ
A.replace('A','B')#リストA内のAという値をすべてBに変える
A.pop(3)#リストAのインデックスが3の値を取り出す
A.clear()#リストAの中身を全削除する
A.reverse()#リストAを反転させる
A.sort()#昇順ソート
A.sort(reverse=True)#降順ソート
S=sorted(A)#Aを昇順ソートしたリストを返す。元のリストへの干渉はない
del A[1]#A[1]を削除する
del A#リストAを削除する
hex()#()内の値を16進数に変換する
oct()#()内の値を8進数に変換する
bin()#()内の値を2進数に変換する
pow(A,B,C)#A**B%Cと同じ値を返す。Cはなくてもよい。
math.floor(X)#小数点第一位を切り捨てた値を返す
math.ceil(x)#小数点第一位を切りあげた値を返す
round(x)#小数点第一位を四捨五入する
print(''.join(S))#リストS内の値をすべて連結して出力する
print('%02d'%(h))#桁数を指定して出力できる。d=int f=float s=string
A={'A':1,'B':2}#ディクショナリの作成
print(A['A'])#keyがAの値を出力
zip(*A)#リストAの行と列を入れ替える
[list(map(int,input().split())) for i in range(n)]#縦nと横入力数の二次元配列の作成
print('hello',end='')#文末の改行取り消し
math.py#円周率の呼び出し
math.factorial()#()内の階乗を返す
list(itertools.permutations(s,3))#リスト内から3つを選んで順列を作成
len(list(itertools.permutations(s,3)))#順列の総数を返す
list(itertools.combinations(s,3))#リスト内から3つの組み合わせを作成
list(itertools.product(s,repeat=3))#リスト内から重複を許した順列を作成
list(itertools.combinations_with_replacement(s,3))#リスト内から重複を許した組み合わせ
A=sum(i[1] for i in B)
#B(二次元配列)の2つめのみの要素の和
sS=sorted(s,key=lambda x:(x[0],x[1]))
#要素を2つ指定してソートできる
文字列.upper()#文字列を大文字に変換する
文字列.lower()#文字列を小文字に変換する
b=[for i in a if x<30]#リスト内から条件に合うものを摘出する。
