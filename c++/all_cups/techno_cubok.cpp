#include <iostream>
using namespace std;

long long task1(long long *nums, long long size) {
    int array_sum = 0;
    int even_number = -1;

    for (long long i = 0; i < size; i++) {
        array_sum += nums[i];
        if (nums[i] % 2 == 0) {
            even_number = i;
        }
    }
    if (array_sum % 3 != 0 || even_number == -1) {
        return -1;
    }
    return (size - even_number - 1);
}

int main() {
    long long size;
    cin >> size;
    long long num;
    cin >> num;
    int nums[size];

    for (long long i = size - 1; i >= 0; i--) {
        nums[i] = num % 10;
        num /= 10;
    }

    long long result1 = task1(nums, size);
    cout << result1 << endl;

    return 0;
}
