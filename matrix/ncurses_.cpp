#include <ncurses.h>

// class Window {
//   private:
//
//   public:
//     Window() {}
// };

int main() {
    // int ncols = 10, nlines = 10, y0 = 5, x0 = 5;
    initscr();
    // WINDOW *win = newwin(nlines, ncols, y0, x0);

    mvprintw(10, 10, "something");
    refresh();
    getch();
    endwin();

    return 0;
}
