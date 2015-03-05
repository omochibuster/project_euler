/*
the answer = 142913828922
*/

#include<stdio.h>

int main(){
	double sum = 2;
	int i,j;

	for(i = 3; i <2000000; i += 2){
		printf("%d\r",i);
		for(j = 3; j <= i; j += 2){
			if(i % j == 0)
				break;
			if( j >= i / 2){
				sum += i;
				break;
			}
		}
	}
	printf("%.0f\n",sum+3);
	return 0;
}