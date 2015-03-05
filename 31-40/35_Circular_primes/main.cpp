/*
the answer is 55
*/

//2014.12.16
#include<iostream>
#include<cmath.h>
using namespace std;

int isPrime(int number);
int calcDigit(int);
int isCircularPrimes(int number, int digit);

int main(void){
	int CircularPrimesCount = 0;
	for(int i = 2; i < 1000000; i ++){
		int digit = calcDigit(i);
		if(isCircularPrimes(i, digit) == 1){
			CircularPrimesCount ++;
		}
	}

	cout << CircularPrimesCount << endl;
	getchar();
	return 0;
}

//素数の場合は1を返す//
int isPrime(int number){

	if(number == 1)
		return 0;//素数でない
	else if(number < 4)
		return 1;// 2と3は素数
	else if(fmod(number,2) == 0)
		return 0;
	else if(number < 9)
		return 1;//9より小さい自然数の偶数は上で消しているので残りは素数となる
	else if(fmod(number,3) == 0)
		return 0;
	else{
		int end = floor(sqrt(number));//ｎの素因数の最大値
		int comparNumber = 5;
		while(comparNumber <= end){
			if(fmod(number, comparNumber) == 0)
				return 0;
			if(fmod(number, comparNumber + 2) == 0)
				return 0;
			//fmod(number, comparNumber + 4)は3の倍数なので判定しなくてよい
			comparNumber += 6;
		}
		return 1;
	}
}

int calcDigit(int number){
	int  digit;
	for(digit = 0; number != 0; digit ++){
		number /= 10;
	}
	return digit;
}

int isCircularPrimes(int number, int digit){
	if(digit == 1){
		if(isPrime(number) == 1){
			return 1;
		}else{
			return 0;
		}
	}
	for(int i = 0; i < digit; i ++){
		if(isPrime(number) == 0){
			break;
		}
		int temp = fmod(number, pow(10, (digit - 1)));
		//cout << number << " " << temp << endl;
		number /= pow(10, (digit - 1));
		temp *=  10;
		number += temp;

		if(i == digit - 1){
			return 1;
		}
	}
	return 0;
}