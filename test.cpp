#include <algorithm>
#include <cctype>
#include <cmath>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
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

    string addBinary(string a, string b) {
        string min_lenth_string;
        string max_lenth_string;
        bool need_to_add_one = false;
        string result;
        int idx;
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());

        if (a.size() > b.size()) {
            min_lenth_string = b;
            max_lenth_string = a;
        } else {
            min_lenth_string = a;
            max_lenth_string = b;
        }

        for (int i = 0; i < min_lenth_string.size(); i++) {

            if (a[i] == '1' && b[i] == '1') {
                if (need_to_add_one) {
                    result += '1';
                } else {
                    need_to_add_one = true;
                    result += '0';
                }
            }
            if (a[i] != b[i]) {
                if (need_to_add_one) {
                    result += '0';
                } else {
                    result += '1';
                }
            }
            if (a[i] == '0' && b[i] == '0') {
                cout << "here" << endl;
                if (need_to_add_one) {
                    result += '1';
                    need_to_add_one = false;
                } else {
                    result += '0';
                }
            }
            // cout << result << endl;
            idx = i;
        }
        while (need_to_add_one) {
            if (idx > max_lenth_string.size() - 1) {
                result += '1';
                need_to_add_one = false;
            }
            if (max_lenth_string[idx] == '1') {
                if (idx == max_lenth_string.size() - 1) {
                    result += '1';
                    need_to_add_one = false;
                    break;
                }
                result += '0';
            } else {
                result += '1';
                need_to_add_one = false;
            }
            idx++;
            // cout << result << endl;
        }

        reverse(result.begin(), result.end());
        return result;
    }

    string reverseVowels(string s) {
        int left = 0, right = s.size() - 1;
        bool left_flag = false;
        set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        vector<int> something;

        while (left < right) {
            if (left_flag) {
                if (vowels.count(s[right]) > 0) {
                    swap(s[left], s[right]);
                    left_flag = false;

                    left++;
                    right--;
                } else {
                    right--;
                }
            } else {
                if (vowels.count(s[left]) > 0) {
                    left_flag = true;
                } else {
                    left++;
                }
            }
        }
        return s;
    }
    vector<int> plusOne(vector<int> &digits) {
        bool need_to_add_one;
        if (digits[digits.size() - 1] + 1 < 10) {
            digits[digits.size() - 1]++;
            return digits;
        }
        string result;
        need_to_add_one = true;
        int idx = digits.size() - 1;
        while (need_to_add_one) {
            if (idx < 0) {
                result += '1';
                break;
            }
            if (digits[idx] + 1 < 10) {
                result += to_string(digits[idx] + 1);
                need_to_add_one = false;
                idx--;
            } else {
                string num_to_string = to_string(digits[idx] + 1);
                result += num_to_string[num_to_string.size() - 1];
                idx--;
            }
        }
        while (idx >= 0) {
            result += to_string(digits[idx]);
            idx--;
        }
        vector<int> final_result;
        reverse(result.begin(), result.end());
        for (int i = 0; i < result.size(); i++) {
            final_result.push_back(result[i] - '0');
        }
        return final_result;
    }

    string sortVowels(string s) {
        set<char> vowels = {'a', 'u', 'o', 'i', 'e', 'A', 'U', 'O', 'I', 'E'};
        vector<char> vowels_array;
        int idx = 0;

        for (int i = 0; i < s.size(); i++) {
            if (vowels.count(s[i]) > 0) {
                vowels_array.push_back(s[i]);
            }
        }

        sort(vowels_array.begin(), vowels_array.end());
        for (int i = 0; i < s.size(); i++) {
            if (vowels.count(s[i]) > 0) {
                s[i] = vowels_array[idx];
                idx++;
            }
        }
        return s;
    }

    int expressiveWords(string s, vector<string> &words) {
        int left = 0, right = 0;
        cout << left << ", " << s.size() << endl;
        string new_s;
        while (right < s.size()) {
            cout << s[left] << ", " << s[right] << endl;
            if (s[left] == s[right]) {
                right++;
            } else {
                if (right - left >= 3) {
                    new_s += s[left];
                } else {
                    for (int i = 0; i <= right - left - 1; i++) {
                        new_s += s[left];
                    }
                }
                left = right;
            }
        }
        if (right - left >= 3) {
            new_s += s[left];
        } else {
            for (int i = 0; i <= right - left - 1; i++) {
                new_s += s[left];
            }
        }
        cout << new_s << endl;
        for (int i = 0; i < words.size(); i++) {
            if (words[i] == new_s) {
                return i + 1;
            }
        }
        return -1;
    }

    int something(int a, int b, int c) {
        int minus = 1;
        while (true) {
            minus++;
            if (a + b - 2 * minus <= c - minus) {
                return minus;
            }
            if (a + c - 2 * minus <= b - minus) {
                return minus;
            }
            if (b + c - 2 * minus <= a - minus) {
                return minus;
            }
        }
        return minus;
    }
    int divide(int dividend, int divisor) {
        double division_result = (double)dividend / divisor;
        int result = 0;
        string string_result = to_string(division_result);
        int left = 0;
        int something = 0;

        if (dividend <= -2147483648 && divisor == -1) {
            dividend++;
            return dividend * divisor;
        }

        while (dividend < -2147483648) {
            dividend++;
        }

        while (dividend > 2147483647) {
            dividend--;
        }

        if (divisor == -1 | divisor == 1) {
            return dividend * divisor;
        }

        cout << string_result << endl;

        left--;
        while (left >= 0) {
            if (string_result[left] == '-') {
                return result * -1;
            }
            int num = string_result[left] - '0';
            for (int i = 0; i < something; i++) {
                num *= 10;
            }
            result += num;
            left--;
        }

        return result;
    }
    int findMaxLength(vector<int> &nums) {
        int count1 = 0, count0 = 0, left = 0, right = 0;
        return 0;
    }

    string flowers(long long w, long long r, long long k) {
        int summ = w + r;
        while (summ >= k) {
            if (r % 2 == 0) {
                summ--;
                if (r <= 0) {
                    w--;
                } else {
                    r--;
                }
            } else {
                return "YES";
            }
        }

        return "NO";
    }

    long long chessboard_and_kings(long long n) {
        long long result = (n + 1) / 2;
        return result * result;
    }

    long long natural_row(long long num) {
        long long size = 10000000;
        long long *nums = new long long[size];
        long long count{};

        for (long long i = 0; i < size; i += 2) {
            nums[i]++;
        }

        for (long long i = 0; i < size; i += 3) {
            nums[i]++;
        }

        for (long long i = 0; i < size; i++) {
            if (nums[i] == 0) {
                count++;
                if (count == num) {
                    delete[] nums;
                    return i;
                }
            }
        }
        return 0;
    }

    int linear_game(int n) {
        if (n == 1 | n == 2) {
            return 0;
        }
        if (n % 2 == 0) {
            return (n / 2) + 1;
        } else {
            return (n + 1) / 2;
        }
    }

    long long rect_and_square(long long m, long long n) {
        long long count{};
        while (m * n >= 1) {
            count++;
            long long side_of_square = min(m, n);
            if (side_of_square == m) {
                n -= side_of_square;
            } else {
                m -= side_of_square;
            }
        }
        return count;
    }
};

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
    // int num = 0 % 2;
    // cout << num << endl;
    Solution solution;
    // string result = solution.addBinary("101101", "10");
    // cout << result << endl;
    // string result1 = solution.reverseVowels("IceCreAm");
    // cout << result1 << endl;
    // vector<int> nums = {1, 2, 9};
    // vector<int> result2 = solution.plusOne(nums);

    // for (int i = 0; i < result2.size(); i++) {
    //     cout << result2[i] << ", ";
    // }
    //
    // string s = "lEetcOde";
    // string result3 = solution.sortVowels(s);
    // cout << result3 << endl;
    //
    // string str = "heeellooo";
    // vector<string> words = {"hello", "hi", "helo"};
    // int result4 = solution.expressiveWords(str, words);
    // cout << result4 << endl;

    // int a, b, c;
    // cin >> a;
    // cin >> b;
    // cin >> c;

    // int result5 = solution.something(a, b, c);
    // cout << result5 << endl;

    // int result6 = solution.divide(-2147483647, -1);
    // cout << result6 << endl;

    // int n;
    // cin >> n;
    // while (n > 0) {
    // long long w, r, k;
    // cin >> w >> r >> k;
    // string result7 = solution.flowers(w, r, k);
    // cout << result7 << endl;
    // n -= 1;
    // }

    // long long n;
    // cin >> n;
    // long long result8 = solution.chessboard_and_kings(n);
    // cout << result8;
    //
    // long long n;
    // cin >> n;
    // long long result9 = solution.natural_row(n);
    // cout << result9 << endl;

    // int n;
    // cin >> n;
    // for (int i = 0; i < n; i++) {
    // int num;
    // cin >> num;
    // }
    // int result9 = solution.linear_game(n);
    // cout << result9 << endl;
    //
    //
    long long m, n;
    cin >> m >> n;
    long long result10 = solution.rect_and_square(m, n);
    cout << result10 << endl;
    return 0;
}
