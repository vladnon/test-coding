// #include <algorithm>
#include <cmath>
#include <iostream>
// #include <vector>
using namespace std;

void findFourSquares(int n) {
    int num = sqrt(n);
    for (int a = 0; a <= sqrt(n); a++) {
        for (int b = 0; b <= sqrt(n); b++) {
            for (int c = 0; c <= sqrt(n); c++) {
                for (int d = 0; d <= sqrt(n); d++) {
                    if (a * a + b * b + c * c + d * d == n) {
                        cout << a << " " << b << " " << c << " " << d << endl;
                        return;
                    }
                }
            }
        }
    }
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

int artem_lebedev(int n, int a, int b, int c) {
    int test = n;
    int count = 0;

    while (test >= a) {
        test -= a;
        count++;
    }

    test = n;
    while (test >= b) {
        test -= b;
        count++;
    }

    test = n;
    while (test >= c) {
        test -= c;
        count++;
    }

    int summ = a + b;
    test = n;
    while (summ <= test) {
        count++;
        summ += a;
    }

    summ = a + b + b;
    test = n;
    while (summ <= test) {
        count++;
        summ += b;
    }

    summ = a + c;
    test = n;
    while (summ <= test) {
        count++;
        summ += a;
    }

    summ = a + c + c;
    test = n;
    while (summ <= test) {
        count++;
        summ += c;
    }

    summ = b + c;
    test = n;
    while (summ <= test) {
        count++;
        summ += b;
    }

    summ = b + c + c;
    test = n;
    while (summ <= test) {
        count++;
        summ += c;
    }

    return count;
}

int main() {
    /*
    int n;
    cin >> n;
    findFourSquares(n);
    */

    long long t;
    cin >> t;
    for (long long i = 0; i < t; i++) {
        long long num;
        cin >> num;
        long long area = num * num + 1;
        int result = monkey(area);
        if (result == -1) {
            cout << -1 << endl;
        } else {

            cout << result << " " << area / result << endl;
        }
    }
    /*
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
     int n, a, b, c;
     cin >> n >> a >> b >> c;
     cout << artem_lebedev(n, a, b, c) << endl;
     */
    return 0;
}
