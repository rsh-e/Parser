## These are the 15 registers used as memory for the computer. The values are empty ("None") when the program begins
from re import L
import re

from pyparsing import line


registers = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
bin_number = ''

## This function converts a number from denary to binary for the LSL and RSL operations
def int_to_bin(number):
    return str(bin(number).replace('0b', ''))

## This function converts a number from binary to denary for the LSL and RSL operations
def bin_to_int(number):
    return int('0b' + str(number), 2)

## This is the interface where you can write the program
def write_code():
    # The program is written as line and each line is added to an array. That array is the lines array
    lines = []
    line = ""
    line_count = 1

    # You can write the program until you type in the Halt command where the code writing stops
    while line != "HALT":
        line = input(str(line_count) + "  ")
        lines.append(line)
        line_count = line_count + 1

    print()
    return lines


## This function splits each word of the line into a list which can be processed
def get_line(lst):
    return lst.split(" ")



def mem_values_true(line_to_exec):
    true_count = 0
    try:
        address_to_store = int(line_to_exec[1][1:])
        value_to_store = int(line_to_exec[2][1:])
        return True
    except:
        print("The registers expect only integers to be operated on in command", *line_to_exec)
        return False

def com_values_true(line_to_exec):
    try:
        # This variable specifies the address where the variable is stored
        address_to_store = int(line_to_exec[1][1:])
        # The variable specifies the address of the first operand
        value_to_operate1 = int(line_to_exec[2][1:])
        # This value specifies the address of the second operand(for #)
        value_to_operate2 = int(line_to_exec[3][1:])
        # This value specifies the address of the second operand(for registers)
        value_to_operate2_r = int(line_to_exec[3][1:])

        if registers[value_to_operate1] == None or registers[value_to_operate2_r] == None:
            print("Memory locations to operate on are empty in command", *line_to_exec)
            return False
        else:
            return True
    except:
        return False
    

## This function explicitly checks the command and checks whether it's valid
def explicit_mem_check(line_to_exec):
    # It checks to whether the first register and the second register/number is valid. If it is returns true, else it returns false
    if line_to_exec[1][0] == "R":
        if line_to_exec[2][0] == "R" or "#":
            try:
                if line_to_exec[3][0] == ";" or "\n":
                    return True
                else:
                    return False
            except:
                return True
        else:
            return False
    else:
        return False


## This function explicitly checks the command and checks whether it's valid
def explicit_com_check(line_to_exec):
    # It checks whether the registers and the numbers are valid. If it is, true is returned. Else, false is returned.
    if line_to_exec[1][0] == "R" and line_to_exec[2][0] == "R":
        if line_to_exec[3][0] == "R" or "#":
            try:
                if line_to_exec[4][0] == ";" or "\n":
                    return True
                else:
                    print("Expected size for computation operation is 3 in command", *line_to_exec)
                    return False
            except:
                return True
        else:
            print("Fourth part of the command must be a register or number in command", *line_to_exec)
            return False
    else:
        print("Second and third part of the command must be a register", *line_to_exec)
        return False


## This function checks whether the compare and branch statements are valid
def explicit_cmp_check(line_to_exec):
    cmp_statements = ["LT", "GT", "EQ", "NE", "LTE", "GTE"]
    if line_to_exec[1] in cmp_statements:
        if line_to_exec[2][0] == "R" and line_to_exec[3][0] == "R" or "#":
            if cmp_true(line_to_exec):
                ## The [:-1] and [:-2] are to be removed once i remove the '\n'
                label = line_to_exec[4]
                label_count = 0
                for i in range(len(commands)):
                    command = commands[i]
                    if label in command:
                        label_count = label_count + 1
                        if label_count == 2:
                            command_number = i+1
                            branch = [commands[command_number]]
                            ## THE BIGGEST CHANGE IS HERE ##
                            while branch != "HALT":
                                branch = [commands[command_number]]
                                valid_command = compile(branch)
                                if valid_command == False:
                                    break
                                elif command_number == len(commands) - 1:
                                    break
                                else:
                                    command_number = command_number + 1
                            try:
                                if line_to_exec[5] == "HALT":
                                    #The program stops execution
                                    return False
                                else:
                                    pass
                            except:
                                pass
        else:
            print("The third and fourth part must be a register in command", *line_to_exec)
            return False
    else:
        print("The second part of the must be a compare operation in command", *line_to_exec)
        return False

