/*
	the answer is 983
*/
//2014.11.23//

/*
	1000以下の自然数nにおいて 1 / n　の巡回節は最高で n - 1桁となる。
	10^m - 1 を割り切ることができればそのnの巡回節はm桁となる。
*/
#include<stdio.h>
#include<math.h>

int main(void){
	int i,cycle,maxCycle = 0,Remainder;

	for(i = 3; i < 1000; i += 2){
		Remainder = 0;
		cycle = 1;//1にしないと結果が合わない　理由は不明
		if(i % 5 == 0)
			i += 2;
		while(1){
			Remainder = (Remainder * 10 + 9) % i;
			cycle ++;
			if(Remainder == 0){
				if(maxCycle < cycle)
					maxCycle = cycle;
				break;
			}
		}
	}
	printf("%d\n",maxCycle);
	getchar();
	return 0;
}