def print_ascii_codes(phrase):
    for char in phrase:
        print(f"{char} = {ord(char)}")


def main():
    while True:
        string = input("Enter the phrase: ")
        if string == "":
            break
        print_ascii_codes(string)


if __name__ == "__main__":
    main()
