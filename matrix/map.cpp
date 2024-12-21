#include <iostream>
#include <string>

class GameMap {
    std::string game_map[40][50];

    void removeExtraColumns() {}

  public:
    void fillMap() {
        for (int i = 0; i < 40; i++) {
            for (int j = 0; j < 50; j++) {
                game_map[i][j] = '"';
            }
        }
    }

    void printMap() {
        for (int i = 0; i < 40; i++) {
            for (int j = 0; j < 50; j++) {
                std::cout << game_map[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }

    void setValue(int x, int y, std::string name) { game_map[x][y] = name; }

    void updateMap() {}
};

int main() {
    GameMap game_map = GameMap();
    game_map.fillMap();
    game_map.setValue(5, 10, "Player_nothing");
    game_map.printMap();
}
