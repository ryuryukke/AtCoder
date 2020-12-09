# N = int(input())
# if N <= 10**3:
#     for i in range(1, N+1):
#         ans = 0
#         for x in range(1, 13):
#             for y in range(1, 13):
#                 for z in range(1, 13):
#                     if (x+y+z)**2-x*y-y*z-z*x == i:
#                         ans += 1
#         print(ans)
# else:
#     table = [0] * N
#     for i in range(1, 10**3):
#         ans = 0
#         for x in range(1, 14):
#             for y in range(1, 14):
#                 for z in range(1, 14):
#                     if (x+y+z)**2-x*y-y*z-z*x == i:
#                         ans += 1
#         table[i-1] += ans
#     for j in range(10**3, N+1):
#         ans = 0
#         for x in range(14, 41):
#             for y in range(14, 41):
#                 for z in range(14, 41):
#                     if (x+y+z)**2-x*y-y*z-z*x == j:
#                         ans += 1
#         table[j-1] += ans
#     print(*table, sep="\n")




# # for i in range(1, N+1):
# #     ans = 0
# #     for x in range(1, 41):
# #         for y in range(1, 41):
# #             for z in range(1, 41):
# #                 if (x+y+z)**2-x*y-y*z-z*x == i:
# #                     ans += 1
# #     print(ans)

# #include <iostream>
# using namespace std;
# int main(){
#     int N, ans, x, y, z, i;
#     cin >> N;
#     if (N <= 10*10*10){
#         for (i = 1; i <= N; i++){
#             ans = 0;
#             for (x = 1; x < 14; x++){
#                 for (y = 1; y < 14; y++){
#                     for (z = 1; z < 14; z++){
#                         if (x*x + y*y + z*z + x*y + y*z + z*x == i){
#                             ans++;
#                         }
#                     }
#                 }
#             }
#             cout << ans;
#             cout << "\n";
#         }
#         return 0;
#     }else{
#         for (i = 1; i < 10*10*10; i++){
#             ans = 0;
#             for (x = 1; x < 41; x++){
#                 for (y = 1; y < 41; y++){
#                     for (z = 1; z < 41; z++){
#                         if (x*x + y*y + z*z + x*y + y*z + z*x == i){
#                             ans++;
#                         }
#                     }
#                 }
#             }
#             cout << ans;
#             cout << "\n";
#         }
#         for (i = 10*10*10; i <= N; i++){
#             ans = 0;
#             for (x = 1; x < 41; x++){
#                 for (y = 1; y < 41; y++){
#                     for (z = 1; z < 41; z++){
#                         if (x*x + y*y + z*z + x*y + y*z + z*x == i){
#                             ans++;
#                         }
#                     }
#                 }
#             }
#             cout << ans;
#             cout << "\n";
#         }
#         return 0;
#     }
# }

N = int(input())

def count(a, b, c):
    return (a+b+c)**2-a*b-b*c-c*a

table = [0] * (N+1)
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            tmp = count(x, y, z)
            if tmp <= N:
                table[tmp] += 1
print(*table[1:], sep="\n")
