/*
	the answer is 76576500
*/

#include<stdio.h>

int calcSumTotal(int );

int main(void){
	int num = 1, total = 0, count, i;

	while(1){
		count = 0;
		total = calcSumTotal(num ++);
		for(i = 1; i * i <= total; i ++){
			if(total % i == 0){
				if(i * i != total)
					count += 2;
				else{
					count ++;
					break;
				}
			}
		}
		if(count >= 500){
			printf("%d\n",total);
			break;
		}
	}
	getchar();
	return 0;
}

int calcSumTotal(int num){
	int total = 0, i;

	for(i = 1; i <= num; i ++)
		total += i;
	return total;
}