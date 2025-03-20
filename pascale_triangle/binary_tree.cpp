#include <cmath>
#include <iostream>
#include <vector>

// TODO u need to work this things:
// 1. the level counting system working wrong
// 2. put fucking value to ur nodes, it will much easier to debug this shit
// 3. rework balance system: instead of copying Node object
// u need to put left_node->right address to a right_node->left

struct Node {
  int *coordinates;
  Node *left = nullptr;
  Node *right = nullptr;
  int level = 0;
  // int value;

  Node(int *coordinates_, int level_)
      : coordinates(coordinates_), level(level_) {}
  Node(int *coordinates_) : coordinates(coordinates_) {}
};

class PascalBinaryTree {

public:
  PascalBinaryTree(int level) {
    createFullTree(level);
    // balance();
  }

  int show() {
    // std::cout << "showing" << std::endl;
    std::vector<int> result;
    std::vector<Node *> stack = {root};
    int count = 0;

    while (!stack.empty()) {
      Node *cur_node = stack.back();
      stack.pop_back();
      result.push_back(1);
      count++;

      if (cur_node->right) {
        stack.push_back(cur_node->right);
      }

      if (cur_node->left) {
        stack.push_back(cur_node->left);
      }
    }
    return count;
  }

  int count() { return countLevels(); }

private:
  Node *root = nullptr;

  // it doesnt work. it creates new object. u need not to create new object, u
  // need to make left_node->right(link) = right_node->left(link)
  //
  void balance() {
    Node *left_node = root;
    Node *right_node = root;

    int level = countLevels();

    // std::cout << level << std::endl;

    while (level > 0) {

      left_node->right = right_node->left;

      left_node = left_node->left;
      right_node = right_node->right;

      level--;
    }
  }

  int countLevels() {
    Node *cur_node = root;

    while (cur_node->left) {
      cur_node = cur_node->left;
      std::cout << cur_node->level << std::endl;
    }

    return cur_node->level;
  }

  void push(int *coordinates) {
    // std::cout << "pushing" << std::endl;
    Node *new_node = new Node(coordinates);

    if (!root) {
      root = new_node;
      return;
    }

    Node *cur_node = root;

    while (cur_node) {
      if (!cur_node->left) {
        std::cout << cur_node->level << std::endl;
        cur_node->left = new Node(coordinates, cur_node->level + 1);
        return;
      } else if (!cur_node->right) {
        std::cout << cur_node->level << std::endl;
        cur_node->right = new Node(coordinates, cur_node->level + 1);
        return;
      } else {
        cur_node = cur_node->left;
      }
    }
  }

  // doesnt work great. sometimes returns wrong result
  void createFullTree(int level) {
    int nodes = 0;
    for (int i = 0; i <= level; i++) {
      int power = std::pow(2, level - 1);
      nodes += power;
    }
    for (int i = 0; i < nodes; i++) {
      int coord[2] = {1, 2};
      push(coord);
    }
  }

  int *calculateCoordinates(Node *parent) {
    int *coords = new int[2];
    return coords;
  }
};

int main() {

  PascalBinaryTree *tree = new PascalBinaryTree(2);
  // std::cout << tree->show() << std::endl;
  std::cout << tree->count() << std::endl;
  delete tree;

  return 0;
}
