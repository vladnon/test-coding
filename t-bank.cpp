#include <cmath>
#include <iostream>
using namespace std;

void findFourSquares(int n) {
    int num = sqrt(n);
    string res = "";

    while (res.length() != 4) {
        if (num * num <= n) {
            res += to_string(num);
            n -= num * num;
        } else {
            num--;
        }
    }

    for (char ch : res) {
        cout << ch << " ";
    }
    cout << endl;
}

int monkey(long long area) {
    long long k = 1;
    while (k * k <= area) {
        if (area % k == 0) {
            if (k >= 2) {
                return k;
            }
            area /= k;
        }
        k++;
    }

    return -1;
}

int main() {
    int n;
    // cin >> n;
    // findFourSquares(n);
    // long long t;
    // cin >> t;
    // for (long long i = 0; i < t; i++) {
    //     long long num;
    //     cin >> num;
    //     long long area = num * num + 1;
    //     int result = monkey(area);
    long long count = 0;
    for (long long i = 0; i < 1000000; i++) {
        int result = monkey(i);
        count++;
        if (result == -1) {
            cout << -1 << endl;
        } else {
            cout << result << " " << i / result << endl;
        }
    }
    cout << count << endl;
    return 0;
}
