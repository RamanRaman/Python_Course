x,y,r = eval(input())
a,b = eval(input())
flag = 1
while(a != 0 and b!= 0):
    if(((a - x)**2 + (b - y)**2) > r**2):
        flag = 0;
    a,b = eval(input())

if(flag == 0):
    print("NO")
else:
    print("YES")
