#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
long long totalPath = 0;
int GetNum(char* commands, int offset)//取指令之間的數字值(char轉int)
{

    int sum = 0, imove = 1;
    while (commands[offset + imove] >= 48 && commands[offset + imove] <= 57)
    {
        //printf("%c \n",commands[offset+imove]);
        sum *= 10;
        sum += commands[offset + imove] - 48;
        imove++;
    }
    return sum;
}
void DetectPath(char* commands, int offset)//(指令開頭位址,偏移量,總位移量)
{
    static int Step[2] = { -1,-1 },FLAG=0;//不會因為結束函數重置出值，儲存上一次T的結果，做奇偶判斷決定怎麼加回傳位移
    if (FLAG == 0)
    {
        Step[0] = GetNum(commands, offset);
        if (Step[1] != -1)
        {
            totalPath += abs(Step[1] - Step[0]); //printf("%d\n", totalPath);
        }
        FLAG = 1;
    }
    else if (FLAG == 1)
    {
        Step[1] = GetNum(commands, offset); 
        totalPath += abs(Step[1] - Step[0]);
        FLAG = 0;
    }
    
}
int Eloop(char* commands,int Lx, int offset)//(指令開頭位址,loop重複幾次(即L後面的個位數字),偏移量)
{
    
    int temp_offset=-99;//為了使迴圈不影響真正的offset，故再複製一個
    
    for (int j = 0; j < Lx; j++)//迴圈跑Lx次
    {
        temp_offset = offset + 1;//剛進函式時offset是指向L後面那個數字(Lx)，加1再判斷
        while (*(commands + temp_offset) != 'E')
        {
            if (*(commands + temp_offset) == 'L')//loop內又嵌套一個loop
            {
                temp_offset =Eloop( commands,commands [temp_offset + 1] - '0', temp_offset +1);
            }
            else if (*(commands + temp_offset) == 'T')
            {
                DetectPath(commands, temp_offset);
                temp_offset += 2;
            }
            temp_offset++;
        }
        
    }
    return temp_offset;
    
}
int main() {
    char nowBit;
    char* commands = NULL;
    commands = (char*)malloc(1 * sizeof(char));
    int MAXINDEX = 0;
    while (cin>>nowBit)//scan commands
    {
        commands = (char*)realloc(commands, (MAXINDEX + 1) * (sizeof(char)));
        commands[MAXINDEX] = nowBit;
        MAXINDEX++;

    }
    //    printf("%d",MAXINDEX);
    //int  totalPath = 0;
    for (int i = 0; i < MAXINDEX; i++)//把輸入的指令遍歷過一次
    {

        if (commands[i] == 'T')
        {
            DetectPath(commands, i);
            i += 2;//讀取進度跳過T後面的兩位數字，已經取好值了
            continue;
        }
        if (commands[i] == 'L')
        {
            //原型宣告Eloop(char* ,int , int)//(指令開頭位址,loop重複幾次(即L後面的個位數字),偏移量)
            i=Eloop(commands, commands[i + 1] - '0', i+1);
        }
        

    }

    //    for(int i=0;i<MAXINDEX;i++)
    //    {
    //        printf("%c",commands[i]);
    //    }
    //printf("%d\n", totalPath);
    cout<<totalPath<<endl;
    free(commands);

}
