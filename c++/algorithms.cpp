#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Algorithms {

  public:
    vector<int> bubleSort(vector<int> arr) {
        bool swapped = true;

        while (swapped) {
            swapped = false;
            for (int i = 0; i < arr.size() - 1; i++) {
                if (arr[i] > arr[i + 1]) {
                    int current_element = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = current_element;
                    swapped = true;
                }
            }
        }
        return arr;
    }

    vector<int> mergeTwoSortedArrays(vector<int> arr1, vector<int> arr2) {
        int p1 = 0, p2 = 0;
        vector<int> result;

        while (p1 < arr1.size() && p2 < arr2.size()) {
            if (arr1[p1] < arr2[p2]) {
                result.push_back(arr1[p1]);
                p1++;
            } else if (arr1[p1] > arr2[p2]) {
                result.push_back(arr2[p2]);
                p2++;
            } else {
                result.push_back(arr1[p1]);
                p2++;
                p1++;
            }
        }

        while (p1 < arr1.size()) {
            result.push_back(arr1[p1]);
            p1++;
        }
        while (p2 < arr2.size()) {
            result.push_back(arr2[p2]);
            p2++;
        }

        return result;
    }

    vector<int> mergeSort(vector<int> arr) {
        if (arr.size() == 1) {
            return arr;
        }
        vector<int> left =
            vector<int>(arr.begin(), arr.begin() + arr.size() / 2);
        vector<int> right =
            vector<int>(arr.begin() + arr.size() / 2, arr.end());
        return mergeTwoSortedArrays(mergeSort(left), mergeSort(right));
    }

    bool binarySearch(vector<int> arr, int target) {
        arr = mergeSort(arr);
        int left, right;
        left = 0;
        right = arr.size() - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] == target) {
                return true;
            }
            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;
    }

    int new_task(vector<int> nums) {
        int left = 0, right = 0;
        int summ = 0;
        int cur_sum = 0;
        while (right < nums.size()) {
            cur_sum += nums[right];
            summ = max(summ, cur_sum);
            right++;

            if (cur_sum < summ) {
                cur_sum = 0;
                left = right;
            }
        }
        return summ;
    }
};

int new_task(vector<int> nums) {
    int left = 0, right = 0;
    int summ = 0;
    int cur_sum = 0;
    while (right < nums.size()) {
        cur_sum += nums[right];
        summ = max(summ, cur_sum);
        right++;

        if (cur_sum < summ) {
            cur_sum = 0;
            left = right;
        }
    }
    return summ;
}

string printVector(vector<int> arr) {
    string result = "{";
    for (const int elem : arr) {
        result += to_string(elem) += ", ";
    }
    if (!arr.empty()) {
        result.pop_back();
        result.pop_back();
    }
    result += "}";
    return result;
}

int main() {
    Algorithms algorithms = Algorithms();

    vector<int> array = {-5, 1, -1, 2, -10, 20, 11, -8, 5};
    int result = algorithms.new_task(array);
    cout << result << endl;

    // vector<int> array(10000);
    // for (int i = 0; i < array.size(); i++) {
    //     int random_number = rand();
    //     array[i] = random_number;
    // }
    // // string result = printVector(array);
    // cout << "This is unsorted array: " << result << "\n" << endl;

    // vector<int> sorted_array2 = algorithms.mergeSort(array);
    // result = printVector(sorted_array2);
    // cout << "This is sorted array by mergeSort: " << result << "\n\n\n\n\n"
    // << endl;

    // vector<int> sorted_array1 = algorithms.bubleSort(array);
    // result = printVector(sorted_array1);
    // cout << "This is sorted array by bubleSort: " << result << "\n" << endl;

    // int target = -100;
    // cout << boolalpha;
    // cout << algorithms.binarySearch(array, target) << endl;
    //
    // vector<int> array1 = {100, -2, 5, 20, -56};
    // array1 = algorithms.mergeSort(array1);
    // vector<int> array2 = {123, -29, -23, 56, 40};
    // array2 = algorithms.bubleSort(array2);
    // vector<int> array12 = algorithms.mergeTwoSortedArrays(array1, array2);
    // cout << "\nThis is array1: " << printVector(array1)
    //      << "\nThis is array2: " << printVector(array2)
    //      << "\nThis is array creating by merging this two sorted arrays: "
    //      << printVector(array12) << endl;
    //
    return 0;
}
