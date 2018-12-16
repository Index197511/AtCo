sx,sy,tx,ty=map(int,input().split())
print('U'*(ty-sy)+'R'*(tx-sx)+'D'*(ty-sy)+'L'*(tx-sx)+'LU'+'U'*(ty-sy)+'R'*(tx-sx)+'RDRD'+'D'*(ty-sy)+'L'*(tx-sx)+'LU')
