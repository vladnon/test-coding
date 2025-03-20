#include <iostream>
#include <string>

using namespace std;

class Human {
  public:
    Human(int age_, string name_) : age(age_), name(name_) {}
    Human(int age_) : age(age_) {}
    Human(string name_) : name(name_) {}

    void setAge(int age_) { age = age_; }
    string hello_msg = "Hello, i am human!";
    void showInfo() {
        cout << "\nage: " << age << "\nname: " << name
             << "\nhello_msg: " << hello_msg << endl;
    }

  private:
    string name;
    int age;
};

class Coder : public Human {
  public:
    Coder(string name_) : Human(name_) {
        Human::hello_msg = "Hello, i am coder!";
        setAge(31);
    }
};

// class Builder : public Human {
//   public:
//     Builder(int age_, int name_) : Human(age_, name_) {}
// };

int main() {

    Human man(20, "human");
    man.showInfo();

    Coder coder("coder");
    coder.showInfo();
    // Builder builder(50, "builder");
    return 0;
}
