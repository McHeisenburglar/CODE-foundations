# Ask which file to check
f_number = input("Which sample file: ")

# Open the specifies files
f_test = open(f'./src/sample{f_number}_tests.txt')
f_sol = open(f'./src/sample{f_number}_solutions.txt')

# Create a list of... 
test_list = f_test.read().splitlines() # all the test inputs
solution_list = f_sol.read().splitlines() # all the correct (expected) outputs

# Check if my output matches the correct output.
def check(output, index):
    if output == solution_list[index]:
        print(f"{index + 1:02d} \u001b[32mCorrect.\u001b[37m")
    else:
        # If it doesn't match, give me line number, and the two outputs that don't match
        print(f"{index + 1:02d} \u001b[31mIncorrect. \u001b[37mOutput: {output}. Expected: {solution_list[index]}")

# For however many lines there are in the files
for x in range(len(test_list)):
    # Get string from line
    str = test_list[x]
    try:
        str_ipv4 = str.split(".") # Create IPv4 test string
        str_ipv6 = str.split(":") # Create IPv6 test string

        # If it contains the correct amount of packets for IPv4, and
        # each packet is between the correct range, check for correct
        if len(str_ipv4) == 4:
            if all(0 <= int(n) <= 255 for n in str_ipv4):
                check("IPv4", x)
            else: 
                check("Neither", x)

        # Same for IPv6
        elif len(str_ipv6) == 8:
            if all(0 <= int(n, 16) <= 65535 for n in str_ipv6):
                check("IPv6", x)
            else:
                check("Neither", x)

        # If neither match, check Neither
        else:
            check("Neither", x)

    # If int() breaks down at any point in the code above,
    # it means the string is not a proper IP address anyway,
    # so I can safely return "Neither"
    except ValueError:
        check("Neither", x)