def cmp_true(line_to_exec):
    r1 = registers[int(line_to_exec[2][1:])]
    r2 = registers[int(line_to_exec[3][1:])]
    # Add a variable incase numbers are being used to compare
    if line_to_exec[1] == "LT":
        return r1 < r2
    elif line_to_exec[1] == "GT":
        return r1 > r2
    elif line_to_exec[1] == "EQ":
        return r1 == r2
    elif line_to_exec[1] == "NE":
        return r1 != r2
    elif line_to_exec[1] == "LTE":
        return r1 <= r2
    elif line_to_exec[1] == "GTE":
        return r1 >= r2
    else:
        return False    

## This function executes commands like LDR, STR, MOV, CPY (worry about LDR later)
def exec_memory_ops(line_to_exec):
    try:
        address_to_store = int(line_to_exec[1][1:])
        value_to_store = int(line_to_exec[2][1:])
    except:
        return False
    # To store a value in a register. The register is assigned the value of the variable
    if line_to_exec[0] == "STR":
        registers[address_to_store] = value_to_store
    #
    elif line_to_exec[0] == "MOV":
        registers[address_to_store] = registers[value_to_store]
        registers[value_to_store] = None
    #
    elif line_to_exec[0] == "CPY":
        registers[address_to_store] = registers[value_to_store]
    else:
        return False


# This function executes commands like ADD, SUB, AND, ORR, EOR, LSL, LSR
def exec_comp_ops(line_to_exec):
    # This variable specifies the address where the variable is stored
    address_to_store = int(line_to_exec[1][1:])
    # The variable specifies the address of the first operand
    value_to_operate1 = int(line_to_exec[2][1:])
    # This value specifies the address of the second operand(for #)
    value_to_operate2 = int(line_to_exec[3][1:])
    # This value specifies the address of the second operand(for registers)
    value_to_operate2_r = int(line_to_exec[3][1:])

    # The program then performs the operations
    if line_to_exec[0] == "ADD":
        if line_to_exec[3][0] == "R":
            registers[address_to_store] = registers[value_to_operate1] + registers[value_to_operate2_r]
        else:
            registers[address_to_store] = registers[value_to_operate1] + value_to_operate2

    elif line_to_exec[0] == "SUB":
        if line_to_exec[3][0] == "R":
            registers[address_to_store] = registers[value_to_operate1] - registers[value_to_operate2_r]
        else:
            registers[address_to_store] = registers[value_to_operate1] - value_to_operate2

    elif line_to_exec[0] == "AND":
        if line_to_exec[3][0] == "R":
            registers[address_to_store] = registers[value_to_operate1] and registers[value_to_operate2_r]
        else:
            registers[address_to_store] = registers[value_to_operate1] and value_to_operate2

    elif line_to_exec[0] == "ORR":
        if line_to_exec[3][0] == "R":
            registers[address_to_store] = registers[value_to_operate1] or registers[value_to_operate2_r]
        else:
            registers[address_to_store] = registers[value_to_operate1] or value_to_operate2

    elif line_to_exec[0] == "EOR":
        if line_to_exec[3][0] == "R":
            registers[address_to_store] = registers[value_to_operate1] ^ registers[value_to_operate2_r]
        else:
            registers[address_to_store] = registers[value_to_operate1] ^ value_to_operate2

    elif line_to_exec[0] == "LSL":
        add_zeros = ''
        def_bin = int_to_bin(registers[value_to_operate1])
        shift = value_to_operate2
        bit_size = len(bin(shift))
        if line_to_exec[3][0] == "#":
            # creating the zeros to be added at the end
            for i in range(shift):
                add_zeros = add_zeros + "0"
            # adding the zeros to the end of the binary number
            zeroed_bin = def_bin + add_zeros
            # shifting the binary
            shifted_bin = zeroed_bin[shift:]
            # putting the shifted number
            registers[address_to_store] = bin_to_int(shifted_bin)

    elif line_to_exec[0] == "LSR":
        add_zeros = ''
        def_bin = int_to_bin(registers[value_to_operate1])
        shift = value_to_operate2
        bit_size = len(bin(shift))
        if line_to_exec[3][0] == "#":
            # creating the zeros to be added at the end
            for i in range(shift):
                add_zeros = add_zeros + "0"
            # adding the zeros to the end of the binary number
            zeroed_bin = add_zeros + def_bin
            # shifting the binary
            shifted_bin = zeroed_bin[0:len(zeroed_bin)-shift]
            # putting the shifted number
            registers[address_to_store] = bin_to_int(shifted_bin)


