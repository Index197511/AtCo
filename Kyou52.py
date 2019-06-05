# a = すねけスタート、b = ふぬけスタート a < b
# c = すぬけゴール、 d = ふぬけゴール
n, a, b, c, d = map(int, input().split())
s = list(input())
s = s + ["."] * 5

for i in range(n-1):
    if s[i] == "#" and s[i+1] == "#":
        print("No")
        exit()


s[a-1] = "A"
s[b-1] = "B"
s[c-1] = "C"
s[d-1] = "D"
# s = field s = goal
#print(s)
if c > d:
    potisinonB = b - 1
    # move A to goal
    i = a - 1
    while(True):

        if s[i] == "C":
            break

        if s[i] == "B":
            if s[i+1] == "#":
                s[i] = "A"
                s[i+2] = "B"
                s[i-1] = "."
                potisinonB += 2
            else:
                s[i+1] = "A"
                s[i-1] = "."
                i += 1
            #print(1)



        elif s[i] == "#" and s[i+1] == "B":
            if s[i+2] == "#":
                s[i+3] = "B"
                s[i+1] = "A"
                s[i-1] = "."
                potisinonB += 2
                i += 1
            else:
                s[i+2] = "B"
                s[i+1] = "A"
                s[i-1] = "."
                potisinonB += 1
                i += 1
            #print(2)


        elif s[i] == "#":
            s[i+1] = "A"
            s[i-1] = "."
            i += 1
            #print(3)


        else:
            s[i] = "A"
            s[i-1] = "."
            #print(4)
        i += 1


        print(s)
    #print(potisinonB)
    if potisinonB > d - 1:
        print("No")
    else:
        print("Yes")
    exit()

print("Yes")
