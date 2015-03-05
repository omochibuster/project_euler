/*
the answer is 45228
*/

//2014.12.13
#include<stdio.h>
#include<math.h>

int sort(int *, int);
int CheckPandigitalNumber(int);

int main(void){
	int num[9] = {1,2,3,4,5,6,7,8,9};//0は使用しないで1~10を使用する.
	int sum,i,number,j;
	int answer[100] = {0};

	j = 0;
	do{
		number = 0;
		for(i = 0; i < 9; i ++){
			number *= 10;
			number += num[i];
		}
		sum = CheckPandigitalNumber(number);
		for(i = 0; i <= j; i ++){
			if(sum == answer[i]){
				break;
			}
			if(i == j){
				answer[j] = sum;
				j ++;
				break;
			}
		}
	}while(sort(num,9));

	sum = 0;
	for(i = 0; i < j; i ++){
		sum += answer[i];
	}

	printf("%d\n",sum);
	
	return 0;
}

int sort(int *p, int n){
  int i, j, k, tmp;

  /* 上位桁のほうが下位桁よりも小さいところまで移動 */
  for(i = n - 1; i > 0 && p[i-1] >= p[i]; i--);

  /* pが最大(次の並べ替えがない) */
  if(i == 0) return 0;

  /* p[i-1]より値の大きい最も下位の桁をp[j]とする */
  for(j = n - 1; j > i && p[i-1] >= p[j]; j--);

  /* p[i-1]とp[j]とを交換 */
  tmp = p[i-1], p[i-1] = p[j], p[j] = tmp;

  /* p[i]から最下位までを逆順 */
  for(k = 0; k <= ((n-1)-i)/2; k++)
    tmp = p[i+k], p[i+k] = p[(n-1)-k], p[(n-1)-k] = tmp;

  return 1;
}

//pow(10,9 - j) をいじると変になる
int CheckPandigitalNumber(int number){
	int i,j,multipled,multiplying;

	for(i = 1; i < 8; i ++){
		multipled = number / pow(10, 9 - i);
		multiplying = fmod(number,pow(10,8 - i + 1));
		for(j = i + 1; j < 9; j ++){
			if(multipled * (int)(multiplying / pow(10,9 - j)) == (int)fmod(multiplying, pow(10,9 - j))){
				return (int)fmod(multiplying, pow(10,9 - j));
			}
		}
	}
	return 0;
}