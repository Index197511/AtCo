dic = {'a':input(), 'b':input(), 'c':input()}
turn = 'a'
while True:
    if len(dic[turn])==0:
        break
    next_turn = dic[turn][0]
    dic[turn] = dic[turn][1:]
    turn = next_turn
print(turn.upper())
