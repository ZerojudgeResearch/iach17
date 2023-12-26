N,M=map(int,input().split(' '))
'''
	  M
	|‾ ‾ |
  N |    |
	|    |
'''
space=[]#放置水管的空間(二維)
for i in range(N):
    space.append(input())
#上,右,下,左
X=[1,1,1,1];I=[1,0,1,0];H=[0,1,0,1];L=[1,1,0,0];
T7=[0,0,1,1];J=[1,0,0,1];F=[0,1,1,0]
UP="XILJ"
RIGHT="XHLF"
DOWN="XI7F"
LEFT="XH7J"
#所有管子列表:XIHL7FJ
visted=[None]*N#造訪清單，大小為N*M，和spacr相同
for i in range(N):
    visted[i] = [0]*M
# print(space)
# print(visted)
# print("-"*10)
WORK=[]#從(0,0)開始走訪，tube連通0個
maxtube=0
for ScreenY in range(N):
    for ScreenX in range(M):
        if visted[ScreenY][ScreenX]==1 or space[ScreenY][ScreenX]=='0':#已造訪或沒有管子
            visted[ScreenY][ScreenX]=1
            continue
        else:
            # if space[ScreenY][ScreenX] in UP:
            #     WORK.append((ScreenX,ScreenY,DOWN))
            # if space[ScreenY][ScreenX] in RIGHT:
            #     WORK.append((ScreenX,ScreenY,LEFT))
            # if space[ScreenY][ScreenX] in DOWN:
            #     WORK.append((ScreenX,ScreenY,UP))
            # if space[ScreenY][ScreenX] in LEFT:
            #     WORK.append((ScreenX,ScreenY,RIGHT))
            WORK.append((ScreenX,ScreenY,"XIHL7FJ"))
            SumTube=0
            while(WORK!=[]):
                flag=0
                # print(WORK,"%")
                # print(space[nowY][nowX])
                nowX,nowY,shape=WORK.pop(0)#X座標,y座標,可允許的方向水管
                #已經拜訪過了或沒有管子
                if visted[nowY][nowX] ==1 or space[nowY][nowX] in '0':
                    continue
                if space[nowY][nowX] in UP and (space[nowY][nowX] in shape ) and nowY-1>=0:
                    flag=1
                    WORK.append((nowX,nowY-1,DOWN))
                if space[nowY][nowX] in RIGHT and space[nowY][nowX] in shape and nowX+1<M:
                    flag=1
                    WORK.append((nowX+1,nowY,LEFT))
                if space[nowY][nowX] in DOWN and space[nowY][nowX] in shape and nowY+1<N:
                    flag=1
                    WORK.append((nowX,nowY+1,UP))
                if space[nowY][nowX] in LEFT and space[nowY][nowX] in shape and nowX-1>=0:
                    flag=1
                    WORK.append((nowX-1,nowY,RIGHT))
                visted[nowY][nowX]=1#把現在這格加入已造訪清單
                if flag:
                    SumTube+=1
                # print(visted,SumTube)
            #每次while代表一坨連續的水管，出while代表把連續的通道走完，要和之前(最大坨數量)比較決定要不要覆蓋，因為要取最大連通值
            if SumTube>maxtube:
                maxtube=SumTube
print(maxtube)