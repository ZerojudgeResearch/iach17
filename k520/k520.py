def DToBin(decNum):
    z=[]
    while True:
        if decNum//2<1:
            if decNum%2==1:
                z.append('1')
            break    
        else:
            answer=str(decNum%2)  #a值是decNum Mod 2的值，即所求二進位各個位元(最後才做顛倒的動作，使用reverse函式)
            z.append(answer)
            decNum=decNum//2 #decNum值是每次自己的值與2取商數的結果 
    z.reverse() #顛倒列表順序
    Strz="".join(z) #把z的列表型態換成字串
    return Strz
def tran_dec(bits:list,base):#bits:欲求值的任意長度的位元array;base:進制
    decSum=0
    for i in range(len(bits)):
        decSum+=pow(base,i)*bits[i]
    return decSum

#二分搜
#幸運基數，找某一最小進制表示輸入值，並使其為全1

SEARCH=int(input())
MAX_bit=len(DToBin(SEARCH))#取二進制SEARCH值，決定最多要有幾位元的1
# print(MAX_bit)
now_bits=[];
for i in range(MAX_bit):#產生全1的arr，找某一最小基數的進制等於SEARCH值
    now_bits.append(1)

#找到幸運基數的flag
FOUND=0

for count in range(MAX_bit):#外層for跑到1最多的數量(SEARCH-1)
    left=2;right=SEARCH-1;mid=-1#界定左界、右界;宣告中間項變數
    while(left<=right):
        mid=(left+right)//2
        startV=tran_dec(now_bits,left)
        midV=tran_dec(now_bits,mid)
        endV=tran_dec(now_bits,right)
        if(startV>SEARCH):#左界已經大於要找的數，代表佔有1的位元太多，跳出while扣一個bit
            break
        if(midV>SEARCH):
            right=mid-1#右界向左移動
        elif(midV<SEARCH):
            left=mid+1#左界向右移動
        else:
            if(midV==SEARCH):#找到幸運基數
                print(mid)
                FOUND=1
            break
        
    #若沒找到，跳出while，不執行下面if敘述
    if(FOUND):
        break
    now_bits.pop()
    