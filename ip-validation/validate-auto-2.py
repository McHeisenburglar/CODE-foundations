# Ask which file to check
f_number = input("Which sample file: ")

# Open the specifies files
f_test = open(f'./src/sample{f_number}_tests.txt')
f_sol = open(f'./src/sample{f_number}_solutions.txt')

# Create a list of... 
test_list = f_test.read().splitlines() # all the test inputs
solution_list = f_sol.read().splitlines() # all the correct (expected) outputs

# Close files
f_test.close()
f_sol.close()dfs

# Check if an output matches the correct answer.
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
        # If it contains the correct amount of packets for IPv4, and
        # each packet is in the correct range, check for correct.
        if len(str.split(".")) == 4 and all(0 <= int(n) <= 255 for n in str.split(".")):
            check("IPv4", x)

        # Same for IPv6
        elif len(str.split(":")) == 8 and all(0 <= int(n, 16) <= 65535 for n in str.split(":")):
            check("IPv6", x)

        # If neither match, check Neither
        else:
            check("Neither", x)

    # If int() breaks down at any point in the code above,
    # it means the string is not a proper IP address anyway,
    # so I can safely return "Neither"
    except ValueError:
        check("Neither", x)
