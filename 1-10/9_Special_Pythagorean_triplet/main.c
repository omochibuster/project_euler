/*
200,375,425‚ÌŽž
the answer = 31875000
*/
#include<stdio.h>

int main(){
	int i,j,k,ans1,flg;

	for(i = 1, flg = 0; i < 1000; i ++){
		for(j = i + 1; j + i < 1000; j ++){
			ans1 = i * i + j * j;
			for(k = j + 1; i + j + k <= 1000; k ++){
			if(ans1 == k * k)
				if(i + j + k == 1000){
					flg = 1;
					break;
				}
			}
			if(flg)
				break;
		}
		if(flg)
			break;
	}
	
	printf("%d %d %d %d\n",i,j,k,i * j * k);
	return 0;
}