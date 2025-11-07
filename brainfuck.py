import os

data_pointer = {}
current_cell_index = 0

def run_interpreter(file_path):
    with open(file_path, "r") as my_handle:
       jump_map = {}

       file_str = my_handle.read()
       if validation_brainfuck_file(file_str):
        jump_map = build_jump_map(file_str)
        instruction_pointer = 0

        while instruction_pointer < len(file_str):
            command = file_str[instruction_pointer]
            instruction_pointer = handle_commad(command, jump_map, instruction_pointer)


def build_jump_map(file_str):
    jump_map = {}
    open_braket_stack = []

    for ip, command in enumerate(file_str):
        if command == '[':
            open_braket_stack.append(ip)
        elif command == ']':
            if not open_braket_stack:
                raise ValueError(f"ERROR: Unmatched closing ']' at index {ip}")
            open_ip = open_braket_stack.pop()
            jump_map[open_ip] = ip
            jump_map[ip] = open_ip

    return jump_map


# make function it's take one parameter (brainfuck_comand) and make action
def handle_commad(command, jump_map, instruction_pointer):
    global current_cell_index, data_pointer

    next_ip = instruction_pointer + 1

    if command == '>':
        current_cell_index += 1

    elif command == '<':
        current_cell_index -= 1

    elif command == '+':
        temp_value = data_pointer.get(current_cell_index, 0)
        temp_value += 1
        data_pointer.update({ current_cell_index : temp_value})

    elif command == '-':
        temp_value = data_pointer.get(current_cell_index, 0)
        temp_value -= 1
        data_pointer.update({current_cell_index : temp_value})

    elif command == '.':
        print(chr(data_pointer[current_cell_index]))

    elif command == ',':
        pass

    elif command == '[':
        if data_pointer.get(current_cell_index) == 0:
            next_ip = jump_map[instruction_pointer]

    elif command == ']':
        if data_pointer.get(current_cell_index) != 0:
            next_ip = jump_map[instruction_pointer]

    return next_ip

def validation_brainfuck_file(file_string):

    # Check file path exist
    if not os.path.exists(final_file_path):
        print(f"ERROR: The file {final_file_path} does not exist, please enter the name of an existing file.")      
        return False
    
    # Check if there not allowed characters
    valid_comands = ['>', '<', '+', '-', '.', '.', '[', ']']

    for char in file_string:
        if char not in valid_comands:
            print(f"ERROR: The file {final_file_path} contains the character '{char}' which is not acceptable for the Brainfuck language")
            return False
        
    return True

def ask_file_name():
    while True:
        file_name = input("Enter file name (ex, hello or hello.bf): ")

        # Display brainfuck commands.
        if file_name.lower() == "help":
            print("\n\nBrainfuck is an esoteric programming language with only 8 commands:\n" \
                  ">   moves the memory pointer one cell to the right\n" \
                  "<   moves the memory pointer one cell to the left\n" \
                  "+   increments the value in the current cell\n" \
                  "-   decrements the value in the current cell\n" \
                  ".   outputs the ASCII character corresponding to the value in the current cell\n" \
                  ",   reads one character of input and stores its ASCII value in the current cell\n" \
                  "[   if the value in the current cell is 0, jumps forward to the command after the matching ']'\n" \
                  "]   if the value in the current cell is not 0, jumps back to the command after the matching '['\n\n")
            continue

        final_file_path = file_name 

        if not os.path.splitext(file_name)[1]:
            print(f"File name '{file_name}' has no extension.")
            print("which type file are you running?")
            print("1: Brainfuck (.bf)")
            print("2. Text (.txt)")
    
            while True:
                choice_file_type = input("Enter 1 or 2 ").strip()
    
                if choice_file_type == '1':
                    final_file_path = f"{file_name}.bf"
                    break
                elif choice_file_type == '2':
                    final_file_path = f"{file_name}.txt"
                    break
                else:
                    print("Invalid choice!")                       


        # Check file existence


        return final_file_path


if __name__ == "__main__":
    print("Hi, this is interpeter for the brainfuck lenguage. ")
    final_file_path = ask_file_name()

    print("\n--- Starting Brainfuck Interperter ---")
    run_interpreter(final_file_path)
    print("\n--- Execution finished ---")
