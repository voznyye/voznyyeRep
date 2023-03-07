#include <sys/wait.h>
#include <unistd.h>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
    pid_t pid_1 = fork();
    if (pid_1 == 0) {
        int x ,y;
        cout << getpid() << " 1 number " << endl;
        cin >> x;
        cout << getpid() << " 2 number " << endl;
        cin >> y;
        cout << "result " << x + y << "\n" << endl;
    }
    else {
        waitpid(pid_1, NULL, 0);

        pid_t pid_2 = fork();
        if (pid_2 == 0) {
            string a;
            cout << getpid() << "  What is your name " << endl;
            cin >> a;
            cout << getpid() << " Hi " << a << "\n";
        }
        else {
            waitpid(pid_2, NULL, 0);
            cout << getpid() << " Parent" << endl;
        }
    }
    return 0;
}
