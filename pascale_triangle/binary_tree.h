// Binary Tree will be always full(no leafes) so i dont need to worry about some
// situations when i dont have
// // right nodes

#include <iostream>
#include <vector>

struct Node {
  int *coordinates[2];
  Node *left = nullptr;
  Node *right = nullptr;
};

class PascalBinaryTree {

public:
  PascalBinaryTree(int level);
  int countLevel();
  int returnWaysCount();
  std::vector<Node *> &show();
  void push(int *coordinates[]);
};
