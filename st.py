from math import log
num = eval(input())
osn = 2
while(osn < num):
    if(int(log(num,osn)) == float(log(num,osn))):
        print("YES")
        osn = 1
        break
    osn+=1
if(osn != 1):
    print("NO")
