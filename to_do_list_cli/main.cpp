#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include <string>
#include <vector>
using json = nlohmann::json;
using namespace std;

// TODO i want to add commits, like failed or fill finish toworrow, and create
// json file for statics, like n tasks u have finished, k u have failed, m u
// havent complete

struct Task {
    string name;        // name of task
    string description; // information about task
    string commit;
    int status; // 0 - didnt start, 1 started, 2 - finished
};

class ToDoList {
    vector<Task> tasks;

    void addTask_(string name, string description, int status, string commit) {
        Task new_task = Task();
        new_task.name = name;
        new_task.description = description;
        new_task.status = status;
        new_task.commit = commit;
        tasks.push_back(new_task);
    }

    void addTask_(string name, string description, int status) {
        Task new_task = Task();
        new_task.name = name;
        new_task.description = description;
        new_task.status = status;
        new_task.commit = "";
        tasks.push_back(new_task);
    }

    void addTask_(string name, string description) {
        Task new_task = Task();
        new_task.name = name;
        new_task.description = description;
        new_task.commit = "";
        tasks.push_back(new_task);
    }

    void addTask() {
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Write tasks name, or back to menu(b)" << endl << ":";

        string name;
        getline(cin, name);

        if (name == "b") {
            menu();
        }

        cout << "\nWrite tasks description" << endl << ":";
        string description;
        getline(cin, description);

        cout << "\nNew task has added" << endl;
        addTask_(name, description);
        menu();
    }

    void updateStatus() {
        printTasks(1);
        cout << "\nChoose task to update status, or back to menu(0)" << endl;
        cout << ":";
        int num;
        cin >> num;
        if (num == 0) {
            menu();
        }
        tasks[num - 1].status++;
        cout << "\nThe tasks status has updated" << endl;
        menu();
    }

    // dont forget, that you are writing on fucking c++, u have overloads
    void printTasks(int mode) {
        if (tasks.size() == 0) {
            cout << "No tasks yet\n";
            if (mode == 0) {
                menu();
            }
        }

        for (int i = 0; i < tasks.size(); i++) {
            string status;
            if (tasks[i].status == 0) {
                status = "uncompleted ";
            } else if (tasks[i].status == 1) {
                status = "in progress 󰦖";
            } else {
                status = "completed ";
            }
            if (tasks[i].commit == "") {
                cout << "\n"
                     << i + 1 << ". Name: " << tasks[i].name
                     << "\t Description: " << tasks[i].description
                     << "\tStatus: " << status
                     << "\tCommit: " << "No commits yet" << endl;
            } else {
                cout << "\n"
                     << i + 1 << ". Name: " << tasks[i].name
                     << "\t Description: " << tasks[i].description
                     << "\tStatus: " << status
                     << "\tCommit: " << tasks[i].commit << endl;
            }
        }
        if (mode == 0) {
            menu();
        }
    }

    void LoadToHistory() {}
    void uploadFromHistory() {}
    void printHistory() {}

    void addCommit() {
        printTasks(1);
        cout << "\nChoose task number, or back to menu(0)" << endl << ":";

        int number;
        cin >> number;

        if (number == 0) {
            menu();
        }

        cout << "\nWrite tasks commit" << endl << ":";
        string commit;
        cin >> commit;
        this->tasks[number - 1].commit = commit;
        menu();
    }

    void loadToJson() {
        json j;
        string filename = "main.json";
        ofstream file(filename);

        if (file.is_open()) {
            for (int i = 0; i < tasks.size(); i++) {
                j[i] = {{"name", tasks[i].name},
                        {"description", tasks[i].description},
                        {"status", tasks[i].status},
                        {"commit", tasks[i].commit}};
            }
            file << j.dump(4);
            file.close();
        }
    }

    void unloadFromJson() {
        string filename = "main.json";
        ifstream file(filename);

        if (file.is_open()) {
            if (file.peek() == ifstream::traits_type::eof()) {
                file.close();
                return;
            }
            json j;
            file >> j;
            for (const auto &new_task : j) {
                addTask_(new_task["name"], new_task["description"],
                         new_task["status"], new_task["commit"]);
            }
            file.close();
        }
    }

    void clearJson() {
        string filename = "main.json";
        ofstream file(filename);

        if (file.is_open()) {
            json j;
            file.clear();
            file << j.dump(4);
            file.close();
        }
    }

    void menu() {
        cout << "\n------------------------------\n"
             << "\nWhat do you want to do?\n"
             << endl;

        string help =
            "0 - help\n1 - add task\n2 - update status\n3 - show tasks\n4 - "
            "save and exit\n5 - clear tasks \n6 - add a commit(u can write "
            "will do next day/ failed)\n7 - "
            "history\n";

        cout << "Write 0 for help\n";
        cout << ":";
        int action;
        cin >> action;
        cout << "\n";
        if (action == 0) {
            cout << help;
            menu();
        } else if (action == 1) {
            addTask();
        } else if (action == 2) {
            updateStatus();
        } else if (action == 3) {
            printTasks(0);
        } else if (action == 4) {
            loadToJson();
        } else if (action == 5) {
            clearJson();
        } else if (action == 6) {
            addCommit();
        } else if (action == 7) {
            printHistory();
        } else {
            cout << "wtf" << endl;
            menu();
        }
    }

  public:
    void start() {
        unloadFromJson();
        menu();
    }
};

int main() {
    ToDoList list = ToDoList();
    list.start();
    return 0;
}
