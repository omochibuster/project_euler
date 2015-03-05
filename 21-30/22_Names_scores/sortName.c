#include"sortName.h"
void sortName(char name[5163][20], int start, int end, int point)
{
	int i,j,k;
	char c = 'A';
	char temp[20];
	if(point >= 20)
		return; 

	for(i = start; i < end; i ++)
	{
		if(name[i][point] == '\0')
		{
			strcpy(temp,name[i]);
			strcpy(name[i],name[start]);
			strcpy(name[start],temp);
			start++;
		}
	}

	for(i = start; i < end; i ++)
	{
		for(j = i;j < end; j ++)
		{
			if(name[j][point] == c)
			{
				strcpy(temp,name[i]);
				strcpy(name[i],name[j]);
				strcpy(name[j],temp);
				i++;
			}
		}
		sortName(name,start,i,point + 1);
		start = i --;
		c++;
		if(c > 'Z')
			break;
	}
}