# Parser

A programming interface and parser which an execute AQA style Assembly code

# How it works

When you run the program, you can either load a file or write a program in the interface which will be executed.
If you load the file, the file must be in the same folder as the main.py otherwise it won't run. If you are writing the program in the interface, then you will have to type 'HALT' in order to stop the interface. Execution will begin after that.
You are alotted 15 memory locations where you can perform a variety of operations as mentioned in the documentation below. The memory locations exist from R0 to R14.

# Documentation

## Memory Operations

Here are the operations you can perform to the memory locations:

### 1) STR 
   This stores a number in a memory location. 
   Syntax: ```STR Rn  #m```
   Here, 'n' is a memory location (0 to 14) and 'm' is any number. In this case, the number 'm' is stored in the memory location 'n' 
### 2) MOV
  This moves the value from one memory location to another.
  Syntax:```MOV Rn Rm```
  Here, 'n' is a memory location (0 to 14) and 'm' is a memory location (0 to 14). In this case, the value in location 'm' is moved to location 'n'. The value no longer  exists in location, 'm'.
### 3) CPY
  This moves the value from one memory location to another.
  Syntax: ```CPY Rn Rm```
  Here, 'n' is a memory location (0 to 14) and 'm' is a memory location (0 to 14). In this case, the value in location 'm' is copied to location 'n'. The value no still exists in location, 'm'.
  
## Arithmetic Operations
Here are the operations you can perform to the values stored in memory:

### 1) ADD
   This adds the values of 2 memory locations and stores them in another memory location (the same location may also be used)
    Syntax: ```ADD Rn Rm Rl```
    Here, the values stored in Rm and Rl are added and stored in Rn
### 2) SUB
   This subtracts the values of 2 memory locations and stores them in another memory location (the same location may also be used)
    Syntax: ```SUB Rn Rm Rl```
    Here, the values stored in Rm and Rl are subtracted and stored in Rn
### 3) AND
   This takes the values of 2 memory locations and performs the logical operation 'AND' on them and then stores the result in another memory location (the same location may also be used)
    Syntax: ```AND Rn Rm Rl```
    Here, the 'AND' operation is performed on Rm and Rl and the result is stored in Rn
### 4) ORR
   This takes the values of 2 memory locations and performs the logical operation 'OR' on them and then stores the result in another memory location (the same location may also be used)
    Syntax: ```ORR Rn Rm Rl```
    Here, the '0RR' operation is performed on Rm and Rl and the result is stored in Rn
### 5) EOR
   This takes the values of 2 memory locations and performs the logical operation 'XOR' on them and then stores the result in another memory location (the same location may also be used)
    Syntax: ```EOR Rn Rm Rl```
    Here, the 'XOR' operation is performed on Rm and Rl and the result is stored in Rn
### 5) LSL
 This takes a value stored in a memory location and performs a bitwise shift to the left and then stores the result in another memory location (the same location may also be used)
    Syntax: ```LSL Rn Rm #l```
    Here, the the logical shift to the left is performed to the value stored in Rm by 'l' number of bits, and store the result in Rn
### 6) LSR
  This takes a value stored in a memory location and performs a bitwise shift to the left and then stores the result in another memory location (the same location may also be used)
    Syntax: ```LSR Rn Rm #l```
    Here, the the logical shift to the left is performed to the value stored in Rm by 'l' number of bits, and store the result in Rn
 
 ## Compare and Branching
 This takes 2 values stored in memory and compares them, if the comparison is true, the program branches to another location in the code given, and runs the code from that location.
 
 Syntax:  ```CMP RO Rn Rm LABEL```
 Here, RO refers to the relational operations less than (```LT```), greater than (```GT```), equal to (```EQ```), not equal to (```NE```), less than or equal to (```LTE```), greater than or equal to (```GTE```). The values in Rn and Rm are compared in the order they are presented in. If the comparison is true, the program branches to a label which is further down the program and executes the code from thereon. The ```LABEL``` must exist after the CMP statement and not before.
