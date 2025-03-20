#pragma once

#include "item.h"
#include <ctime>
#include <iostream>
#include <random>
#include <string>
#include <vector>

class Player {
  public:
    Player(std::string name_);
    Player(int health_, int strength_, std::string name_);

    std::string hello_text = "hi:)";
    std::string background_story;

    std::string id = "player";

    bool isHit();

    void updatePlayerStatus();

    void die();
    void showInformation();
    void showHelloText();
    void showStory();

    void hit(Player &person);
    void damage(int strength);

    int getHealth();
    int getStrength();
    bool isAlive();
    std::string getName();
    int getMoney();

    void setHealth(int hp_);
    void setStrength(int strength_);
    void setName(std::string name_);
    void setId(std::string id);
    void setAliveStatus(bool status);
    void setMoney(int money_);
    void setChanceToMiss(int chance_);

  private:
    int health;
    std::string name;
    int strength;
    bool alive = true;
    int money;
    int chanceToMiss = 5;
    std::vector<Item *> &inventory;
};
