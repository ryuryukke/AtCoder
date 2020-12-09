# かっこ列の整合性の問題
# 典型的手法として,スタック的に考える。
def main():
    from collections import deque
    n = int(input())
    s = input()
    need_left, need_right = 0, 0
    for i in s:
        if i == "(":
            need_right += 1
        else:
            if need_right == 0:
                need_left += 1
            else:
                need_right -= 1
    for i in range(need_left):
        s = "(" + s
    for j in range(need_right):
        s = s + ")"
    print(s)
if __name__ == "__main__":
    main()
