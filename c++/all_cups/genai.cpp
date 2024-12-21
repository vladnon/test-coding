#include <iostream>
#include <map>
#include <vector>
using namespace std;

int task1(int *nums, int size) {
    int left = 0, right = 0;
    int summ = *nums;
    int cur_sum = 0;
    while (right < size) {
        cur_sum += nums[right];
        summ = max(summ, cur_sum);
        right++;

        if (cur_sum < 0) {
            cur_sum = 0;
            left = right;
        }
    }
    return summ;
}

void task2(map<string, int> hashmap) {
    vector<int> weather;
    int idx = 0;
    vector<string> date;

    for (auto const &[key, val] : hashmap) {
        weather.push_back(val);
        if (weather[idx] < val) {
            date.push_back(key);
        }
        idx++;
    }
    for (int i = 0; i < date.size(); i++) {
        cout << date[i] << endl;
    }
}

int task3(int *nums, int size) {
    int left = 0, right = 1;
    int result = 0;

    while (right < size) {
        if (nums[left] < nums[right]) {
            result = max(result, nums[right] - nums[left]);

        } else {
            left = right;
        };
        right++;
    }
    return result;
}

int main() {
    // int size;
    // cin >> size;
    //
    // int array[size];
    // for (int i = 0; i < size; i++) {
    //     cin >> array[i];
    // }
    // int res = task1(array, size);
    // cout << res << endl;
    //

    // map<string, int> hashmap;
    // int n;
    // cin >> n;
    //
    // for (int i = 0; i < n; i++) {
    //     string date;
    //     int weather;
    //     cin >> date >> weather;
    //     hashmap[date] = weather;
    // }
    //
    // task2(hashmap);

    int size;
    cin >> size;

    int nums[size];
    for (int i = 0; i < size; i++) {
        cin >> nums[i];
    }
    int result3 = task3(nums, size);
    cout << result3 << endl;

    return 0;
}
