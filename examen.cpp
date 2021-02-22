#include<iostream>
#include<string>

#define ENTER "\n"
using namespace std;

int main(){
	string palabra;
	cout<<"Escribe una palabra";
	getline (cin,palbra,ENTER);
	
//cout<<palabra;
string alreves;
int tamano=palabra.length();
fot (int i=tamano-1; i>=0; i--){
	// cout<palabra[i]
	alreves=alreves+palabra[i];
}
cout<<alreves<<endl;
if (palabra==alreves){
	cout<<"ES PALINDROMO"<<endl;
} else(
	cout<<"No es palindromo"<<endl;
	)
}
	



