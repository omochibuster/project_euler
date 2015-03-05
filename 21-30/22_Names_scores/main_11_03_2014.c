/*
Problem 22 「名前のスコア」 †

the answer = 871198282
*/

#include "sortName.h"

void calcScore(char name[5163][20]);
int main(void)
{

	FILE *fp;
	FILE *sfp;
	char c;
	char name[5163][20];
	int i,j,count;

	if((fp = fopen("22.txt","r")) == NULL)
		return 0;

	if((sfp = fopen("sort22.txt","w")) == NULL)
		return 0;

	for(i = 0;(c = fgetc(fp)) != EOF; i ++)
	{
		if(i != 0)
			c = fgetc(fp);//\,をとる
		for(j = count = 0;; j ++)
		{
			if(c == '\"')
				if(count == 0)
				{
					count ++;
					c = fgetc(fp);
				}else
					break;
			name[i][j] = c;
			c = fgetc(fp);
		}
		name[i][j] = '\0';
	}
	sortName(name,0,i,0);
	for(i = 0; i < 5163; i ++)
	{
		printf("%s\n",name[i]);
		fprintf(sfp,"%s\n",name[i]);
	}
	calcScore(name);
	fclose(fp);
	fclose(sfp);

	return 0;
}

void calcScore(char name[5162][20])
{
	int i,j;
	int perScore;
	double totalScore = 0;
	for(i = 0; i < 5163; i ++)
	{
		perScore = 0;
		for(j = 0;name[i][j] != '\0'; j ++)
		{
			perScore += (name[i][j] - 'A') + 1;
		}
		totalScore = totalScore + (perScore * (i + 1));
	}
	printf("score =      %.0f\n",totalScore);
}