##include <iostream>
#include <set>
using namespace std;

int main() {
    int size = 10000000;
    int *factors = new int[size];
    for (int i = 1; i <= size + 1; i++) {
        for (int idx = 0; idx <= size; idx += i) {
            factors[idx] += 1;
        }
    }

    for (int i; i <= size; i++) {
        cout << factors[i] << ", " << endl;
    }

    set<int> peak_numbers;
    int result = 0;
    int max_factors = 0;

    for (int i = 0; i <= size; i++) {
        if (factors[i] > max_factors) {
            max_factors = factors[i];
            result = i;
            peak_numbers.insert(result);
            cout << result << endl;
        }
    }

    delete[] factors;
    return 0;
}include <set>
using namespace std;

int main() {
    int size = 10000000;
    int *factors = new int[size];
    for (int i = 1; i <= size + 1; i++) {
        for (int idx = 0; idx <= size; idx += i) {
            factors[idx] += 1;
        }
    }

    for (int i; i <= size; i++) {
        cout << factors[i] << ", " << endl;
    }

    set<int> peak_numbers;
    int result = 0;
    int max_factors = 0;

    for (int i = 0; i <= size; i++) {
        if (factors[i] > max_factors) {
            max_factors = factors[i];
            result = i;
            peak_numbers.insert(result);
            cout << result << endl;
        }
    }

    delete[] factors;
    return 0;
}#include <iostream>
#include <set>
using namespace std;

int main() {
    int size = 10000000;
    int *factors = new int[size];
    for (int i = 1; i <= size + 1; i++) {
        for (int idx = 0; idx <= size; idx += i) {
            factors[idx] += 1;
        }
    }

    for (int i; i <= size; i++) {
        cout << factors[i] << ", " << endl;
    }

    set<int> peak_numbers;
    int result = 0;
    int max_factors = 0;

    for (int i = 0; i <= size; i++) {
        if (factors[i] > max_factors) {
            max_factors = factors[i];
            result = i;
            peak_numbers.insert(result);
            cout << result << endl;
        }
    }

    delete[] factors;
    return 0;
}include <set>
using namespace std;

int main() {
    int size = 10000000;
    int *factors = new int[size];
    for (int i = 1; i <= size + 1; i++) {
        for (int idx = 0; idx <= size; idx += i) {
            factors[idx] += 1;
        }
    }

    for (int i; i <= size; i++) {
        cout << factors[i] << ", " << endl;
    }

    set<int> peak_numbers;
    int result = 0;
    int max_factors = 0;

    for (int i = 0; i <= size; i++) {
        if (factors[i] > max_factors) {
            max_factors = factors[i];
            result = i;
            peak_numbers.insert(result);
            cout << result << endl;
        }
    }

    delete[] factors;
    return 0;
}include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> trains = {3, 2, 1};
    int count = 0;

    while (trains.size() > 0) {
        vector<int> array1 = {trains[0]};
        vector<int> tmp;

        for (int i = 1; i < trains.size(); i++) {
            if (array1[array1.size() - 1] <= trains[i]) {
                array1.push_back(trains[i]);
            } else {
                tmp.push_back(trains[i]);
            }
        }
        trains = tmp;
        count++;
    }
    cout << count - 1 << endl;
}
