#include <cstddef>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Node {
  int value;
  Node *next = NULL;
};

class LinkedList {
  Node *head;

public:
  LinkedList() { head = NULL; }
  void append(int value) {
    Node *new_node = new Node();
    new_node->value = value;

    if (!this->head) {
      new_node->next = head;
      head = new_node;

    } else {
      Node *cur_node = head;
      while (cur_node->next) {
        cur_node = cur_node->next;
      }
      cur_node->next = new_node;
    }
  }

  string print() {
    Node *node = head;
    string result;
    while (node) {
      result += (to_string(node->value)) + " ";
      node = node->next;
    }
    return result;
  }

  void removeFromBeginng() {
    Node *node = head;
    head = head->next;
    delete node;
  }

  void remove(int value) {
    if (!head) {
      cout << "The list is empty" << endl;
      return;
    }

    Node *node = head;

    if (node->value == value) {
      removeFromBeginng();
    }
    while (node->next) {
      if (node->next->value == value) {
        Node *node_to_delete = node->next;
        node->next = node_to_delete->next;
        delete node_to_delete;
        break;
      }
      node = node->next;
    }
  }
};

LinkedList createListFromArray(vector<int> arr, LinkedList list) {
  for (int i = 0; i < arr.size(); i++) {
    int num = arr[i];
    list.append(num);
  }
  return list;
}

int main() {
  LinkedList list = LinkedList();
  vector<int> arr(10000000000000000);
  list = createListFromArray(arr, list);
  // cout << "this is fine";
  // list.remove(10);

  cout << "My linked list: " << list.print() << endl;
  return 0;
}
