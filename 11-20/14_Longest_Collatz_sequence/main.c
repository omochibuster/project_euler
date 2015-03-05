/*
	the answer is 837799
*/
//2014.11.16//
#include<stdio.h>
#include<math.h>

int main(void){
	int count,i,max = 0, tmp, maxNum = 0;
	double num;

	for(i = 1; i <= 1000000; i ++){
		count = 1;
		num = tmp = i;
		while(num > 1){
			if(fmod(num,2) == 0)
				num /= 2;
			else
				num = num * 3 + 1;
			count ++;
		}
		if(max < count){
			maxNum = tmp;
			max = count;
		}
	}
	printf("%d\n",maxNum);
	getchar();
	return 0;
}