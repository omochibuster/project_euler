/*
the answer is 906609
*/

//2014.09.09//
//2014.11.06 pdfŒ`®‚É•ÏX//

#include<stdio.h>

int reverse(int);
int isPalindrome(int);

int main(void){
	int largestPalindrome = 0,
		 a = 999,
		 b,db;

	while(a >= 100)
	{
		if(a % 11 == 0)
		{
			b = 999;
			db = 1;
		}
		else
		{
//the largest number less than or equal 999 and divisible by 11
			b = 990;
			db = 11;
		}
		while(b >= a)
		{
			if(a * b <= largestPalindrome)
				break;
			if(isPalindrome(a * b))
				largestPalindrome = a * b;
			b = b - db;
		}
		a--;
	}
	printf("%d\n",largestPalindrome);
	getchar();
	return 0;
}

int reverse(int n)
{
	int reversed = 0;
	while(n > 0)
	{
		reversed = (10 * reversed) + (n % 10);
		n = n / 10;
	}
	return reversed;
}

int isPalindrome(int n)
{
	return n == reverse(n);
}