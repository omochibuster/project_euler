// the answer is -59231

//2014.11.25

#include<stdio.h>
#include<math.h>

int CheckPrime(int x);
int Calc(int, int);

int main(void){
	int i,j;
	int primeAmount,maxprimeAmount,keepa,keepb;

	maxprimeAmount = 0;
	keepa = keepb = 0;
	
	for(i = -999; i < 1000; i ++){
		for(j = 2; j < 1000;){
			primeAmount = Calc(i,j);
			if(maxprimeAmount < primeAmount){
				maxprimeAmount = primeAmount;
				keepa = i;
				keepb = j;
			}
			if(j > 2)
				j += 2;
			else
				j ++;
		}
	}

	printf("%d\n",keepa * keepb);

	getchar();
	return 0;
}


int CheckPrime(int x){
	int i,end;

	if(x < 2)
		return -1;

	if(x == 2)
		return 0;

	end = sqrt(x);
	//合成数の場合は-1,素数の場合のみ0を返す
	if(x % 2 == 0)
		return -1;
	for(i = 3; i <= end; i += 2){
		if(x % i == 0){
			return -1;
		}
	}
	return 0;
}

int Calc(int a,int b){
	int i;

	for(i = 0;; i ++){
		if(CheckPrime( ( (i * i) + (a * i) + b)) != 0)
			return i;
	}
	return 0;
}