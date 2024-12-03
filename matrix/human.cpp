#include <iostream>
#include <map>
#include <string>
#include <vector>

class Human {
    int id;
    int age;
    std::string name;
    std::string family_name;

  public:
    Human(int id, int age, std::string name, std::string family_name) {
        this->id = id;
        this->age = age;
        this->name = name;
        this->family_name = family_name;
    }

    int getAge() const { return age; }
    int getId() const { return id; }
    std::string getName() const { return name; }
    std::string getFamilyName() const { return family_name; }

    void sayHello() {
        std::cout << "Hello!\n"
                  << "My name is\t" << name << "\nMy age is\t" << age
                  << "\nMy id is id\t" << id << "\nMy family name"
                  << family_name << std::endl;
    }
};

int main() {
    Human nobody = Human(0, 18, "nobody", "nobody");
    nobody.sayHello();
    return 0;
}
