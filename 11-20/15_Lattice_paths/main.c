/*
	the answer is 137846528820
*/
//2014.11.18
#include<stdio.h>
#define END 1//パスカルの三角形の両端は1
int main(void){
	int pathNum = 20;//経路の数
	double pascal[pathNum + 1];
	double newPascal[pathNum + 1];
	int j, i;

//パスカルの三角形を作成する
	for(i = 0, j = 1; i < pathNum; i ++){//jを初期化しないとi=0の時20行目で引っかかる
		newPascal[0] = END;
		if(i != 0){
			for(j = 1; j <= i; j ++)
				newPascal[j] = pascal[j - 1] + pascal[j];
		}
		newPascal[j] = END;
		for(j = 0; j < i + 2; j ++)
			pascal[j] = newPascal[j];
	}

//作成したパスカルの三角形を足しpathNum * pathNumの経路数を求める
	for(j = pathNum; j > 0; j --){
		for(i = 0; i < j; i ++){
			pascal[i] += pascal[i + 1];
		}
	}
	printf("%.0lf\n",pascal[0]);
	getchar();
	return 0;
}