#ABC036_B
n=int(input())
s=reversed([input() for i in range(n)])
for i in zip(*s):
    print(''.join(i))


#before
#4
#ooxx
#xoox
#xxxx
#xxxx

#after
#xxxo
#xxoo
#xxox
#xxxx
