/*
the answer is 232792560
*/
//2014.09.09//
//2014.11.08 pdfå`éÆÇ…ïœçX//

#include<stdio.h>
#include<math.h>
#define ARRAY_SIZE 8
int main(){
	int k = 20,
		 n = 1,
		 check = 1,
		 limit,i;
	int p[ARRAY_SIZE] = {2,3,5,7,11,13,17,19};
	int a[10];

	limit = sqrt(k);
	for(i = 0; i < ARRAY_SIZE && p[i] < k; i ++){
		a[i] = 1;
		if(check == 1)
			if(p[i] <= limit)
				a[i] = floor(log(k) / log(p[i]));
			else
				check = 0;
		n = n * pow(p[i],a[i]);
	}
	printf("%d\n",n);
	getchar();
	return 0;
}