# This function checks whether the formatting and commands are valid
def syntax_check(line_to_exec):
    memory_ops = ["STR", "MOV", "CPY"]
    comp_ops = ["ADD", "SUB", "AND", "ORR", "EOR", "LSL", "LSR"]

    # This checks if it's a memory operation. If it is, the program then executes it.
    if line_to_exec[0] in memory_ops:
        if len(line_to_exec) >= 3:
            if explicit_mem_check(line_to_exec) and mem_values_true(line_to_exec): 
                exec_memory_ops(line_to_exec)
            else:
                return False
        else:
            print("\nInvalid command size for memory operation:", *line_to_exec, "\nExpected size is 3")
            return False
    # This checks if it's a computational operation. If it is, the program then executes it.
    elif line_to_exec[0] in comp_ops:
        if len(line_to_exec) >= 4:
            if explicit_com_check(line_to_exec) and com_values_true(line_to_exec): 
                   exec_comp_ops(line_to_exec) ## Last seen here
            else:
                return False
        else:
            print("\nInvalid command size for memory operation:", *line_to_exec, "\nExpected size is 4")
            return False
    # This checks if it's compare and branch statement. If it is, the program then executes it.
    elif line_to_exec[0] == "CMP":
        if len(line_to_exec) >= 5:
            explicit_cmp_check(line_to_exec)
            if explicit_cmp_check(line_to_exec) == False:
                return False
        else:
            print("\nInvalid command size for memory operation:", *line_to_exec, "\nExpected size is 5")
            return False



# This if the function where the code is compiles and executed
def compile(commands):  
    valid_commands = ["STR", "ADD", "SUB", "MOV", "CMP", "B", "AND", "ORR", "EOR", "MVN", "LSL", "LSR", "CPY", "HALT"]
    for command in commands:
        line_to_exec = get_line(command)
        if line_to_exec[0] in valid_commands:
            if line_to_exec[0] == "\n":
                print("Program executed without errors")
            no_error = syntax_check(line_to_exec)
            if no_error == False:
                return False
                break
            ## So there's an issue below about undeclared labels, run an fix it later.
        elif len(line_to_exec) == 1:
            print("Label", line_to_exec, "is undeclared previously")
        else:
            print("Invalid command", line_to_exec[0], "\nError found with line:", command)
            return False

## The commands needed to be executed are first loaded or written to this function
def get_commands():
    print("Welcome to the Assembly Compiler!")
    # This variable is toggled to ensure that the program doesn't end on an invalid input
    temp = False
    # The program first asks whether we want to load or write a program
    while temp is False:
        load_write = input("Load a file to compile or write a program? (l/w) : ")
        if load_write == "l" or load_write == "w":
            temp = True
        else:
            print("Invalid Command. Try again.")

    # This section then tries to open the program file and if it can't it asks for you to input a file again
    if load_write == "l":
        commands = []
        while temp is True:
            src_code = input("Input the name of the file you want to compile (No extension is nessecary): ")
            try:
                src_code = src_code + ".txt"
                with open(src_code) as path:
                    commands = [ command.strip() for command in path ]
                    temp = False
            except:
                print("No such file exists. Please try again.")
    # Otherwise, the commands are then loaded from the program
    elif load_write == "w":
        commands = write_code()

    # the commands to be executed are then returned
    return commands

## This is where the components all meet up and make the program run
if __name__ == "__main__":
    # The commands needed to be executed are stored in the get_commands variable
    commands = get_commands()
    # The commands then get compiled and executed
    compile(commands)
    # We can then see the memory from the program
    print("\nMemory: ", registers)


## Some errors repeat twice but everything else works fine

