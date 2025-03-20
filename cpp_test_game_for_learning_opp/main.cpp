#include "enemy.h"
#include "user.h"

// TODO сделать родительский класс user, от него будут наследоваться классы
// player и enemy, и все остальные enemy

void start_game() {
    int answer;
    std::cout << "Hello hero. We need you. Enemies have attacked our village. "
                 "\nGo staight 5 times and you will see a lot of enemies!!!"
              << std::endl;
    std::cout << "1 answer: Go fuck yourself, I dont  want to do that"
              << std::endl;
    std::cout
        << "2 answer: Ok, i will do it for you but you need to give me my money"
        << std::endl;
    std::cout << "3 answer: I will do it for free" << std::endl;
    std::cin >> answer;
    switch (answer) {
    case 1:
        std::cout << "The game finished. Enemies killed everyone in the village"
                  << std::endl;
        return;
    case 2:
        std::cout << "You have to fight with 2 light enemies and this guy will "
                     "give u 50 coins"
                  << std::endl;
    case 3:
        std::cout << "You have to fight with 2 light enemies and this guy will "
                     "marry you with his daughter"
                  << std::endl;
    }
    for (long long i = 0; i < 1000000000; i++) {
    }
    return;
}

void checkWhichEnemyIsDead(std::vector<Player *> &enemies,
                           std::vector<Player *> &dead_enemies) {
    std::vector<Player *> result;
    for (Player *enemy : enemies) {
        if (!enemy->isAlive()) {
            result.push_back(enemy);
        }
    }
    for (Player *enemy : result) {
        dead_enemies.push_back(enemy);
    }
}

void playerEnemyAttack(Player &player, std::vector<Player *> &enemies) {
    for (Player *enemy : enemies) {
        if (!player.isAlive()) {
            return;
        }
        player.hit(*enemy);
        enemy->updatePlayerStatus();
        if (enemy->isAlive()) {
            enemy->hit(player);
            player.updatePlayerStatus();
        }
    }
}

void enemiesDying(std::vector<Player *> &enemies) {
    for (auto it = enemies.begin(); it != enemies.end();) {
        if (!(*it)->isAlive()) {
            delete *it;
            it = enemies.erase(it);
        } else {
            ++it;
        }
    }
}

void fight(Player &player, std::vector<Player *> &enemies, int size) {
    std::cout << "\nThe fight started" << std::endl;
    std::vector<Player *> dead_enemies = {};
    while (player.isAlive()) {
        playerEnemyAttack(player, enemies);

        checkWhichEnemyIsDead(enemies, dead_enemies);

        if (size == dead_enemies.size()) {
            std::cout << "\nYou killed every enemy on your way\nYou are hero!!!"
                      << std::endl;
            return;
        }

        enemiesDying(dead_enemies);
    }
    std::cout << "\nYou have died in the fight\nYou are so newbie!!!"
              << std::endl;
}

int main() {
    // start_game();
    Player *vova = new Player(90, 15, "player");
    HeavyEnemy *vlad = new HeavyEnemy("enemy");
    LightEnemy *bogdan = new LightEnemy("enemy2");
    Enemy *somebody = new Enemy("enemy3");

    std::vector<Player *> enemies;
    enemies.push_back(vlad);
    enemies.push_back(bogdan);

    fight(*vova, enemies, enemies.size());

    delete vova;

    return 0;
}
