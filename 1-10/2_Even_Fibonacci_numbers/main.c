/*
the answer 4613732
*/
//2014.09.07//
//2014.11.05 pdf�A���S���Y���ɕύX
#include<stdio.h>
#define END 4000000 //���̐��܂�

int main(void){
	int a = 1,b = 1,c;
	int sum = 0;

	c = a + b;
	a = 0;
	
	while(c <= END)
	{
		sum += c;
		b = a;
		a = c;
		c = 4 * a + b;
	}
	printf("%d\n",sum);
	getchar();
	return 0;
}