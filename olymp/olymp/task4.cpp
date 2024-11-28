#include <iostream>
#include <string>
using namespace std;

int main() {
    long long tasks[10] = {8,
                           19,
                           72,
                           445,
                           648772,
                           623690081,
                           54433933447,
                           713016426262703497,
                           585335723211047202};
    long long size = 100000000000;
    long long result = 0;
    for (long long i = 0; i < size; i++) {
        long long num = i + 1;
        while (num % 10 == 0) {
            num /= 10;
        }
        result += num;
        if (i == 54433933447) {
            cout << result % 10000000007;
            break;
        }
    }
    return 0;
}
