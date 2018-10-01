import math
checker = False
a=int(input())
integers_list = [int(i) for i in input().split()]
for i in integers_list :
    if i == 1:
        checker = True



if checker == True:
    print("HARD")
else :
    print("EASY")
