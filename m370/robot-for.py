init,foods=map(int,input().split(' '))
locate=list(map(int,input().split(' ')))
leftF=0;rightF=0
max=-101;min=101#比大小給初值，題目有限定值位於-100~100之間
#分類每個食物的座標，看它在init左邊還是右邊記數
for food in locate:
    if food >init:
        rightF+=1
    else:
        leftF+=1
    if food>max:
        max=food
    if food<min:
        min=food
if rightF>leftF:
    print(rightF,max)
else:
    print(leftF,min)