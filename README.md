# CVM++
### Stack-Based Virtual Machine & Custom Compiler

CVM++ is a custom scripting language built entirely in **C++**, designed to demonstrate how programming languages work internally.

The project implements the complete compilation pipeline:

Source Code → Lexer → Parser → AST → Bytecode Compiler → Stack-Based Virtual Machine

Instead of relying on existing runtimes, CVM++ compiles source programs into a custom bytecode format which is then executed by a proprietary stack machine runtime.

---

# Features

## Frontend

✅ Lexer / Tokenizer  
✅ Recursive Descent Parser  
✅ Abstract Syntax Tree (AST) Generation  
✅ AST Debug Printer  
✅ Syntax Diagnostics  

## Compiler

✅ Bytecode Generation  
✅ Custom Instruction Set Architecture (ISA)  
✅ Variable Memory Handling  
✅ Control Flow Compilation  

## Runtime

✅ Stack-Based Virtual Machine  
✅ Bytecode Execution Engine  
✅ Runtime Error Handling  
✅ REPL Support  
✅ File Runner  
✅ Debug Mode  

---

# Architecture

```text
Source Program (.cvm)
        │
        ▼
Lexer
(Tokenization)
        │
        ▼
Parser
(AST Construction)
        │
        ▼
Compiler
(Bytecode Generation)
        │
        ▼
Virtual Machine
(Stack Execution Runtime)
        │
        ▼
Program Output
```

---

# Supported Language Features

## Variables

```c
let x = 10;
let y = input();
```

---

## Arithmetic Operations

```c
print(a + b);
print(a - b);
print(a * b);
print(a / b);
```

Supported:

- Addition `+`
- Subtraction `-`
- Multiplication `*`
- Division `/`

---

## Comparisons

```c
print(x > 0);
print(x < 0);
print(x == 0);
```

Boolean values:

```text
1 → true
0 → false
```

---

## if / else

```c
if (x > 0)
{
    print(1);
}
else
{
    print(0);
}
```

Nested conditions are supported.

---

## while Loops

```c
let x = input();

while (x > 0)
{
    print(x);
    x = x - 1;
}
```

---

# Instruction Set Architecture (ISA)

| Opcode | Description |
|---------|------------|
| PUSH | Push constant onto stack |
| ADD | Addition |
| SUB | Subtraction |
| MUL | Multiplication |
| DIV | Division |
| STORE | Store variable |
| LOAD | Load variable |
| GT | Greater Than |
| LT | Less Than |
| EQ | Equality |
| PRINT | Output value |
| INPUT | Read input |
| JMP | Unconditional jump |
| JMP_IF_FALSE | Conditional jump |
| HALT | Stop execution |

---

# Grammar

```text
program     -> statement* EOF

statement   -> varDecl
             | assignment
             | printStmt
             | ifStmt
             | whileStmt
             | block

varDecl     -> "let" IDENTIFIER "=" expression ";"

assignment  -> IDENTIFIER "=" expression ";"

printStmt   -> "print" "(" expression ")" ";"

ifStmt      -> "if" "(" expression ")" block
               ("else" block)?

whileStmt   -> "while" "(" expression ")" block

block       -> "{" statement* "}"

expression  -> equality

equality    -> comparison
               ("==" comparison)*

comparison  -> term
               ((">" | "<") term)*

term        -> factor
               (("+" | "-") factor)*

factor      -> unary
               (("*" | "/") unary)

unary       -> "-" unary
             | primary

primary     -> NUMBER
             | IDENTIFIER
             | "(" expression ")"
             | input()
```

---

# Build Instructions

Compile project:

```bash
make
```

Clean build files:

```bash
make clean
```

---

# Running CVM++

## REPL Mode

```bash
./main
```

---

## Execute File

```bash
./main examples/factorial.cvm
```

---

## Debug Mode

Shows:

- Generated AST
- Bytecode Instructions
- VM Execution Trace

Run:

```bash
./main examples/factorial.cvm --debug
```

---

# Example Programs

## Factorial

```c
let n = input();

let result = 1;

while (n > 1)
{
    result = result * n;
    n = n - 1;
}

print(result);
```

---

## Arithmetic

```c
let a = input();
let b = input();

print(a+b);
print(a-b);
print(a*b);
print(a/b);
```

---

## Boolean Checks

```c
let x = input();

print(x > 0);
print(x < 0);
print(x == 0);
```

---

## Nested if / else

```c
let x = input();

if (x > 0)
{
    print(1);
}
else
{
    if (x < 0)
    {
        print(-1);
    }
    else
    {
        print(0);
    }
}
```

---

# Project Structure

```text
CVM++/

├── ast/
│   ├── expr.h
│   ├── stmt.h
│   ├── ast_printer.h
│   └── ast_printer.cpp
│
├── lexer/
│   ├── lexer.h
│   ├── lexer.cpp
│   └── token.cpp
│
├── parser/
│   ├── parser.h
│   └── parser.cpp
│
├── compiler/
│   ├── compiler.h
│   └── compiler.cpp
│
├── vm/
│   ├── vm.h
│   ├── vm.cpp
│   ├── instruction.h
│   └── instruction.cpp
│
├── examples/
├── tests/
├── docs/
│
├── grammar.txt
├── design_notes.txt
├── main.cpp
├── Makefile
└── README.md
```

---

# Tech Stack

Language:

- C++

Core Concepts:

- Lexical Analysis
- Recursive Descent Parsing
- AST Construction
- Bytecode Compilation
- Stack Machine Architecture
- Virtual Machine Design
- Runtime Execution
- Memory Handling

---

# Contributors

### Vishwak

Primary Contributions:

- Lexer
- Recursive Descent Parser
- AST Design
- Grammar Design
- AST Debug Printer
- Syntax Diagnostics

Secondary:

- REPL Integration
- Frontend Testing

---

### Srikar

Primary Contributions:

- Opcode ISA
- Bytecode Compiler
- Virtual Machine
- Runtime Execution
- Variable Memory System
- Control Flow Runtime

Secondary:

- Bytecode Debugging
- Integration

---

# Future Improvements

- Functions
- Strings
- Arrays
- Logical Operators (&&, ||)
- Function Calls
- Return Statements
- Garbage Collection
- Optimized Dispatch Loop
- JIT Compilation

---

Built as part of **CVM++ — Stack-Based Virtual Machine & Custom Compiler Project**