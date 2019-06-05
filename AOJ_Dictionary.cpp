#include<iostream>
#include<string>
#include<vector>
#include<cstring>
using namespace std;
int main(){
    int n;
    string a;
    string b;
    string st[n];
    string st2[n];
    for (int i = 0; i < n; i++) {
        st[i] == "-1";
        st2[i] == "01";
    }
    bool flag = false;
    bool flag2 = false;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        if (a == "insert") {
            st[i] = b;
        }
        else{
            st2[i] = b;
        }
      }

      for (int i = 0; i < n; i++) {
          flag = false;
          flag2 = false;
          for (int j = 0; j < n; j++) {
              if (st2[i] == st[j] && st2[i] != "01") {
                  flag = true;
                  flag2 = true;
              }
          }
          if (flag2 == true) {
              if (flag == true) cout << "yes" << endl;
              else cout << "no" << endl;
          }
      }

    return 0;

}
