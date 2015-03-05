/*
	the answer is 2783915460
*/
//2014.11.19
#include<stdio.h>
#define NUM 10
#define END 1000000

void swap(char [],int,int);
void sortaccending_notinclude_head(char [],int);

int main(void){
	int i,limit,sum = 0,p=0;
	char num[11] = {'0','1','2','3','4','5','6','7','8','9'};

	while(p != NUM - 1){
	//階乗の計算
		limit = 1;
		for(i = 1; i < NUM - p; i ++)
			limit *= i;
	//ENDが含まれる範囲を求める
		for(i = p; i < NUM; i ++){
			sum += limit;
			if(sum >= END)
				break;
		}
		sum -= limit;//調整
		swap(num,p,i);
		p++;
		sortaccending_notinclude_head(num,p);
	}
	printf("%s\n",num);
	getchar();
	return 0;		
}
void swap(char num[10],int a,int b){
	char temp;

	temp = num[a];
	num[a] = num[b];
	num[b] = temp;
}

void sortaccending_notinclude_head(char num[],int p){
	int i,j;
	char temp;

	for(i = p; i < NUM; i ++)
		for(j = i + 1; j < NUM; j ++){
			if(num[i] > num[j])
				swap(num,i,j);
		}
}