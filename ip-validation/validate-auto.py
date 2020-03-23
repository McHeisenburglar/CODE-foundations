f_number = input("Which file: ")
f_test = open(f'./src/sample{f_number}_tests.txt')
f_sol = open(f"./src/sample{f_number}_solutions.txt")

test_list = f_test.read().splitlines()
solution_list = f_sol.read().splitlines()

for x in range(len(test_list)):
    print(f"index: {x}")
    str = test_list[x]
    try:
        str_ipv4 = str.split(".")
        str_ipv6 = str.split(":")

        if len(str_ipv4) == 4:
            if all(0 <= int(n) <= 255 for n in str_ipv4):
                if solution_list[x] == 'IPv4':
                    print(f"Correct. (line {x+1})")
                else: 
                    print(f"Incorrect. (line {x+1}).\nYour answer: IPv4. Line {x+1} of solution: {solution_list[x]}")
            else: 
                print(f"Incorrect. (line {x+1}).\nYour answer: IPv4. Line {x+1} of solution: {solution_list[x]}")

        elif len(str_ipv6) == 8:
            if all(0 <= int(n, 16) <= 65535 for n in str_ipv6):
                if solution_list[x] == 'IPv6':
                    print(f"Correct. (line {x+1})")
                else: 
                    print(f"Incorrect. (line {x+1})")
        else:
            if solution_list[x] == 'Neither':
                print(f"Correct. (line {x+1})")
            else:
                print(f"Incorrect. (line {x+1})")

    except ValueError:
        if solution_list[x] == 'Neither':
            print(f"Correct. (line {x+1})")
        else:
            print(f"Incorrect. Your output: 'Neither'. Correct: {solution_list[x]}")