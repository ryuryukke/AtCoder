# ans = []
# for i in range(1, 5):
#     ans.append(i)
# print(*ans)

# ans = []
# for i in range(5, 1, -1):
#     ans.append(i)
# print(*ans)
# stack = [1,2,3]
# p = stack.pop()
# print(stack)

from functools import lru_cache

text1 = input()
text2 = input()

@lru_cache(maxsize=None)
def helper(ptr1, ptr2):
    if ptr1 == len(text1) or ptr2 == len(text2):
        return " "
    elif text1[ptr1] == text2[ptr2]:
        return text1[ptr1] + helper(ptr1+1, ptr2+1)
    else:
        a = helper(ptr1+1, ptr2) 
        b = helper(ptr1, ptr2+1)
        return a if len(a) > len(b) else b
        
print(helper(0, 0))





