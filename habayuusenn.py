h,w=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
c=[list(input()) for _ in range(h)]

c[sy-1][sx-1]=0
que=[(sy-1,sx-1)]#キューの中にスタート地点の座標を入れ、スタートから探索
cnt=0

while True:
  que_next=[]#次に調べる値を格納するためのリストを作成
  cnt+=1
  for y,x in que:#キューから座標の値を取り出し代入、探索
    for i,j in ((0,1),(1,0),(0,-1),(-1,0)):#現在位置の前後左右の値を調べるループ
        if c[y+i][x+j]=='.':#進めるマスかどうか判定する
          c[y+i][x+j]=cnt#もし進めるマスならば、そこまでにかかった手数を代入する
          que_next.append((y+i,x+j))
  que=que_next
  if (gy-1,gx-1) in que_next:#もしキューの中にゴールの座標が入っていたらbreak
    break
print(cnt)#現在の手数を出力する
