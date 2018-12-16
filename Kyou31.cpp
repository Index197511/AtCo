#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main(){
 int n,x,cnt=0;
 cin>>n>>x;
 vector<string> a;
 string s;
 a[0]="P";
 for (int i = 1; i < n+1; i++) {
   a[i]="B"+a[i-1]+"P"+a[i-1]+"B";
   cout<<a[i]<<endl;
 }
 cout<<a[n];
//for (int i = 0; i < x; i++) {
  //if (a[n][i]=="P") {
    //cnt++;
  //}
//}
//cout<<cnt<<endl;
return 0;


}
