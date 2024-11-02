#include <iostream>
using namespace std;

class Rectangle {
  int width, height;

public:
  Rectangle(int a, int b) {
    width = a;
    height = b;
  }
  int area() { return (width * height); }
};

int main() {
  int a, b;
  cin >> a;
  cin >> b;
  Rectangle rect(a, b);
  Rectangle rectb(a, b);
  cout << "rect area: " << rect.area() << endl;
  cout << "rectb area: " << rectb.area() << endl;
  return 0;
}
