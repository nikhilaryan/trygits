#include<iostream>
#include<vector>
using namespace std;
void bfs(vector<int>v,int l,int r,int curr, int &index)
{
	if(l<r)
	{
		int mid=(l+r)/2;
		if(v[mid]==curr)
		{
			index=mid;
			return;
		}
		else if(v[mid]<curr) return bfs(v,mid+1,r,curr,index);
		else bfs(v,l,mid-1,curr,index);
	}
}
int main()
{
	vector<int>nvec={1,2,3,4,5,6};
	int index=-1;
    bfs(nvec,0,nvec.size(),4,index);
	if(index!=-1) cout<<index+1<<endl;
	else cout<<"Element not found"<<endl; 
}