/*
	the answer is 31626
*/
//2014.11.19
#include<stdio.h>

#define END 10000

int main(void){
	int i,j,amiSum = 0,divisor,divDiv;

	for(i = 2; i < END; i ++){
		divisor = divDiv = 0;
		for(j = 1; j < i; j ++)
			if(i % j == 0)
				divisor += j;
		for(j = 1; j < divisor; j ++)
			if(divisor % j == 0)
				divDiv += j;
		if(i == divDiv && divisor > divDiv)
			amiSum += i + divisor;
	}
	printf("%d\n",amiSum);
	getchar();
	return 0;
}