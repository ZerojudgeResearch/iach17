#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <cstdlib>
using namespace std;
int MAP[101][101] = { 0 };
int boss_life[500];
struct boss
{
	//初始座標
	int now_x;
	int now_y;
	//每回合移動步數
	int move_x;
	int move_y;
};
int  check(int k, int rangex, int rangey, boss* boss)
{


	if (boss_life[k])//魔王是活的
	{
		if (boss->now_x > rangex || boss->now_y > rangey|| boss->now_x<0|| boss->now_y<0)//檢查出界
		{
			boss_life[k] = 0;
			return 1;//本次死魔王
		}
		else
		{
			//判斷腳下炸彈
			if (MAP[boss->now_x][boss->now_y] == 1)//踩到炸彈
			{
				boss_life[k] = 0;
				MAP[boss->now_x][boss->now_y] = 2;//本回合爆炸中(模擬多隻魔王踩到同一點一起爆炸的效果)，之後若有魔王踩到也會爆炸
				return 1;//本次死魔王
			}
			else if (MAP[boss->now_x][boss->now_y] == 2)//踩到爆炸中點位
			{
				boss_life[k] = 0;
				return 1;//本次死魔王
			}
		}

	}
	return 0;//safe or這隻魔王已經死了。回傳0使呼叫的if不成立，不用扣魔王數
}
void move(int rangex, int rangey, int k, boss* boss)
{
	if (boss_life[k])//魔王是活的
	{
		//移動+放炸彈(MAP座標變1)
		MAP[boss->now_x][boss->now_y] = 1;//放炸彈
		boss->now_x += boss->move_x;
		boss->now_y += boss->move_y;
	}

}
int main()
{
	
	int n, m, k;
	/* n,m決定地圖大小
		k:魔王數量
	*/
	//scanf_s("%d%d%d", &n, &m, &k);
	cin >> n >> m >> k;
	//題目未說明好m*n的長寬，湊出來的結果
	//用xor做變數交換
	m ^= n;
	n ^= m;
	m ^= n;
	for (int i = 0; i < k; i++)
	{
		boss_life[i] = 1;
	}
	boss blist[500];
	for (int kc = 0; kc < k; kc++)
	{

		for (int i = 0; i < 4; i++)
		{
			switch (i)//給予魔王們初始屬性
			{
			case 0:
				//scanf_s("% d", &blist[kc].now_x);
				cin >> blist[kc].now_x;
				break;
			case 1:
				//scanf_s("% d", &blist[kc].now_y);
				cin >> blist[kc].now_y;
				break;
			case 2:
				//scanf_s("% d", &blist[kc].move_x);
				cin >> blist[kc].move_x;
				break;
			case 3:
				//scanf_s("% d", &blist[kc].move_y);
				cin >> blist[kc].move_y;
				break;
			default:
				break;
			}
		}
	}
	//試著輸出魔王屬性 
//	for (int kc = 0; kc < k; kc++)
//	{
//		cout<<kc<<":"<<blist[kc].now_x<<" "<<blist[kc].now_y<<" "<<blist[kc].move_x<<" "<<blist[kc].move_y<<endl;
//	}
	int boss_count = k, bomb_count = 0;
	//K:魔王數量 
	while (boss_count != 0) {
		//printf("|");
		bomb_count = 0;
		for (int kc = 0; kc < k; kc++)
		{
			move(m, n, kc, &blist[kc]);//移動魔王
		}

		for (int kc = 0; kc < k; kc++)//移動完檢查
		{
			if (check(kc, m, n, &blist[kc]))
			{
				boss_count--;
			}
		}


		//結算、整理地圖上的炸彈 
		for (int index_m = 0; index_m < m; index_m++)
		{
			for (int index_n = 0; index_n < n; index_n++)//數炸彈 
			{
				if (MAP[index_m][index_n] == 1)
				{
					bomb_count++;
				}
				else if (MAP[index_m][index_n] == 2)
				{
					MAP[index_m][index_n] = 0;//把爆炸中狀態清除
				}
			}
		}

	}
	printf("%d", bomb_count);
	return 0;

}

