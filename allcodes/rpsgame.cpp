#include<iostream>
using namespace std;
class GameManger
{
public: 
	void storewin(int a,int b);
	void calulatevalues(char p1,char p2);
	void DisplayScore();
	void Gamerules();
private:
	int player1, player2;
}
void GameManger::storewin(int a,int b)
{
	if(a>b) player1++;
	else player2++;
}
void GameManger::Gamerules(char p1,char2)
{
  	
  	if     (p1=='r'&&p2=='s') storewin(0,1);
  	else if(p1=='s'&&p2=='r') storewin(1,0);
  	else if(p1=='s'&&p2=='p') storewin(1,0);
  	else if(p1=='p'&&p2=='s') storewin(0,1);
  	else if(p1=='p'&&p2=='r') storewin(1,0);
  	else if(p1=='r'&&p2=='p') storewin(0,1);
}
void GameManger::DisplayScore()
{
	cout<<"Player 1 wins"<<player1<<" : player 2 wins"<<player2<<endl;
}
void GameManger::calulatevalues(char p1,char p2)
{
	Gamerules(p1,p2);
}
int main()
{
	char a,b;
	int end=0;
	cout<<"welcome "<<endl<<"r for rock, p for paper, s for scissor"<<endl<<"player 1:player 2"<<endl;
	while(!end)
	{
	cin>>a>>b;
	GameManger gamevalues;
	gamevalues.calulatevalues(a,b);
	gamevalues.DisplayScore();
	cout<<"Do you want to end press 1 to end or 0 to continue";
	cin>>end;
	}
}