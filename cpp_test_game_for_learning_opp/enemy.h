#include "user.h"
#pragma once

class Enemy : public Player {
  public:
    Enemy(int health_, int strength_, std::string name_);
    Enemy(std::string name_);
};

class LightEnemy : public Player {
  public:
    LightEnemy(int health_, int strength_, std::string name_);
    LightEnemy(std::string name_);
};

class MediumEnemy : public Player {
  public:
    MediumEnemy(int health_, int strength_, std::string name_);
    MediumEnemy(std::string name_);
};

class HeavyEnemy : public Player {
  public:
    HeavyEnemy(int health_, int strength_, std::string name_);
    HeavyEnemy(std::string name_);
};
