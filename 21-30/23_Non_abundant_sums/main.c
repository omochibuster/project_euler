/*
the answer is 4179871
*/
//2014.11.11//
/*
	is_abundant�֐�����������������Ɖ��P�ł��邩��
	2�̉ߏ萔�̘a�ŕ\���Ȃ����R�������߂邱�Ƃɒ���
	2�̉ߏ萔�̘a�ŕ\���Ȃ��ߏ萔�����a�Ɋ܂܂��
*/
#include<stdio.h>
#include<math.h>
#include<time.h>
#define LIMIT 28123
#define ARRAY_NUM 10000

int is_abundant(int,int[]);
int divitSum(int);
int main(void){
	int i,j,abundant[ARRAY_NUM],abundantSum = 0;
	int start,end;

	start = clock();//���s���Ԃ̌v��

	for(i = 0; i < ARRAY_NUM; i ++)
		abundant[i] = 0;

	for(i = 1; i <= LIMIT; i ++){
		abundantSum += is_abundant(i,abundant);
	}
	end = clock();//���s���ԑ���I��
	printf("%d\n",abundantSum);
	printf("���s���Ԃ� %d �~���b�ł���\n",end - start);
	getchar();
	return 0;
}

int is_abundant(int number,int abundant[ARRAY_NUM]){
	int i,j;

	for(i = 0; abundant[i] != 0; i ++){
		for(j = i; abundant[j] != 0; j ++){
			if(abundant[i] + abundant[j] == number){
				if(divitSum(number) > number){
					while(abundant[++i] != 0);//�󂫔z��܂Ő��`�T��
						abundant[i] = number;
				}
				return 0;
			}
		}
	}
	if(divitSum(number) > number){
		for(; abundant[i] != 0; i ++);//�󂫔z��܂Ő��`�T��
			abundant[i] = number;
	}
	return number;
}

int divitSum(int number){
	int i,sum = 1;

	for(i = 2; i < number; i ++)
		if(number % i == 0)
			sum += i;
	return sum;
}