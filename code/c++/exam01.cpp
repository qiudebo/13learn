#include<iostream>
using namespace std;

# 例6.2

void swap(int *p1,int *p2){
	int temp;
	temp = *p1;
	*p1 = *p2;
	*p2 = temp;
}

int main(){
	void swap(int *p1,int *p2);
	int *p1,*p2,a,b;
	a = 10,b=100;
	p1 = &a,p2 = &b;
	if (a < b) swap(p1,p2);
	std::cout <<"a="<<a<<"b="<<b<<endl;
	#std::cout <<"max="<<*p1<<"min="<<*p2<<endl;
	return 0;
}


