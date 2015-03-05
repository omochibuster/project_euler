/*
the answer is 40730
*/

//2014.12.16
#include<iostream>
using namespace std;

int factorial(int NaturalNumber);
int main(void){
	int answer = 0;

	for(int i = 3; i < 9999999; i ++){
		int num = i;
		int FactorialSum = 0;
		while(num != 0){
			FactorialSum += factorial(num % 10);
			num /= 10;
		}
		if(FactorialSum == i){
			answer += i;
		}
	}
	cout << answer << endl;
	getchar();
	return 0;
}

int factorial(int NaturalNumber){

	if(NaturalNumber >= 10 || NaturalNumber < 0){
		return 0;
	}

	switch(NaturalNumber){
		case 0:
		case 1:
			return 1;
		case 2:
			return 2;
		case 3:
			return 6;
		case 4:
			return 24;
		case 5:
			return 120;
		case 6:
			return 720;
		case 7:
			return 5040;
		case 8:
			return 40320;
		case 9:
			return 362880;
	}
	return 0;
}