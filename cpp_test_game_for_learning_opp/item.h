#pragma once

#include <iostream>
#include <string>
#include <vector>

class Item {
  public:
    bool getEffect();
    bool getApplication();
    std::string getCondition();
    std::string getName();

    void use();

    void setEffect(bool effect_);
    void setApplication(bool application_);
    void setName(std::string name_);

  private:
    bool effect; // add or take
    std::string condition;
    bool application; // player or enemy
    std::string name;
};

class Shield : public Item {
  public:
    // void use(Player &player);
};
class Potion : Item {};
class Spell : Item {};
