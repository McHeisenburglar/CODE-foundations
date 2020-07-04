for x in range(1, int(input("How many tests? ")) + 1):
    str = input("Check: ")
    try:
        str_ipv4 = str.split(".")
        str_ipv6 = str.split(":")

        if len(str_ipv4) == 4 and all(0 <= int(n) <= 255 for n in str_ipv4):
            print("IPv4")

        elif len(str_ipv6) == 8 and all(0 <= int(n, 16) <= 65535 for n in str_ipv6):
            print("IPv6")

        else:
            print("Neither")

    except ValueError:
        print("Neither")