#include<iostream>
#include<algorithm>
using namespace std;
int main(){
    int n,m;
    cin>>n>>m;
    int a,ans=1;
    a=m/n;
    if (m%n==0) {
      cout<<m/n<<endl;
      return 0;
    }
    for (size_t i = 1; i < a+1; i++) {
      if (m%i==0) {
        if (ans<i) {
          ans=i;
        }
      }
    }
    cout<<ans<<endl;






}
