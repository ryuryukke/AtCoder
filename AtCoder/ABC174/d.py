n = int(input())
c = list(input())
print(len([i for i, j in zip(sorted(c), c) if i != j])//2)





# flag = False
# ans = 0
# for i in range(n-1):
#     if c[i] == "W" and c[i+1] == "R":
#         flag = True
#         break
# if not flag:
#     print(0)
#     exit()
# for i in range(n//2):
#     if c[i] == "R" and c[n-i-1] == "W":
#         continue
#     else:
#         if c[i] == "W" and c[n-i-1] == "R":
#             c[i] = "R"
#             c[n-i-1] = "W"
#             ans += 1
#         elif c[i] == "W" and c[n-i-1] == "W":
#             for j in range(n-i,i+1,-1):
#                 if c[j] == "R":
#                     c[i] = "R"
#                     c[j] = "W"
#                     break
#             ans += 1
#         elif c[i] == "R" and c[n-i-1] == "R":
#             for j in range(i+1, n-i-1):
#                 if c[j] == "W":
#                     c[n-i-1] = "W"
#                     c[j] = "R"  
#                     break
#             ans += 1
# print(ans)

























# # if c[0] == "W" and c[-1] == "R":
# #     ans += 1
# #     c[0], c[-1] = "R", "W"
# #     for i in range(n-1):
# #         if c[i] == "W" and c[i+1] == "R":
# #             ans += 1
# #     print(ans)
# # elif c[0] == "R" and c[-1] == "W":
# #     for i in range(n-1):
# #         if c[i] == "W" and c[i+1] == "R":
# #             ans += 1
# #     print(ans)
# # elif c[0] == "R" and c[-1] == "R":
# #     for i, v in enumerate(c):
# #         if v == "W":
# #             c[i] = "R"
# #             c[-1] = "W"
# #             break
# #     ans += 1
# #     for i in range(n-1):
# #         if c[i] == "W" and c[i+1] == "R":
# #             ans += 1
# #     print(ans)
# # else:
# #     for i, v in enumerate(reversed(c)):
# #         if v == "R":
# #             c[n-1-i] = "W"
# #             c[0] = "R"
# #             break
# #     ans += 1
# #     for i in range(n-1):
# #         if c[i] == "W" and c[i+1] == "R":
# #             ans += 1
# #     print(c)
# #     print(ans)