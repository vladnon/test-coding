#pragma once

#include "item.h"
#include <iostream>
#include <string>
#include <vector>

class Market {
  public:
    std::vector<Item *> items;

    Item &buyItem();

  private:
};
