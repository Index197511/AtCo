#include<iostream>
#include<algorithm>
using namespace std;
int main(){
    int n = 0,m = 0,cnt = 0, b = 0, c = 0;
    long long ans = 0;
    cin >> n >> m;
    int a[n] = {0};

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a, a+n);

    for (int i = 0; i < m; i++) {
        cnt = 0;
        cin >> b >> c;
        for (int j = 0; j < n; j++) {
            if (a[j] < c) {
                a[j] = c;
                cnt++;
                if (cnt >= b){
                    break;
                }
            }else{
                break;
            }

        }

        sort(a, a+n);
    }

    for (int i = 0; i < n; i++) {
        ans += a[i];
    }
    cout << ans << endl;



}
