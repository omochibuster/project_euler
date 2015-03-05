/*
the answer is 104743
*/

//2014.11.08 pdfŒ`®‚É•ÏX//

#include<stdio.h>
#include<math.h>
#include"prime.h"
#define LIMIT 10001
int main(){
	int count=1,candidate = 1;

	while(count != LIMIT){
		candidate = candidate + 2;
		if(isPrime(candidate))
			count ++;
	}
	printf("%d\n",candidate);
	getchar();
	return 0;
}