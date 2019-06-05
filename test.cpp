#include <iostream>
#include <vector>
using namespace std;
int main(){
    int x;
    vector <int> a;
    for (int i = 0; i < 10; i++) {
        cin >> x;
        a.push_back(x);
    }
    for (int i = 0; i < 10; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}
// 入力 1 2 3 4 5 6 7 8 9 10
// 出力 2 4 6 8 10 12 14 16 18 20
