init,foods=map(int,input().split(' '))
locate=list(map(int,input().split(' ')))
locate.sort()
Lcount=0
if init>=locate[-1]:# |----| init=>init在locate左/右界外面，往一個方向可以全部吃到
    print(len(locate),locate[0])
    exit()
elif init<=locate[0]:
    print(len(locate),locate[-1])
    exit()
now_eat=locate[0]#temper，當前吃的東西座標
while now_eat<init:#從最左到現在位置算老鼠左邊食物數量
    now_eat=locate[Lcount+1]
    # print(locate[Lcount])
    Lcount+=1
Rcount=len(locate)-Lcount#右邊食物的數量用全部食物總數-左邊食物去求
if(Lcount>Rcount):
    print(Lcount,locate[0])
else:
    print(Rcount,locate[-1])