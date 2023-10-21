N,TARGET,L,R=map(int,input().split())
# ^ n格，目標，每次左/右可移動的步數
local=list(map(int,input().split()))
# ^ 每一格地上傳送點座標

def go(now):#查表完成傳送動作
    global local
    if now<0 or now>=N:
        return -1
    else:
        return local[now]
def add_son(ROOT):
    global next_layertemp,L,R,visted
    goL=go(ROOT-L);goR=go(ROOT+R)#接下來的位置算法:左/右移動，踩到傳送點移動過去
    #走出界外的節點不會加入待造訪清單走下去
    if goL!=-1 and not(goL in visted):
        next_layertemp.add(goL)
        visted.add(goL)
    if goR!=-1 and not(goR in visted):
        next_layertemp.add(goR)
        visted.add(goR)
Tstep=1#Totalstep:操作次數記數，輸出就要它
now_layerNode=[]
next_layertemp=set()
visted=set()
add_son(0)
while(1):
    if len(next_layertemp)==0:#沒有子節點了，結束程式
        print(-1)
        exit()
    now_layerNode=list(next_layertemp.copy())
    next_layertemp.clear()
    while(now_layerNode!=[]):
        if now_layerNode[0]==TARGET:
            print(Tstep)
            exit()
        add_son(now_layerNode[0])#append子樹，放在next_layertemp占存，等等會丟給now_layer執行
        now_layerNode.pop(0)
    
    Tstep+=1