def main(n, s):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
    tmp = (sorted(s, reverse = True))

    for i in range(n):

        if s[i] != tmp[0]:
          print(tmp[0])
        else:
          print(tmp[1])

if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))
    main(n, s)
