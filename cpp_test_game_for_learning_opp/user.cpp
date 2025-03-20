#include "user.h"

Player::Player(int Health_, int strength_, std::string name_)
    : health(Health_), strength(strength_), name(name_) {}

Player::Player(std::string name_) : name(name_) {};

void Player::showInformation() {
    std::cout << "\nname: " << name << "\nhp: " << health
              << "\nstrength: " << strength << "\nid: " << id << std::endl;
    // std::cout << background_story << std::endl;
}

void Player::damage(int strength) {
    std::cout << name << " have earned " << strength << " damage" << std::endl;
    health -= strength;
    std::cout << "His health now is " << health << std::endl;
}
void Player::hit(Player &person) {
    if (!isHit()) {
        std::cout << "\n" << name << " have missed " << std::endl;
        for (long long i = 0; i < 1000000000; i++) {
        }
        return;
    } else {
        std::cout << "\n" << name << " have hit " << person.name << std::endl;
        person.damage(strength);
        for (long long i = 0; i < 1000000000; i++) {
        }
    }
}

bool Player::isHit() {
    srand(time(NULL));
    int chance = rand() % chanceToMiss;
    if (chance == 1) {
        return false;
    }
    return true;
}

void Player::updatePlayerStatus() {
    if (health <= 0) {
        alive = false;
        die();
    }
}

void Player::die() { std::cout << "\n" << name << " have died" << std::endl; }
void Player::showStory() { std::cout << background_story << std::endl; }
void Player::showHelloText() { std::cout << hello_text << std::endl; }

int Player::getHealth() { return health; }
int Player::getStrength() { return strength; }
std::string Player::getName() { return name; }
bool Player::isAlive() { return alive; }
int Player::getMoney() { return money; }

void Player::setName(std::string name_) { name = name_; }
void Player::setHealth(int health_) { health = health_; }
void Player::setStrength(int strength_) { strength = strength_; }
void Player::setId(std::string id_) { id = id_; }
void Player::setAliveStatus(bool status_) { alive = status_; };
void Player::setMoney(int money_) { money = money_; }
void Player::setChanceToMiss(int chance_) { chanceToMiss = chance_; }
