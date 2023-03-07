#include <sys/wait.h>
#include <unistd.h>
#include <vector>
#include <iostream>
#include <string>
#include <array>
#include <algorithm>

using namespace std;

string pipeRead(int pipe)
{
    string message;
    char c;
    while (read(pipe, &c, 1) > 0)
        message += c;
    return message;
}

void pipeWrite(int pipe, std::string message)
{
    write(pipe, message.c_str(), message.length());
}

string pipesRead(vector<int> const& pipesIn)
{
    string message = "{";
    message += to_string(getpid());
    for (auto pipeIn : pipesIn)
    {
        message += ";";
        message += pipeRead(pipeIn);
    }
    message += "}";
    return message;
}


void childProcess(vector<int> const& pipesIn, vector<int> const& pipesOut)
{
    string message = pipesRead(pipesIn);
    for (auto pipeOut : pipesOut)
        pipeWrite(pipeOut, message);
}

vector<array<int, 2>> createPipes(int count)
{
    vector<array<int, 2>> pipes;
    for (int i = 0; i < count; ++i)
    {
        array<int, 2> newPipe;
        if (pipe(newPipe.data()) == -1)
        {
            perror("Error creating pipe.");
            exit(EXIT_FAILURE);
        }
        pipes.push_back(newPipe);
    }
    return pipes;
}

void closePipes(vector<int> pipes)
{
    for (auto& p : pipes)
        close(p);
}

void closePipes(vector<array<int, 2>> pipes, vector<int> exceptPipes)
{
    for (auto& p : pipes)
    {
        for( int i = 0; i < 2; ++ i)
            if( find( exceptPipes.begin(), exceptPipes.end(), p[i]) == exceptPipes.end())
                close(p[i]);
    }
}

int main(int argc, char* argv[])
{
    auto pipes = createPipes(7);

    if (fork() == 0)
    {
        // child 0
        vector<int> usedPipes = { pipes[0][1], pipes[1][1], pipes[2][1] };
        closePipes(pipes, usedPipes);
        childProcess({}, { pipes[0][1], pipes[1][1], pipes[2][1] });
        closePipes(usedPipes);
    }
    else
    if (fork() == 0)
    {
        // child 1
        vector<int> usedPipes = { pipes[1][0], pipes[4][1] };
        closePipes(pipes, usedPipes);
        childProcess({ pipes[1][0] }, { pipes[4][1] });
        closePipes(usedPipes);
    }
    else
    if (fork() == 0)
    {
        // child 2
        vector<int> usedPipes = { pipes[2][0], pipes[3][1] };
        closePipes(pipes, usedPipes);
        childProcess({ pipes[2][0] }, { pipes[3][1] });
        closePipes(usedPipes);
    }
    else
    if (fork() == 0)
    {
        // child 3
        vector<int> usedPipes = { pipes[3][0], pipes[6][1] };
        closePipes(pipes, usedPipes);
        childProcess({ pipes[3][0] }, { pipes[6][1] });
        closePipes(usedPipes);
    }
    else
    if (fork() == 0)
    {
        // child 4
        vector<int> usedPipes = { pipes[0][0], pipes[5][1] };
        closePipes(pipes, usedPipes);
        childProcess({ pipes[0][0] }, { pipes[5][1] });
        closePipes(usedPipes);
    }
    else
    {
        // parent
        vector<int> usedPipes = { pipes[6][0], pipes[4][0], pipes[5][0]  };
        closePipes(pipes, usedPipes);
        cout << pipesRead({ pipes[6][0], pipes[4][0], pipes[5][0]  }) << "\n";
        closePipes(usedPipes);
    }
    return 0;
}


