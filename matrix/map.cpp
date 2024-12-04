#include <iostream>
#include <string>

class GameMap {
    std::string game_map[20][30];

  public:
    void fillMap() {
        for (int i = 0; i < 20; i++) {
            for (int j = 0; j < 30; j++) {
                game_map[i][j] = "0";
            }
        }
    }

    void printMap() {
        for (int i = 0; i < 20; i++) {
            for (int j = 0; j < 30; j++) {
                std::cout << game_map[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }

    void updateMap() {}
};

int main() {
    GameMap game_map = GameMap();
    game_map.fillMap();
    game_map.printMap();
}
