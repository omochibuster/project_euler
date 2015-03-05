/*
	the answer is 4782
*/
//2014.11.19
#include<stdio.h>
int Carry(int [],int);
int main(void){
	int fibonacci1[1002] = {0},fibonacci2[1002] = {0};
	int arrayp = 0;//配列の要素数
	int i,j;
	fibonacci1[0] = fibonacci2[0] = 1;
	for(j = 3; ; j += 2){
		for(i = 0; i <= arrayp; i ++)
			fibonacci1[i] = fibonacci1[i] + fibonacci2[i];
		arrayp = Carry(fibonacci1,arrayp);
		if(arrayp >= 999)
			break;
		for(i = 0; i <= arrayp; i ++)
			fibonacci2[i] = fibonacci1[i] + fibonacci2[i];
		arrayp = Carry(fibonacci2,arrayp);
		if(arrayp >= 999)
			break;
	}
	printf("%d\n",j + 1);//forの途中で抜けるので+1する
	getchar();
	return 0;
}

int Carry(int fibonacci[1002],int arrayp){
	int i;

	for(i = 0; i <= arrayp; i ++)
		if(fibonacci[i] >= 10){
			fibonacci[i + 1] += 1;
			fibonacci[i] -= 10;
		}
	if(fibonacci[arrayp + 1] != 0)
		return arrayp + 1;
	return arrayp;
}