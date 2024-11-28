#include <array>
#include <iostream>
#include <string>
using namespace std;

int main() {
  int a = 234;
  int *pa = &a;
  int *pa1 = pa;
  cout << pa1 << " " << pa << " " << &a << endl;
  return 0;
}
