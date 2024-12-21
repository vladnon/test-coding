#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

long long taskA() {
    long long a, b, c, x, y, z;
    cin >> a >> b >> c >> x >> y >> z;
    a *= 3600 * 24;
    b *= 60 * 24;
    c *= 24;
    long long min1 = min(a / x, b / y);
    long long min2 = min(min1, c / z);
    return min2;
}

long long taskE(int size, int *nums) {
    int values[size + 1];
    values[0] = -1000000099;
    for (int i = 1; i <= size; i++) {
        values[i] = 1000000001;
    }
    for (int i = 0; i <= size; i++) {
        int *new_num = lower_bound(values, values + size, nums[i]);
        new_num--;
        int len_num = new_num - values + 1;
        if (values[len_num] < nums[i]) {
            values[len_num] = nums[i];
        }
    }

    return 0;
}

int main() {
    int size;
    cin >> size;
    int *nums = new int[size - 1];
    for (int i = 0; i < size; i++) {
        int num;
        cin >> num;
        nums[i] = num;
    }

    cout << taskA() << endl;
    cout << taskE(size, nums) << endl;
    return 0;
}
