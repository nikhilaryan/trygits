#include<iostream>
#include<tuple>
#include<vector>
#include<sort>
using namespace std;

bool sortbythird(tuple<int,int,int>a,tuple<int,int,int>b)
{
	return (a.third<b.third);
}

int main()
{
	vector<tuple<int,int,int>>nvec;
	while(true)
	{
	int a,b,c;
	cin>>a>>b>>c;
	nvec.push_back(make_tuple(a,b,c));
	sort(nvec.begin(), nvec.end(),sortbythird);
    }
}