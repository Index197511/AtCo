#逆元とは…割り算を掛け算に直すこと
#今回はmod=10*9+7で割ったあまり
#(a*b*c)%modとa*b%mod*c%modは等しい
import math
h,w=map(int,input().split())
mod=10**9+7
a=math.factorial(h+w-2)%mod#階乗は掛け算なので先に%modで桁数を減らす
#フェルマーの小定理を利用して逆元を求める
#求めたい数を**mod-2して%modする
b=pow(math.factorial(h-1),mod-2,mod)%mod
c=pow(math.factorial(w-1),mod-2,mod)%mod
print(a*b*c%mod)

'''
任意のPが素数の時、
a^-1=a^p-2(mod p)
b/a=b*a^p-2　と置き換えられる
'''
