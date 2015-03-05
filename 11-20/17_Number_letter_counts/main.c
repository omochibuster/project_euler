/*
	the answer is 21124
*/
//2014.11.18
#include<stdio.h>

int oneDigit(int);
int twoDigit(int);
int threeDigit(int);

int main(void){
	int count = 0, i, j, k;

	for(i = 0; i < 10; i ++){//i = 100の位
		if(i != 0){//100の位がある
			//百の位の文字数 + hundred + and * (00 ～ 99まで100個分)
			count += (oneDigit(i) + 7 + 3) * 100;
			count -= 3;//100や200などの詩も二桁が00はandがないので引く
		}
		for(j = 0; j < 10; j ++)
			count += oneDigit(j);//1～9
		for(j = 0; j < 10; j ++){
			count += twoDigit(j);//10～19
		}
		for(j = 2; j < 10; j ++){//20以降
			count += threeDigit(j) * 10;//～tyが0～9まであるので*10
			for(k = 0; k < 10; k ++)
				count += oneDigit(k);
		}
	}
	count += 11;//one Thousandを足す
	printf("%d\n",count);
	getchar();
	return 0;
}

int oneDigit(int num){
	switch(num){
		case 1://one
		case 2://two
		case 6://six
			return 3;//3文字
		case 4://four
		case 5://five
		case 9://nine
			return 4;//4文字
		case 3://three
		case 7://seven
		case 8://eight
			return 5;//5文字
	}
	return 0;
}

int twoDigit(int num){
	switch(num){
		case 0://ten
			return 3;//3文字
		case 1://eleven
		case 2://twelve
			return 6;
		case 5://fifteen
		case 6://sixteen
			return 7;
		case 3://thirteen
		case 4://fourteen
		case 8://eighteen
		case 9://nineteen
			return 8;
		case 7://seventeen
			return 9;//9文字
	}
	return 0;
}

int threeDigit(int num){
	switch(num){
		case 4://forty
		case 5://fifty
		case 6://sixty
			return 5;//5文字
		case 2://twenty
		case 3://thirty
		case 8://eighty
		case 9://ninety
			return 6;//6文字
		case 7://seventy
			return 7;//7文字
	}
	return 0;
}
