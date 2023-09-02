section .data
    numbers db 98 dup(1)  ; 1 means unmarked (prime), 0 means marked (not prime)

section .text
    global _start

_start:
    mov ecx, 2          ; Starting number

outer_loop:
    cmp ecx, 10         ; Prime numbers greater than sqrt(100) won't have multiples under 100
    jae done

    ; If the number is marked (not prime), skip to next number
    mov al, [numbers + ecx - 2]
    test al, al
    jz next_outer

    ; Start marking multiples of ecx
    mov edx, ecx

marking_loop:
    add edx, ecx
    cmp edx, 100
    jae next_outer      ; If multiple exceeds 99, move to next outer number
    mov [numbers + edx - 2], 0   ; Mark the multiple as not prime

next_outer:
    inc ecx
    jmp outer_loop

done:
    ; Exit the program (for Linux)
    mov eax, 0x60      ; syscall: exit
    xor edi, edi       ; status: 0
    syscall

