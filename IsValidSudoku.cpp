#include <bits/stdc++.h>
using namespace std;

int sudoku[9][9];

/*
3 0 6 5 0 8 4 0 0 
5 2 0 0 0 0 0 0 0 
0 8 7 0 0 0 0 3 1 
0 0 3 0 1 0 0 8 0 
9 0 0 8 6 3 0 0 5 
0 5 0 0 9 0 6 0 0 
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4 
0 0 5 2 0 6 3 0 0
*/
bool finalCheck(){
	int i,j;
	for(i=0;i<9;i++){
		map<int,int>f;
		for(j=0;j<9;j++){if(sudoku[i][j]==0)continue;
			f[sudoku[i][j]]++;
			if(f[sudoku[i][j]]>1)return false;
			}//f.clear();
		}
	for(i=0;i<9;i++){
		map<int,int>f;
		for(j=0;j<9;j++){if(sudoku[j][i]==0)continue;
			f[sudoku[j][i]]++;
			if(f[sudoku[j][i]]>1)return false;
			}//f.clear();
		}
	return true;
	}

int main(){
	int t;
	cin>>t;
	while(t--){
		int i,j;
		for(i=0; i<9; i++){
			for(j=0; j<9; j++)cin>>sudoku[i][j];
			}
		if(finalCheck())cout<<1<<endl;
		else cout<<0<<endl;
		}
	return 0;
	}
