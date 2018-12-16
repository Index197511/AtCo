#ボードの作成
#二次元配列で管理
#石を置く
#そこに石が置けるかの判定
#おけた場合ひっくり返す処理
#盤面の出力
#おけなくなった場合の処理

#ひっくり返すことができる石の判定
def look_up(x,y,player):
    direction=[-1,0,1]
    getable=[]
    for dx in direction:
        for dy in direction:
            if dx==0 and dy==0:
                continue
            depth=0
            while True:
                depth+=1
                rx=x+rx*depth
                ry=y+ry*depth
                tmp=[]
                if 0<=rx<board_size and 0<=ry<board_size:
                    req=game_board[ry][rx]
                    if req==None:
                        break
                    if req==player:
                        if len(tmp)!=0:
                            getable.extend(tmp)
                            break
                    else:
                        tmp.append((rx,ry))
        return getable

board_size=8
#盤面の作成
game_board=[]

for i in range(8):
    game_board.append([None for i in range(8)])
game_board[3][3]='black'
game_board[3][4]='white'
game_board[4][3]='white'
game_board[4][4]='black'
#石を置く
print('初手はblackの人です')
print('座標を(x,y)の形で指定してください')
print('例:4,5')
player = 'black'
while True:
    for i in game_board:
        for j in i:
            if j =='white':
                print('W',end='')
            elif j == 'black':
                print('B',end='')
            else:
                print('*',end='')
        print("\n",end="")

    x,y=map(int,input().split(','))
    if game_board[x-1][y-1] != None:
        print('そこには置くことができません')
        print('もう一度入力して下さい')
        continue
    qu=look_up(x,y,player)
    for x,y in getable:
        game_board[x][y]==player
    if player == 'white':
        player = 'black'
    else:
        player = 'white'
