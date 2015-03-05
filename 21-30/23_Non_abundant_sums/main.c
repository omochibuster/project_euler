/*
the answer is 4179871
*/
//2014.11.11//
/*
	is_abundant関数部分をもうちょっと改善できるかも
	2つの過剰数の和で表せない自然数を求めることに注意
	2つの過剰数の和で表せない過剰数も総和に含まれる
*/
#include<stdio.h>
#include<math.h>
#include<time.h>
#define LIMIT 28123
#define ARRAY_NUM 10000

int is_abundant(int,int[]);
int divitSum(int);
int main(void){
	int i,j,abundant[ARRAY_NUM],abundantSum = 0;
	int start,end;

	start = clock();//実行時間の計測

	for(i = 0; i < ARRAY_NUM; i ++)
		abundant[i] = 0;

	for(i = 1; i <= LIMIT; i ++){
		abundantSum += is_abundant(i,abundant);
	}
	end = clock();//実行時間測定終了
	printf("%d\n",abundantSum);
	printf("実行時間は %d ミリ秒でした\n",end - start);
	getchar();
	return 0;
}

int is_abundant(int number,int abundant[ARRAY_NUM]){
	int i,j;

	for(i = 0; abundant[i] != 0; i ++){
		for(j = i; abundant[j] != 0; j ++){
			if(abundant[i] + abundant[j] == number){
				if(divitSum(number) > number){
					while(abundant[++i] != 0);//空き配列まで線形探索
						abundant[i] = number;
				}
				return 0;
			}
		}
	}
	if(divitSum(number) > number){
		for(; abundant[i] != 0; i ++);//空き配列まで線形探索
			abundant[i] = number;
	}
	return number;
}

int divitSum(int number){
	int i,sum = 1;

	for(i = 2; i < number; i ++)
		if(number % i == 0)
			sum += i;
	return sum;
}