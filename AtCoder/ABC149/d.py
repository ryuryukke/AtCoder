n, k = map(int, input().split())
R, S, P = map(int, input().split())
t = input()
ans = 0
hand = []
for i in t:
    if i == "r":
        hand.append("p")
    if i == "s":
        hand.append("r")
    if i == "p":
        hand.append("s")
for i, h in enumerate(t):
    if i >= k:
        if h == "r":
            if hand[i-k] != "p":
                ans += P
            else:
                if i+k <= n-1:
                    if hand[i+k] == "r":
                        hand[i] = "s"
                    else:
                        hand[i] = "r"
                else:
                    hand[i] = "r"
        if h == "s":
            if hand[i-k] != "r":
                ans += R
            else:
                if i+k <= n-1:
                    if hand[i+k] == "s":
                        hand[i] = "p"
                    else:
                        hand[i] = "s"
                else:
                    hand[i] = "s"
        if h == "p":
            if hand[i-k] != "s":
                ans += S
            else:
                if i+k <= n-1:
                    if hand[i+k] == "p":
                        hand[i] = "r"
                    else:
                        hand[i] = "p"
                else:
                    hand[i] = "p"
    else:
        if h == "r":
            ans += P
        if h == "s":
            ans += R
        if h == "p":
            ans += S
print(ans)
