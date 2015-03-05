/*
the answer 6857
*/
//2014.09.07//
//2014.11.06 pdfŒ`®‚É•ÏX//
#include<stdio.h>
#include<math.h>
#define NUM 600851475143
int main(){
	double num = NUM;
	int factor = 2,
		 lastFactor,
		 maxFactor,
		 i;

	//2‚ÅŠ„‚é
	if(fmodl(num,factor) == 0)
	{
			lastFactor = factor;
			num /= factor;
			while(fmodl(num,factor) == 0)
				num /= factor;
	}else
		lastFactor = 1;

	factor = 3;
	maxFactor = sqrt(num);
	while(num > 1 && factor <= maxFactor)
	{
		if(fmodl(num,factor) == 0)
		{
			num /= factor;
			lastFactor = factor;
			while(fmodl(num,factor) == 0)
				num /= factor;
			maxFactor = sqrt(num);
		}
		factor += 2;
	}
	if(num == 1)
		printf("%d\n",lastFactor);
	else
		printf("%.0f", num);
	getchar();
	return 0;
}