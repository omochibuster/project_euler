// the answer is 669171001

//2014.11.25

/*
	対角に属する数値：1週目は2を足していくと次の対角の数値となる。
	　　　　　　　　　　　 2週目は4を足していくと次の対角の数値となる。
	これを利用したプログラム
*/
#include<stdio.h>

int main(void){
	int start = 1;
	int i,j;
	int addNum = 2;
	double addAll = 0;

	addAll += start;
	for(i = 1; i <= 500; i ++){
		for(j = 0; j < 4; j ++){
			start += addNum;
			addAll += start;
		}
		addNum += 2;
	}

	printf("%.0lf\n",addAll);
	getchar();
	return 0;
}