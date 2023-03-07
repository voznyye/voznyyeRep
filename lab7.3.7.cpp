#include <sys/wait.h>
#include <unistd.h>
#include <vector>
#include <iostream>
#include <string>
#include <array>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
    pid_t pid_4, pid_5, pid_6;
    int dad_pid = getpid();

    if (fork() == 0) { //child 1
        cout << "IM C 1 " << getpid() << " CHILD OF " << dad_pid << "\n";

        int d_pid = getpid();

        for (int j = 0; j < 3; j++) {
            wait(NULL);
        }
        for (int i = 0; i < 3; i++) {
            if (fork() == 0) // grandchild 1, 2, 3
            {
                cout << "IM GC " << i + 1 << ' ' << getpid() << " CHILD OF " << d_pid << "\n";
                break;
            }
        }
    }
    else
    if (fork() == 0) { // child 2

        int d_pid = getpid();
        int ex = 0;

        cout << "IM C 2 " << getpid() << " CHILD OF " << dad_pid << "\n";
        pid_4 = fork();
        if (pid_4 == 0) { // grandchild 4
            pid_4 = getpid();
            cout << "IM GC 4 " << pid_4 << " CHILD OF " << d_pid << "\n";
            while (true) {
                ex ++;
                if (ex == 666999)
                    break;
            }
        } else {
            pid_5 = fork();
            if (pid_5 == 0) { // grandchild 5
                pid_5 = getpid();
                cout << "IM GC 5 " << pid_5 << " CHILD OF " << d_pid << "\n";
                while (true) {
                    ex --;
                    if (ex == -666999)
                        break;
                }
            }
            waitpid(pid_4, NULL, 0);
            waitpid(pid_5, NULL, 0);
            kill(pid_4, SIGKILL);
            kill(pid_5, SIGKILL);
        }
    }
    else
    if (fork() == 0) { // child 3
        cout << "IM C 3 " << getpid() << " CHILD OF " << dad_pid << "\n";
        pid_6 = fork();
        if (pid_6 == 0) { // grandchild 6
            pid_6 = getpid();
            while (true) {
                cout << "IM GC 6 " << pid_6 << " CHILD OF " << dad_pid << "\n";
                break;
            }

        }
        waitpid(pid_6, NULL, 0);
        kill(pid_6,SIGKILL);
    }
    else // parent
    {
        for (int j = 0; j < 3; j++) {
            wait(NULL);
        }
        cout << "END " << getpid() << "\n";
    }
    return 0;
}

