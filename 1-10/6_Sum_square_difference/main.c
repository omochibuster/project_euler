/*
the answer is 25164150
*/
//2014.11.08 pdfå`éÆÇ…ïœçX//
#include<stdio.h>
#include<math.h>
#define LIMIT 100

int main(){
	int sum,sum_sq;

	sum = (LIMIT * (LIMIT + 1)) / 2;
	sum_sq = ((2 * LIMIT + 1) * (LIMIT + 1) * LIMIT) / 6;
	printf("%.0f\n",pow(sum,2) - sum_sq);
	return 0;
}