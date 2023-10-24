#輸入N行，每行M個整數。
'''
      M
    |‾ ‾ |
  N |    |
    |    |
'''
def offset(n,content):#跳過水平空格
    # print("C:",content)
    global board,M
    
    if board[n][content]!=-1:
        return content
    else:
        while board[n][content]==-1:#把target放到非-1的值，若加到M還是-1，就回傳原本的index-1
            content+=1
            if content>=M:return content-1
        return content
def checkL(newN,m):#跳過垂直空格
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
#先檢查橫排相鄰
havebanned=1 #判斷這次迴圈有沒有消除數字的flag
while (havebanned):
    havebanned=0
    Nindex=-1
    for rowN in board:
        Nindex+=1
        cnacleFlag=1
        while (cnacleFlag):
            cnacleFlag=0
            for elementNM in range(len(rowN)-1):#elementNM是row的index
                this=offset(Nindex,elementNM);next=offset(Nindex,elementNM+1)#求相鄰索引值
                if this==next:#安全機制，如果不小心取到相同index不比較
                    continue
                # print(rowN,'----',this,next)
                if (rowN[this]==rowN[next]) and (rowN[this]!=-1 and rowN[next]!=-1):
                    score+=rowN[this]
                    # print("\n比較:",this,next)
                    cnacleFlag=1
                    havebanned=1
                    rowN[this]=-1
                    rowN[next]=-1
    for colM in range(M):
        cnacleFlag=1
        while(cnacleFlag):
            print(board,'\n------',)
            cnacleFlag=0
            for rowN in range(N-1):
                aboveN=checkL(rowN,colM);underN=checkL(rowN+1,colM)#求垂直相鄰索引值
                if aboveN==underN:#安全機制，如果不小心取到相同index不比較
                    continue
                if (board[aboveN][colM]==board[underN][colM]) and \
    (board[aboveN][colM]!=1 and board[underN][colM]!=1):
                    print('compire:',board[aboveN][colM],board[underN][colM])
                    score+=board[aboveN][colM]
                    cnacleFlag=1
                    havebanned=1
                    board[aboveN][colM]=-1
                    board[underN][colM]=-1


print(score)
# print(board)