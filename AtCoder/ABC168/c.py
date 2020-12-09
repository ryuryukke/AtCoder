import math
a, b, h, m = map(int, input().split())
theta_h = math.degrees((h/12)*2*math.pi)
theta_m = math.degrees((m/60)*2*math.pi)
theta = abs(theta_h - theta_m)
if theta > math.degrees(math.pi):
    theta = 2*(math.degrees(math.pi)) - theta
# theta = math.radians(theta)
print((a**2 + b**2 +(-2*a*b*math.cos(math.radians(theta))))**(1/2))
# print(math.sqrt((a**2) + (b**2) - (2*a*b*math.cos(theta))))
