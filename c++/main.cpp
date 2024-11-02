#include <iostream>
#include <string>
using namespace std;

int fibbinochiNumber(int num) {
  if (num == 0) {
    return 0;
  }
  if (num == 1) {
    return 1;
  }
  if (num == 2) {
    return 1;
  }
  return fibbinochiNumber(num - 1) + fibbinochiNumber(num - 2);
}
int main() {
  string hello = "Hello world, ";
  string name;
  cin >> name;
  cout << hello << name << "!" << "\n";
  for (char ch : name) {
    cout << ch << "\n";
  }
  int num;
  cin >> num;
  cout << fibbinochiNumber(num) << endl;
}
