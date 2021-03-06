#include<math.h>
int isPrime(int n){
	int r,f;
//素数の場合は1を返す//
	if(n == 1)
		return 0;//素数でない
	else if(n < 4)
		return 1;// 2と3は素数
	else if(fmod(n,2) == 0)
		return 0;
	else if(n < 9)
		return 1;//9より小さい自然数の偶数は上で消しているので残りは素数となる
	else if(fmod(n,3) == 0)
		return 0;
	else{
		r = floor(sqrt(n));//ｎの素因数の最大値
		f = 5;
		while(f <= r){
			if(fmod(n,f) == 0)
				return 0;
			if(fmod(n,f + 2) == 0)
				return 0;
			//fmod(n,f + 4)は3の倍数なので判定しなくてよい
			f += 6;
		}
		return 1;
	}
}