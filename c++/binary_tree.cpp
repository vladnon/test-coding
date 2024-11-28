#include <iostream>
#include <queue>

struct Node {
    int value;
    Node *left = NULL;
    Node *right = NULL;

    Node(int value_) { this->value = value_; }
};

class BinaryTree {
    Node *head = NULL;

  public:
    void append(int value) {
        Node *new_node = new Node(value);
        Node *cur_node = head;
        if (!head) {
            head = new Node(value);
            return;
        }

        while (cur_node) {
            if (!cur_node->left) {
                cur_node->left = new_node;
                return;
            } else if (!cur_node->right) {
                cur_node->right = new_node;
                return;
            } else {
                cur_node = cur_node->left;
            }
        }
    }

    void printBinaryTree() {
        Node *cur_node = head;
        std::queue<Node> queue;

        while (cur_node) {
            std::cout << cur_node->value;
            if (cur_node->right) {
                queue.push_back(cur_node->right);
            }
        }
    }
};

int main() { return 0; }
