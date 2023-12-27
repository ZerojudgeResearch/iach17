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
            WORK.append((ScreenX,ScreenY))
            SumTube=0
            while(WORK!=[]):
                flag=0
                # print(WORK,"%")
                # print(space[nowY][nowX])
                nowX,nowY=WORK.pop(0)#X座標,y座標
                #已經拜訪過了或沒有管子
                if visted[nowY][nowX] ==1 or space[nowY][nowX] == '0':
                    continue
                #判斷方向、鄰居可以銜接、沒有越界
                if space[nowY][nowX] in UP and nowY-1>=0 and space[nowY-1][nowX] in DOWN:
                    flag=1
                    WORK.append((nowX,nowY-1))
                if space[nowY][nowX] in RIGHT and nowX+1<M and space[nowY][nowX+1] in LEFT:
                    flag=1
                    WORK.append((nowX+1,nowY))
                if space[nowY][nowX] in DOWN and nowY+1<N and space[nowY+1][nowX] in UP:
                    flag=1
                    WORK.append((nowX,nowY+1))
                if space[nowY][nowX] in LEFT and nowX-1>=0 and space[nowY][nowX-1] in RIGHT:
                    flag=1
                    WORK.append((nowX-1,nowY))
                visted[nowY][nowX]=1#把現在這格加入已造訪清單
                if flag:
                    SumTube+=1
                # print(visted,SumTube)
            #每次while代表一坨連續的水管，出while代表把連續的通道走完，要和之前(最大坨數量)比較決定要不要覆蓋，因為要取最大連通值
            if SumTube>maxtube:
                maxtube=SumTube
print(maxtube)