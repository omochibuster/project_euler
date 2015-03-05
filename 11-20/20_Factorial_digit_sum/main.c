/*
	the answer is 648
*/
//2014.11.19
#include<stdio.h>

#define END 100
int digitCalc(int value[],int count);
int main(void){
	int value1[100] = {0},digit[5],value2[100] = {0};
	int count = 0, digitsum = 0;
	int i,j,k,ivalue,sp;

	value1[0] = 1;
	for(i = 1; i <= END; i ++){
		ivalue = i;
		sp = 0;
		while(ivalue != 0 && sp < 5){
			digit[sp++] = ivalue % 10;
			ivalue /= 10;
		}
		sp --;
		for(j = 0; j <= count; j ++){
			value2[j] = value1[j];
			value1[j] = 0;
		}
		while(sp >= 0){
			for(j = 0; j <= count && digit[sp] != 0; j ++)
				value1[j] += value2[j] * digit[sp];
			if(sp != 0)
				for(k = 0;k <= count; k ++)
					value1[k] *= 10;
			for(j = 0; j <= count; j ++)
				while(value1[j] >= 100000){
					value1[j + 1] += 1;
					value1[j] -= 100000;
					if(j + 1 > count)
						count ++;
				}
				sp--;
		}
	}
	printf("%d\n",digitCalc(value1,count));
	getchar();
	return 0;
}

int digitCalc(int value[100],int count){
	int i,digitsum = 0;

	for(i = 0; i <= count; i ++)
		while(value[i] != 0){
			digitsum += value[i] % 10;
			value[i] /= 10;
		}
	return digitsum;
}