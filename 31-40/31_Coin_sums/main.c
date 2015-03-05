/*
	the answer is 73682
*/

//for文の判定処理に改善の余地あり。
#include<stdio.h>

#define LIMIT 200

int main(void){
	int p1,p2,p5,p10,p20,p50,p100,p200;
	int count = 0;

	for(p1 = 0; p1 <= LIMIT; p1 ++){
		for(p2 = 0; p1 + p2 <= LIMIT; p2 += 2){
			for(p5 = 0; p1 + p2 + p5 <= LIMIT; p5 += 5){
				for(p10 = 0; p1 + p2 + p5 + p10 <= LIMIT; p10 += 10){
					for(p20 = 0; p1 + p2 + p5 + p10 + p20 <= LIMIT; p20 += 20){
						for(p50 = 0; p1 + p2 + p5 + p10 + p20 + p50 <= LIMIT; p50 += 50){
							for(p100 = 0; p1 + p2 + p5 + p10 + p20 + p50 + p100 <= LIMIT; p100 += 100){
								for(p200 = 0; p1 + p2 + p5 + p10 + p20 + p50 + p100 + p200 <= LIMIT; p200 += 200){
									if(p1 + p2 + p5 + p10 + p20 + p50 + p100 + p200 == 200){
										count ++;
									}
								}
							}
						}
					}
				}
			}
		}
	}
	printf("%d\n",count);
	return 0;
}