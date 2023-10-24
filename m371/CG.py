#輸入N行，每行M個整數。
'''
      M
    |‾ ‾ |
  N |    |
    |    |
'''
def HorizonOffset(n,newM):#跳過水平空格
    global board,M
    
    if board[n][newM]!=-1:
        return newM
    else:
        while board[n][newM]==-1:#把target放到非-1的值，若加到M還是-1，就回傳原本的index-1
            newM+=1
            if newM>=M:return newM-1
        return newM
def VerticalOffset(newN,m):#跳過垂直空格
    global board,N
    if board[newN][m]!=-1:
        return newN
    else:
        while board[newN][m]==-1:#把target放到非-1的值，若加到M還是-1，就回傳原本的index-1
            newN+=1
            if newN>=N:return newN-1
        return newN
N,M=map(int,input().split(' '))
board=[]
score=0
for herz in range(N):#inssert every row numbers
    board.append(list(map(int,input().split(' '))))

havebanned=1 #判斷這次迴圈有沒有消除數字的flag
while (havebanned):#只要這回合有消掉數字就再做一次，因為會有消掉中間的數字導致多一組可以消除
    havebanned=0
    Nindex=-1
    #檢查橫排相鄰
    for rowN in board:#用board裡面的list去跑
        Nindex+=1
        cnacleFlag=1
        while (cnacleFlag):
            cnacleFlag=0
            for elementNM in range(len(rowN)-1):#elementNM是row的index
                this=HorizonOffset(Nindex,elementNM);next=HorizonOffset(Nindex,elementNM+1)#求水平相鄰索引值
                if this==next:#安全機制，如果不小心取到相同index不比較
                    continue
                # print(rowN,'----',this,next)
                if (rowN[this]==rowN[next]) and (rowN[this]!=-1 and rowN[next]!=-1):
                    score+=rowN[this]
                    # print("\n比較:",this,next)
                    cnacleFlag=1;havebanned=1
                    rowN[this]=-1;rowN[next]=-1
    #檢查直排相鄰
    for colM in range(M):
        cnacleFlag=1
        while(cnacleFlag):
            # print(board,'\n------',)
            cnacleFlag=0
            for rowN in range(N-1):
                aboveN=VerticalOffset(rowN,colM);underN=VerticalOffset(rowN+1,colM)#求垂直相鄰索引值
                if aboveN==underN:#安全機制，如果不小心取到相同index不比較
                    continue
                if (board[aboveN][colM]==board[underN][colM]) and \
    (board[aboveN][colM]!=1 and board[underN][colM]!=1):
                    print('compire:',board[aboveN][colM],board[underN][colM])
                    score+=board[aboveN][colM]
                    cnacleFlag=1;havebanned=1
                    board[aboveN][colM]=-1;board[underN][colM]=-1


print(score)