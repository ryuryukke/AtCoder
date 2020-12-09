s = input()
cand = []
ans = [0] * len(s)

# RLの位置を把握
for i in range(len(s)-1):
    if s[i] == "R" and s[i+1] == "L":
        cand.append(i)
for j in range(len(cand)):
    if j == 0:
        lst_l = s[:cand[j]]
        lst_r = s[cand[j]+2:cand[j+1]]
    elif j == len(cand)-1:
        lst_l = s[cand[j-1]+2:cand[j]]
        lst_r = s[cand[j]+2:]
    else:
        lst_l = s[cand[j-1]+2:cand[j]]
        lst_r = s[cand[j]+2:cand[j+1]] 
    num_R = len([i for i in lst_l if i == "R"])
    num_L = len([i for i in lst_r if i == "L"])
    num = num_R + num_L
    j = cand[j]
    if num % 2 == 0:
        ans[j:j+2] = [num//2+1, num//2+1]
    else:
        if num_R == 0 or num_L == 0:
            if num_R == 0:
                ans[j:j+2] = [num_L-(num_L//2)+1, num_L//2+1]
            else:
                ans[j:j+2] = [num_R//2+1, num_R-(num_R//2)+1]
        else:
            ans[j:j+2] = [num_R+1, num_L+1]
print(*ans)