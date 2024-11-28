#include <iostream>
using namespace std;

int main() {
    int a, b, c, x, y, z;
    int n = 6;
    cin >> a >> b >> c >> x >> y >> z;
    a *= 3600 * 24;
    b *= 60 * 24;
    c *= 24;
    int result = (a + b + c) / x / y / z;
    cout << result << endl;
    return 0;
}
