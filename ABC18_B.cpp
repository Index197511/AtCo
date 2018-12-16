#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main(){
string S;
int N;
cin>>S>>N;
int l,r;
for (int i = 0; i < N; i++) {
  cin>>l>>r;
  reverse(&S[l-1],&S[r]);
}
cout<<S<<endl;







}
