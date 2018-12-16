A=list()
m=[]#listの作成方法
3 in A#リストAの中に3があるかサーチする
A[1:4]#リストの中からインデックスが1，2，3のものを返す
len(A)#リストAの要素数を返す
min(A)#リストAの最小値を返す
max(A)#リストAの最大値を返す
A.append()#()内の値をリストの最後尾に追加する
A.insert(0,値)#値を0番の位置に挿入する
A.remove()#()内の値を削除する
C.replace('A','B')#文字列のAという文字をBに置き換える
str[::-1]#strに入っている文字列を反転させる
del A[1]#A[1]を削除する
del A#リストAを削除する
A.pop()#リストAの最後の値を取り出す
A.popleft()#リストAの頭の値を取り出す
A.clear()#リストの中身を全て削除する
A.reverse()#リストの中身を反転させる
del list[i]#リストのi番目を削除
A.sort()#昇順ソート
A.sort(reverse=True)#降順ソート
A=[i for i in B if i>0]#リストBから指定の条件を満たすものを取り出す
sorted(A)#sortされたリストを新しく作成するため元のリストは何も干渉されないメリットがある
abs(値)#値の絶対値を返す
any(コンテナ名)#コンテナから任意の値を取り出す
hex()#()内の値を16進数に変換する
oct()#()内の値を8進数に変換する
bin()#()内の値を2進数に変換する
pow(A,B)#AのB乗の値を得る
pow(A,B,C)#A**B%Cと同じ値を返す
math.floor(x)#xの小数第一位を切り捨てた値を返す
math.ceil(x)#xの小数第一位を切り上げた値を返す
round(x)#xの小数第一位を四捨五入した値を返す
if A in list[A]#in演算子の左側の値が右辺のリスト内にあるかどうかを探索する
print(''.join(S))#リストSを全て連結して出力する
print('%02d:%02d:%02d'%(h,m,N))#桁数を指定して出力できる。d=int f=float s=string
dic={'A':1,'B':2}#辞書の作成
print(dic(A))#キーがAの値を出力する
sum(リスト名)#リストの総和を出力
set(リスト名)#重複を削除する
zip(*リスト名)#二次元配列の行と列を入れ替える
[list(map(int,input().split())) for i in range(n)]#縦ｎ、横入力数の二次元配列の作成
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))#二次元配列の作成
print("hello",end='')#文末の改行取り消し
x=list(x)#xをリスト化する。xを文字列にした場合のみ適用可能
math.pi#円周率を返す
.split(',')#文字列に含まれている','で区切ってリストで返す。
math.factorial()#()内の階乗を返す
list(itertools.permutations(s,3))#リストの中から順列の組み合わせを全列挙してリスト化
len(list(itertools.permutations(s,3)))#順列の総数を返す
list(itertools.combinations(s,3))#リストsから3つの組み合わせを作成
list(itertools.product(s,repeat=3))#リストsから重複を許した順列
list(itertools.combinations_with_replacement(s,3))#重複を許した重複組み合わせ
文字列.upper()#文字列を大文字に変換する
文字列.lower()#文字列を小文字に変換する
b=[i for i in a if x<30]#リストaから条件に一致するものをリストbに追加
