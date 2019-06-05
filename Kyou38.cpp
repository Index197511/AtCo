#include<iostream>
#include<math.h>
#include<cmath>
#include<iomanip>
using namespace std;
int main(){
    int n, k, cnt = 0, tmp = 1, end = n;
    cin >> n >> k;
    double ans = 0.0, tmp3, tmp4;
    while(1){
        tmp *= 2;
        cnt++;
        if (tmp >= k) break;
    }
    //cout << cnt << endl;
    for (int i = 0; i < n; i++) {
        tmp3 = pow((1.0 / 2.0), (double) cnt);
        //cout << "tmp3 " << tmp3 << endl;
        tmp4 = ((double) 1) / ((double) n);
        if (isinf(tmp3) || isinf(tmp4)){
            continue;
        }else{
        ans += tmp4 * tmp3;
        //cout << ans << endl;
        cnt -= 1;
    }
    }
    cout << setprecision(15) << ans << endl;
    return 0;
}
