// ABC

#include <iostream>
#include <string>
#include "monitor.h"

int const threadsCounts = 3;  //liczba wątków

int const numberOfLettersA = 20;
int const numberOfLettersB = 20;
int const numberOfLettersC = 20;

std::string s;

Semaphore semA(1);
Semaphore semB(0);
Semaphore semC(0);
//TODO dodać i zainicjować wymagany semafor/semafory

void writeA()
{
    semA.p();
    std::cout << "A" << std::flush;
    s += "A";
    semB.v();

}

void writeB()
{
    semB.p();
    std::cout << "B" << std::flush;
    s += "B";
    semC.v();
}

void writeC()
{
    semC.p();
    std::cout << "C" << std::flush;
    s += "C";
    semA.v();
}

void* threadA(void* arg)
{
    for (int i = 0; i < numberOfLettersA; ++i)
    {
        writeA();
    }
    return NULL;
}

void* threadB(void* arg)
{
    for (int i = 0; i < numberOfLettersB; ++i)
    {
        writeB();
    }
    return NULL;
}

void* threadC(void* arg)
{
    for (int i = 0; i < numberOfLettersC; ++i)
    {
        writeC();
    }
    return NULL;
}

int main()
{
#ifdef _WIN32
    HANDLE tid[threadsCounts];
	DWORD id;

	// utworzenie wątków
	tid[0] = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)threadA, 0, 0, &id);
	tid[1] = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)threadB, 0, 0, &id);
    tid[2] = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)threadC, 0, 0, &id);

	// czekaj na zakończenie wątków
	for (int i = 0; i <= threadsCounts; i++)
		WaitForSingleObject(tid[i], INFINITE);
#else
    pthread_t tid[threadsCounts];

    // utworzenie wątków
    pthread_create(&(tid[0]), NULL, threadA, NULL);
    pthread_create(&(tid[1]), NULL, threadB, NULL);
    pthread_create(&(tid[2]), NULL, threadC, NULL);

    //czekaj na zakończenie wątków
    for (int i = 0; i < threadsCounts; i++)
        pthread_join(tid[i], (void**)NULL);
#endif
    std::cout << "\n";
    std::cout << "s=" << s << "\n";
    return 0;
}

// CAB

#include <iostream>
#include <string>
#include "monitor.h"

int const threadsCounts = 3;  //liczba wątków

int const numberOfLettersA = 20;
int const numberOfLettersB = 20;
int const numberOfLettersC = 20;

std::string s;

Semaphore semA(0);
Semaphore semB(0);
Semaphore semC(1);
//TODO dodać i zainicjować wymagany semafor/semafory

void writeA()
{
    semA.p();
    std::cout << "A" << std::flush;
    s += "A";
    semB.v();

}

void writeB()
{
    semB.p();
    std::cout << "B" << std::flush;
    s += "B";
    semC.v();
}

void writeC()
{
    semC.p();
    std::cout << "C" << std::flush;
    s += "C";
    semA.v();
}

void* threadA(void* arg)
{
    for (int i = 0; i < numberOfLettersA; ++i)
    {
        writeA();
    }
    return NULL;
}

void* threadB(void* arg)
{
    for (int i = 0; i < numberOfLettersB; ++i)
    {
        writeB();
    }
    return NULL;
}

void* threadC(void* arg)
{
    for (int i = 0; i < numberOfLettersC; ++i)
    {
        writeC();
    }
    return NULL;
}

int main()
{
#ifdef _WIN32
    HANDLE tid[threadsCounts];
	DWORD id;

	// utworzenie wątków

	tid[1] = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)threadA, 0, 0, &id);
	tid[2] = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)threadB, 0, 0, &id);
    tid[0] = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)threadC, 0, 0, &id);
	// czekaj na zakończenie wątków
	for (int i = 0; i <= threadsCounts; i++)
		WaitForSingleObject(tid[i], INFINITE);
#else
    pthread_t tid[threadsCounts];

    // utworzenie wątków

    pthread_create(&(tid[1]), NULL, threadA, NULL);
    pthread_create(&(tid[2]), NULL, threadB, NULL);
    pthread_create(&(tid[0]), NULL, threadC, NULL);

    //czekaj na zakończenie wątków
    for (int i = 0; i < threadsCounts; i++)
        pthread_join(tid[i], (void**)NULL);
#endif
    std::cout << "\n";
    std::cout << "s=" << s << "\n";
    return 0;
}


// AABCCC

#include <iostream>
#include <string>
#include "monitor.h"
#include <vector>

int const threadsCounts = 3;  //liczba wątków

int const numberOfLettersA = 20;
int const numberOfLettersB = 10;
int const numberOfLettersC = 30;

std::string s;
std::vector<char> chars;

Semaphore semA(1);
Semaphore semB(0);
Semaphore semC(0);

//TODO dodać i zainicjować wymagany semafor/semafory

void writeA()
{
    semA.p();
    std::cout << "A" << std::flush;
    s += "A";
    chars.push_back('A');
    semA.v();
    if (chars[chars.size() -1] == 'A' && chars[chars.size() -2] == 'A') {
        semA.p();
        semB.v();
    }
}

void writeB()
{
    semB.p();
    std::cout << "B" << std::flush;
    s += "B";
    chars.push_back('B');
    if (chars[chars.size() -1] == 'B') {
        semC.v();
    }
}

void writeC() {
    semC.p();
    std::cout << "C" << std::flush;
    s += "C";
    chars.push_back('C');
    semC.v();
    if (chars[chars.size() -1] == 'C' && chars[chars.size() -2] == 'C' && chars[chars.size() -3] == 'C') {
        semC.p();
        semA.v();
    }
}

void* threadA(void* arg)
{
    for (int i = 0; i < numberOfLettersA; ++i)
    {
        writeA();
    }
    return NULL;
}

void* threadB(void* arg)
{
    for (int i = 0; i < numberOfLettersB; ++i)
    {
        writeB();
    }
    return NULL;
}

void* threadC(void* arg)
{
    for (int i = 0; i < numberOfLettersC; ++i)
    {
        writeC();
    }
    return NULL;
}

int main()
{
#ifdef _WIN32
    HANDLE tid[threadsCounts];
	DWORD id;

	// utworzenie wątków
	tid[0] = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)threadA, 0, 0, &id);
	tid[1] = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)threadB, 0, 0, &id);
    tid[2] = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)threadC, 0, 0, &id);

	// czekaj na zakończenie wątków
	for (int i = 0; i <= threadsCounts; i++)
		WaitForSingleObject(tid[i], INFINITE);
#else
    pthread_t tid[threadsCounts];

    // utworzenie wątków
    pthread_create(&(tid[0]), NULL, threadA, NULL);
    pthread_create(&(tid[1]), NULL, threadB, NULL);
    pthread_create(&(tid[2]), NULL, threadC, NULL);

    //czekaj na zakończenie wątków
    for (int i = 0; i < threadsCounts; i++)
        pthread_join(tid[i], (void**)NULL);
#endif
    std::cout << "\n";
    std::cout << "s=" << s << "\n";
    return 0;
}


