#include <iostream>
#include <vector>
using namespace std;

vector<int> findDividers(int num) {
    vector<int> result;
    int d = 1;
    while (d * d <= num) {
        if (num % d == 0) {
            result.push_back(num);
            result.push_back(d);
        }
    }
    return result;
}

int main() {
    int l, r;
    cin >> l;
    cin >> r;
}
