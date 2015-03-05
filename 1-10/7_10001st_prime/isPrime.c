#include<math.h>
int isPrime(int n){
	int r,f;
//‘f”‚Ìê‡‚Í1‚ğ•Ô‚·//
	if(n == 1)
		return 0;//‘f”‚Å‚È‚¢
	else if(n < 4)
		return 1;// 2‚Æ3‚Í‘f”
	else if(fmod(n,2) == 0)
		return 0;
	else if(n < 9)
		return 1;//9‚æ‚è¬‚³‚¢©‘R”‚Ì‹ô”‚Íã‚ÅÁ‚µ‚Ä‚¢‚é‚Ì‚Åc‚è‚Í‘f”‚Æ‚È‚é
	else if(fmod(n,3) == 0)
		return 0;
	else{
		r = floor(sqrt(n));//‚‚Ì‘fˆö”‚ÌÅ‘å’l
		f = 5;
		while(f <= r){
			if(fmod(n,f) == 0)
				return 0;
			if(fmod(n,f + 2) == 0)
				return 0;
			//fmod(n,f + 4)‚Í3‚Ì”{”‚È‚Ì‚Å”»’è‚µ‚È‚­‚Ä‚æ‚¢
			f += 6;
		}
		return 1;
	}
}