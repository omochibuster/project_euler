/*
	the answer is 100
*/

//2014.12.15
#include<iostream>
using namespace std;

int Minimum(int, int);
int Comprime(int, int);
int CheckSameNumber(int, int);
int JudgementDivisor(int Denominator1, int numerator1,int Denominator2,int numerator2);

int main(void){

	double answer = 1;

	for(int Denominator = 11; Denominator < 100; Denominator ++){
		for(int numerator = 10; numerator < Denominator; numerator ++){
			if(Comprime(Denominator, numerator) == 1){
				int commonNum = CheckSameNumber(Denominator, numerator);
				if(commonNum > 0){
					int num1, num2;
					if(Denominator % 10 == commonNum){
						num1 = Denominator / 10;
					}else{
						num1 = Denominator % 10;
					}
					if(numerator % 10 == commonNum){
						num2 = numerator / 10;
					}else{
						num2 = numerator % 10;
					}
					//printf("%d %d %d %d\n",Denominator, numerator, num1, num2);
					if(JudgementDivisor(Denominator, numerator, num1, num2) == 1){
						answer = answer * num1 / num2;
					}
				}
			}
		}
	}
	cout << answer;
	getchar();
	return 0;
}

int Minimum(int a, int b){
	if(a < b){
		return a;
	}
	return b;
}

//互いに素ならば0を返す
int Comprime (int Denominator, int numerator){
	int min = Minimum(Denominator,numerator);

	for(int i = 2; i <= min; i ++){
		if(Denominator % i == 0 && numerator % i == 0){
			return 1;
		}
	}
	return 0;
}

//num1とnum2に共通する数字を返却する
int CheckSameNumber(int num1, int num2){
	int numArray[100];
	int num1DigitCount;

	for(num1DigitCount = 0; num1 != 0; num1DigitCount ++){
		numArray[num1DigitCount] = num1 % 10;
		num1 /= 10;
	}

	for(int i = 0; num2 != 0; i ++){
		int num = num2 % 10;
		num2 /= 10;
		for(int j = 0; j < num1DigitCount; j ++){
			if(numArray[j] == num)
				return num;
		}
	}
	return -1;
}

int JudgementDivisor(int Denominator1, int numerator1,int Denominator2,int numerator2){
	if(numerator2 == 0){
		return 0;
	}
	if((double)numerator1 / numerator2 * Denominator2 == Denominator1){
		return 1;
	}
	return 0;
}