f_number = input("Which sample file: ")
f_test = open(f'./src/sample{f_number}_tests.txt')
f_sol = open(f'./src/sample{f_number}_solutions.txt')

test_list = f_test.read().splitlines()
solution_list = f_sol.read().splitlines()

def check(output, index):
    if output == solution_list[index]:
        print(f"{index + 1:02d} \u001b[32mCorrect.\u001b[37m")
    else:
        print(f"{index + 1:02d} \u001b[31mIncorrect. \u001b[37mOutput: {output}. Expected: {solution_list[index]}")

for x in range(len(test_list)):
    str = test_list[x]
    try:
        str_ipv4 = str.split(".")
        str_ipv6 = str.split(":")

        if len(str_ipv4) == 4:
            if all(0 <= int(n) <= 255 for n in str_ipv4):
                check("IPv4", x)
            else: 
                check("Neither", x)

        elif len(str_ipv6) == 8:
            if all(0 <= int(n, 16) <= 65535 for n in str_ipv6):
                check("IPv6", x)
            else:
                check("Neither", x)
        else:
            check("Neither", x)

    except ValueError:
        check("Neither", x)