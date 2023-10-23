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
        while board[n][content]==-1:
            content+=1
            if content>=M:return content-1
        return content
N,M=map(int,input().split(' '))
board=[]
score=0
for herz in range(N):#inssert every row numbers
    board.append(list(map(int,input().split(' '))))
#先檢查橫排相鄰
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
                rowN[this]=-1
                rowN[next]=-1
print(score)
# print(board)