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
        if (checkIfListIsEmpty()) {
            return;
        }
        Node *node = head;
        head = head->next;
        delete node;
    }

    bool checkIfListIsEmpty() {
        if (!head) {
            cout << "The list is empty!" << endl;
            return true;
        }
        return false;
    }

    bool find(int value) {
        Node *node = head;

        while (node) {
            if (node->value == value) {
                return true;
            }
            node = node->next;
        }
        return false;
    }

    int size() {
        int count = 0;
        Node *node = head;

        while (node) {
            count++;
            node = node->next;
        }

        return count;
    }

    void removeFromTheEnd() {
        if (checkIfListIsEmpty()) {
            return;
        }
        Node *node = head;

        while (node->next->next) {
            node = node->next;
        }
        delete node->next;
        node->next = NULL;
    }

    void remove(int value) {
        if (checkIfListIsEmpty()) {
            return;
        }
        Node *node = head;

        if (node->value == value) {
            removeFromBeginng();
            return;
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

    Node popFront() {
        Node *node = head;
        Node *tmp = head;
        head = head->next;
        cout << "this is working :)" << endl;
        delete node;
        return *tmp;
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
    cout << "the linked list has created" << endl;
    LinkedList list = LinkedList();
    // vector<int> arr(10000);
    // list = createListFromArray(arr, list);
    // cout << "this is fine";
    list.append(10);
    list.append(234);
    list.append(0);
    list.append(143);
    list.append(50);
    list.append(90);
    list.append(23);
    list.append(211);
    list.append(98);
    // cout << "the list: " << list.print() << endl;
    //
    // cout << "after removing the first node" << endl;
    // list.removeFromBeginng();
    //
    // cout << list.print() << endl;
    // cout << "after removing the last node" << endl;
    // list.removeFromTheEnd();
    // cout << list.print() << endl;
    //
    // cout << "after removing 50 " << endl;
    // list.remove(50);
    // cout << list.print() << endl;
    //
    // cout << "show list size: " << list.size() << endl;
    // cout << boolalpha;
    // cout << "finding 234 in the list: " << list.find(234) << endl;
    //
    // list.remove(234);
    // cout << "finding 234 in the after removing it: " << list.find(234) <<
    // endl;
    //
    // cout << "My linked list: " << list.print() << endl;
    Node node = list.popFront();
    cout << node.value << endl;
    return 0;
}
