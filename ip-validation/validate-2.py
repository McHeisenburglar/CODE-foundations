for x in range(1, int(input("How many tests? ")) + 1):
    str = input("Check: ")
    try:
        # If it contains the correct amount of packets for IPv4, and
        # each packet is in the correct range, check for correct.
        if len(str.split(".")) == 4 and all(0 <= int(n) <= 255 for n in str.split(".")):
            check("IPv4", x)

        # Same for IPv6
        elif len(str.split(":")) == 8 and all(0 <= int(n, 16) <= 65535 for n in str.split(":")):
            check("IPv6", x)

        else:
            print("Neither")

    except ValueError:
        print("Neither")