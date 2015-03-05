/*
	the answer is 443839
*/
//2014.12.03
#include<stdio.h>

int pow5(int);
int main(void){
	int i,sum,number,answer;
	answer = 0;

	//354294以上の数においては同値となるような数は存在しない
	for(i = 2; i <= 354294; i ++){
		sum = 0;
		number = i;
		while(number != 0){
			sum += pow5(number % 10);
			number /= 10;
		}
		if(i == sum){
			answer += sum;
		}
	}
	printf("%d\n",answer);
	getchar();
	return 0;

}

int pow5(int number){
	switch(number){
		case 0: return 0;
		case 1: return 1;
		case 2: return 32;
		case 3: return 243;
		case 4: return 1024;
		case 5: return 3125;
		case 6: return 7776;
		case 7: return 16807;
		case 8: return 32768;
		case 9: return 59049;
		default: return 0;
	}
}