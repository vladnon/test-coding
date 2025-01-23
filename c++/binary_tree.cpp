#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int value;
    Node *left = NULL;
    Node *right = NULL;

    Node(int value_) { value = value_; }
};

class BinaryTree {

    bool searchRecursive(Node *node, int target) {
        if (node == NULL) {
            return false;
        }
        if (node->value == target) {
            return true;
        }
        return searchRecursive(node->left, target) ||
               searchRecursive(node->right, target);
    }

    bool printBinaryTree(Node *current) {
        if (current == NULL) {
            return false;
        }
        cout << current->value << endl;
        return printBinaryTree(current->left) ||
               printBinaryTree(current->right);
    }

  public:
    Node *head = NULL;

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

    bool search(int value) {
        cout << "\nSearching node with value: " << value << endl;
        return searchRecursive(head, value);
    }

    bool print() {
        cout << "\nPrinting binary tree" << endl;
        return printBinaryTree(head);
    };
};

int main() {
    BinaryTree *binary_tree = new BinaryTree();
    binary_tree->append(10);
    binary_tree->append(234);
    binary_tree->append(108);
    binary_tree->append(75);
    binary_tree->append(29);
    binary_tree->append(290);
    bool result_searching = binary_tree->search(29);
    if (result_searching == 1) {
        cout << "True" << endl;
    } else {
        cout << "False" << endl;
    }
    binary_tree->print();
    return 0;
}
