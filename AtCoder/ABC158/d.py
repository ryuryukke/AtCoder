"""
<<計算量の工夫>>
dequeによる先頭,末尾に対する要素の挿入の計算量をO(1)にする
毎回,reverseしているようだと計算量が増えるので,revというフラグをつけて元の文字列が
反転している状態かどうかを保持しておいて最後に状態変化させる.
その際,元の文字列が反転しているかどうかで,挿入の時の先頭,末尾も逆にすることに注意.
"""
def main():
    from collections import deque
    s = deque(input().split())
    q = int(input())
    rev = False
    for i in range(q):
        l = input().split()
        if l[0] == "2":
            flag = int(l[1])
            flag -= 1
            if rev: flag ^= 1
            if flag == 1:
                s.append(l[2])
            else:
                s.appendleft(l[2])
        else:
            rev = not rev
    if rev:
        s.reverse()
        print("".join(s))
    else:
        print("".join(s))

if __name__ == "__main__":
    main()
