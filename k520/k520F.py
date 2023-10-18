##優化版本，執行速度較快)
def DToBin(decNum):
    return str(bin(decNum)[2:])
def tran_dec(bits:list,base):#bits:欲求值的任意長度的位元array;base:進制
    decSum=0
    for i in range(len(bits)):
        decSum+=pow(base,i)*bits[i]
    return decSum
#二分搜
#幸運基數，找某一最小進制表示輸入值，並使其為全1

SEARCH=int(input())
MAX_bit=0
luckBin=1
for i in ((DToBin(SEARCH))):
    if (i=="0"):
        luckBin=0#轉換為二進制後有某一位有非1的bit，代表不是全1
    MAX_bit+=1#決定最多要有幾位元的1
if(int(luckBin)):#轉二進制就是全1，找到幸運基數，可以直接輸出，結束程式
    print(2)
    exit()
now_bits=[1,1,1]

#找到幸運基數的flag
FOUND=0
left=2;right=SEARCH-1;mid=None#界定左界、右界;宣告中間項變數
for count in range(MAX_bit):#外層for跑到1最多的數量(SEARCH-1)
    left=2
    startV=tran_dec(now_bits,left)
    if(startV>SEARCH):#左界已經大於要找的數，代表佔有1的位元太多，加一個1continue
            now_bits.append(1)
            continue
    while(left<=right):
        mid=(left+right)//2
        midV=tran_dec(now_bits,mid)
        if(midV>SEARCH):
            right=mid-1#右界向左移動
        elif(midV<SEARCH):
            left=mid+1#左界向右移動
        else:
            if(midV==SEARCH):#找到幸運基數
                print(mid)
                FOUND=1
            break
    #跳出while
    if(FOUND):
        exit()
    now_bits.append(1)
if(not(FOUND)):
    print(SEARCH-1)