#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k, q;
    cin >> n >> k;
    k--;
    int arr[n];

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cin >> q;
    vector<pair<int, int>> lrs;
    for (int i = 0; i < q; i++) {
        int l, r;
        cin >> l >> r;
        pair<int, int> new_pair = {l, r};
        lrs.push_back(new_pair);
    }

    for (int i = lrs.size() - 1; i >= 0; i--) {
        int l = lrs[i].first;
        int r = lrs[i].second;
        l--;
        r--;
        if (k >= l && k <= r) {
            k = l + r - k;
        }
    }

    cout << arr[k] << endl;
    return 0;
}
