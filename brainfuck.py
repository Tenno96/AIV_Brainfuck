BRAINFUCK_FILE_PATH = "brainfuck_file.txt"

data_pointer = {}
current_cell_index = 0

def run_interpreter():
    with open(BRAINFUCK_FILE_PATH, "r") as my_handle:
       jump_map = {}

       file_str = my_handle.read()
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

if __name__ == "__main__":
    run_interpreter()