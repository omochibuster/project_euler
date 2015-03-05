/*
	the answer is 9183
*/
//2014.12.02//
#include<stdio.h>
#include<math.h>

#define N 100

int checkSameNumber(int, int, int);
int checkPower(int,int);
int checkPrimeNumber(int);

int main(void){
	int i,j,k;
	int nump = 0,temp;

	for(i = 2; i <= N; i ++){
		if(checkPrimeNumber(i) == 0){
			nump += (N - 1);
			continue;
		}
		for(j = 2; j <= N; j ++){
			temp = checkPower(i,j);
			if(temp == -1){
				nump ++;
			}
		}
	}

	printf("%d\n",nump);
	getchar();
	return 0;
}


int checkPrimeNumber(int Number){
	int i;

	if(Number == 2)
		return 0;

	if(Number % 2 == 0){
		return -1;
	}

	for(i = 3; i * i <= Number; i += 2){
		if(Number % i == 0){
			return -1;
		}
	}
	return 0;
}

//同じ値が既に存在するか。
int checkPower(int base,int exponent){
	int i;
	int count = 1;

	for(i = 2;i < base; i ++){
		while(base % i == 0 && base != i){
			base /= i;
			count ++;
		}
		//同じ値が存在しない
		if(count != 1 && base != i){
			return -1;
		}
		//同じ値が存在する
		if(base == i){
			if(exponent * count <= N){
				return 0;
			}else{
				return checkSameNumber(base, exponent, count);
			}
		}
	}
	return -1;
}

//同じ値があれば0を返す
int checkSameNumber(int base, int exponent, int count){
	int originExponent,originBase,keep;
	int i;

	originBase = pow(base, count);
	originExponent = exponent;
	exponent = exponent * count;
	keep = base;

	for(i = 2; ; i ++){
		if(exponent % i == 0){
			base = pow(base,i);
			exponent /= i;
			//同じ値が見つからなかった。
			if(base >= originBase){
				return -1;
			}else if(exponent <= N){
				return 0;
			}
			base = keep;
			exponent = originExponent;
		}
	}
	return 0;
}