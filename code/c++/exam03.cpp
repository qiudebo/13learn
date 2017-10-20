
# 结构体类型  数据项
# 结构体类型 -- 模型

#include<iostream>
using namespace std;

struct Date
{int month;
	int day;
	int year;
};

struct Student
{int num;
	char name[20];
	char sex;
	int age;
	Date birthday;
	float score;
	char address[30];	
}student1,student2 = {10001,'Tom','M',18,5,32,1990,92.5,'BeiJing'};

int main(){
    student1 = student2;
    student1.num = 10002;
    return 0;
}






