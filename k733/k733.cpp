#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
long long totalPath = 0;
int GetNum(char* commands, int offset)//�����O�������Ʀr��(char��int)
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
void DetectPath(char* commands, int offset)//(���O�}�Y��},�����q,�`�첾�q)
{
    static int Step[2] = { -1,-1 },FLAG=0;//���|�]��������ƭ��m�X�ȡA�x�s�W�@��T�����G�A���_���P�_�M�w���[�^�Ǧ첾
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
int Eloop(char* commands,int Lx, int offset)//(���O�}�Y��},loop���ƴX��(�YL�᭱���Ӧ�Ʀr),�����q)
{
    
    int temp_offset=-99;//���F�ϰj�餣�v�T�u����offset�A�G�A�ƻs�@��
    
    for (int j = 0; j < Lx; j++)//�j��]Lx��
    {
        temp_offset = offset + 1;//��i�禡��offset�O���VL�᭱���ӼƦr(Lx)�A�[1�A�P�_
        while (*(commands + temp_offset) != 'E')
        {
            if (*(commands + temp_offset) == 'L')//loop���S�O�M�@��loop
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
    for (int i = 0; i < MAXINDEX; i++)//���J�����O�M���L�@��
    {

        if (commands[i] == 'T')
        {
            DetectPath(commands, i);
            i += 2;//Ū���i�׸��LT�᭱�����Ʀr�A�w�g���n�ȤF
            continue;
        }
        if (commands[i] == 'L')
        {
            //�쫬�ŧiEloop(char* ,int , int)//(���O�}�Y��},loop���ƴX��(�YL�᭱���Ӧ�Ʀr),�����q)
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
