#include <iostream>
using namespace std;
#include <string>

string checkIfTrIsReal(int a, int b, int c) {
    if ((a + b) <= c) {
        return "NO";
    }
    if ((a + c) <= b) {
        return "NO";
    }
    if ((b + c) <= a) {
        return "NO";
    }
    return "YES";
}

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << checkIfTrIsReal(a, b, c);
    return 0;
}
