#include <iostream>
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
