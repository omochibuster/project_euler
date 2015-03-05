/*
the answer is 23514624000
*/
//2014.09.11//
//2014.11.08//

#include<stdio.h>
double multiple_array(char cnum[14]);
double isMax(double max, double mult);
int get_12number_from_file(FILE *,char []);
int main(){
	char a;
	char cnum[14];
	int i,count=0;
	double mult, max = 1;
	FILE *fp;

	if((fp = fopen("problem.txt","r")) == NULL)
		return 0;

	while(count != 12)
		cnum[count++] = fgetc(fp);

	while((a = fgetc(fp)) != EOF){
		if(a == '\n')
			continue;
		if(a == '0'){//0�|���͖��Ӗ��Ȃ̂�12���V���Ɉ�C�ɂƂ�
			if(get_12number_from_file(fp,cnum) == 0)//EOF�ɂȂ����甲���o��
				break;
			count = 12;
			continue;
		}
		cnum[count++ % 13] = a;
		max = isMax(max,multiple_array(cnum));
	}
	fclose(fp);
	printf("%.0lf\n",max);
	getchar();
	return 0;
}

int get_12number_from_file(FILE *fp,char cnum[14]){
	int i;
	char a;

	for(i = 0; i < 12; i ++){
		if((a = fgetc(fp)) == EOF){
			return 0;
		}
		if(a == '\n')
			a = fgetc(fp);
		if(a == '0')
			i = -1;
		cnum[i] = a;
	}
	return 1;
}
double isMax(double max, double mult){
	if(max < mult)
		return mult;
	return max;
}

double multiple_array(char cnum[14]){
	int i;
	double mult = 1;
	for(i = 0; i <= 12; i ++){
		mult *= (cnum[i] - '0');
	}
	return mult;
}