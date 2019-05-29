#include<iostream>
#include<vector>
using namespace std;

void Print(vector<int>a)
{
	for(int i=0;i<a.size();i++)
		cout<<a[i]<<" ";
}
int main()
{
	vector<int>a={1,4,9,16,25,36,49,64,81,100};
	vector<int>na;
	for(int i=0;i<a.size();i++)
	{
		if(a[i]/2==0) na.push_back(a[i]);
	}
	Print(na);
}