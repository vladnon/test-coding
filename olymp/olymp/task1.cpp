#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> h = {2, 4, 5}, b = {1, 4, 3};
    sort(begin(h), end(h));
    sort(begin(b), end(b));
    long long result = 0;
    for (int i = h.size(); i > 0; i--) {
        result += abs(h[i] - b[i]);
    }
    cout << result << endl;
}
