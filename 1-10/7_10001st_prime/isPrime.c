#include<math.h>
int isPrime(int n){
	int r,f;
//�f���̏ꍇ��1��Ԃ�//
	if(n == 1)
		return 0;//�f���łȂ�
	else if(n < 4)
		return 1;// 2��3�͑f��
	else if(fmod(n,2) == 0)
		return 0;
	else if(n < 9)
		return 1;//9��菬�������R���̋����͏�ŏ����Ă���̂Ŏc��͑f���ƂȂ�
	else if(fmod(n,3) == 0)
		return 0;
	else{
		r = floor(sqrt(n));//���̑f�����̍ő�l
		f = 5;
		while(f <= r){
			if(fmod(n,f) == 0)
				return 0;
			if(fmod(n,f + 2) == 0)
				return 0;
			//fmod(n,f + 4)��3�̔{���Ȃ̂Ŕ��肵�Ȃ��Ă悢
			f += 6;
		}
		return 1;
	}
}