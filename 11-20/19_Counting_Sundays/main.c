/*
	the answer is 171
*/
//2014.11.19//
#include<stdio.h>

#define SYEAR 1901
#define EYEAR 2000

int getYear(int);
int monthToDays(int);

int main(void){
	int year = 1900;
	int week = 1;
	int i, count = 0, syear;

	syear = SYEAR;
	while(year < SYEAR){
		week += getYear(year);
		week = week % 7;
		year ++;
	}

	while(syear <= EYEAR){
		for(i = 1; i <= 12; i ++){
			if(week == 0)
				count ++;
			week += monthToDays(i);
			if(year % 4 == 0 && i == 2)
				week ++;
			week %= 7;
		}
		syear ++;
	}
	printf("%d\n",count);
	getchar();
	return 0;
}

int getYear(int year){
	if(year % 100 == 0)
		if(year % 400 != 0)
			return 365;
	if(year % 4 == 0)
		return 366;
	return 365;
}

int monthToDays(int month){
	switch(month){
		case 4:
		case 6:
		case 9:
		case 11:
			return 30;
		case 2:
			return 28;//うるう年の場合は呼び出しもとで調整する
		default:
			return 31;
	}
}