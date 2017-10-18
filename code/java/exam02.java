#include<iostream>
using namespace std;

void swap(int *p1,int *p2){
	int temp;
	temp = *p1;
	*p1 = *p2;
	*p2 = temp;
}

void exchange(int *q1,int *q2,int *q3){
	void swap(int *,int *);
	if(*q1<*q2) swap(q1,q2);
	if (*q1<*q3) swap(q1,q3);
	if (*q2<*q3) swap(q2,q3);
}

int main(){
	void exchange(*,*,*);
	int a,b,c,*p1,*p2;
	a=7;b=8;c=9;
	p1 = &a; p2=&b;p3=&c;
	exchange(p1,p3,p3);
	std:cout<<"a="<<a<<" b="<<b<<" c="<<c<<endl;
}