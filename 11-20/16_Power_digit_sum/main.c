/*
	the answer is 1366
*/
//2014.11.18
#include<stdio.h>

#define POWERS 1000//2のべき乗数
int main(void){
	int num[100] = {0};
	int count, add, j, i;//countは使っている配列の数

	count = add = 0;
	num[0] = 1;

//2のPOEWRS乗を求める
	for(i = 0; i < POWERS; i ++){
		for(j = 0; j <= count; j ++)
			num[j] *= 2;//<<を使用するのもあり
		for(j = 0; j <= count; j ++){
			if(num[j] >= 100000){
				num[j + 1] += 1;
				num[j] -= 100000;
				if(j == count)
					count ++;
			}
		}
	}

//各桁の総和を求める
	for(i = 0; i <= count; i ++){
		while(num[i] != 0){
			add += num[i] % 10;
			num[i] /= 10;
		}
	}

	printf("%d\n",add);
	getchar();
	return 0;
}