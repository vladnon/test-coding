#include "item.h"

void Item::use() {
    std::cout
        << "You have user used abstract item\nNothing will happen, dont worry"
        << std::endl;
}

bool Item::getEffect() { return effect; }
std::string Item::getCondition() { return condition; }
bool Item::getApplication() { return application; }
std::string Item::getName() { return name; }

void Item::setApplication(bool application_) { application = application_; };
void Item::setEffect(bool effect_) { effect = effect_; };
void Item::setName(std::string name_) { name = name_; }

// void Shield::use(Player &player) {
// std::cout << player.getName() << " used " << getName() << std::endl;
// }
