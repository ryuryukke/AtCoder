# <この問題の教訓>  出力例もきっちり読もう。
def main():
    n = int(input())
    a = list(map(int, input().split()))
    color = set()
    free = 0
    for score in a:
        if score < 3200:
            color.add(score//400)
        else:
            free += 1
    print(max(len(color),1), len(color)+free)
if __name__ == "__main__":
    main()
