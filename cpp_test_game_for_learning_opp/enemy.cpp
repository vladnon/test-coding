#include "enemy.h"

Enemy::Enemy(int hp_, int strength_, std::string name_)
    : Player(hp_, strength_, name_) {}

Enemy::Enemy(std::string name_) : Player(name_) {
    Player::setHealth(50);
    Player::setStrength(5);
    setId("enemy");
}

LightEnemy::LightEnemy(int hp_, int strength_, std::string name_)
    : Player(hp_, strength_, name_) {}

LightEnemy::LightEnemy(std::string name_) : Player(name_) {
    Player::setHealth(75);
    Player::setStrength(10);
    Player::setChanceToMiss(5);
    setId("light_enemy");
};

MediumEnemy::MediumEnemy(int hp_, int strength_, std::string name_)
    : Player(hp_, strength_, name_) {}

MediumEnemy::MediumEnemy(std::string name_) : Player(name_) {
    Player::setHealth(90);
    Player::setStrength(15);
    Player::setChanceToMiss(3);
    setId("medium_enemy");
};

HeavyEnemy::HeavyEnemy(int hp_, int strength_, std::string name_)
    : Player(hp_, strength_, name_) {}

HeavyEnemy::HeavyEnemy(std::string name_) : Player(name_) {
    Player::setHealth(110);
    Player::setStrength(20);
    Player::setChanceToMiss(2);
    Player::setId("heavy_enemy");
};
