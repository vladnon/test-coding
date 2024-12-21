#include <iostream>
#include <map>
#include <set>
#include <string>
using namespace std;

class Solution {
  public:
    bool checkIfPangram(string sentence) {
        set<char> chars;
        string letters = "abcdefghijklmnopqstuvwxyz";
        for (const char ch : sentence) {
            chars.insert(ch);
        }
        for (const char letter : letters) {
            if (chars.count(letter) == 0) {
                return false;
            }
        }
        return true;
    }

    bool squareIsWhite(string coordinates) {
        map<char, int> hashmap{{'a', 1}, {'b', 2}, {'c', 3}, {'d', 4},
                               {'e', 5}, {'f', 6}, {'g', 7}, {'h', 8}};

        if (((int)coordinates[1] + hashmap[coordinates[0]]) % 2 == 0) {
            return false;
        }
        return true;
    }
};

void something(int &num) { num = 10; }

void something_2(int *nums[], int n) {
    for (int i = 0; i <= n; i++) {
        cout << nums[i] << ", ";
    }
}

int main() {
    // string coords = "b1";
    // bool answer = true;
    // Solution solution;
    // bool result = solution.squareIsWhite(coords);
    // if (result == answer) {
    //     cout << "Your solution is correct" << endl;
    // } else {
    //     cout << "Your solution is incorrect" << endl;
    // }

    // int nums[] = {1, 2, 3, 4};
    // int n = 4;
    //
    // int num{15};
    // cout << num << endl;
    // something(num);
    // cout << num;

    int num = 0 % 2;
    cout << num << endl;
    return 0;
}
