import sys


def main():
    # sys.argv[0] is the script name
    arguments = sys.argv

    print("Number of arguments:", len(arguments))
    print("Arguments list:", arguments)

    actual_arguments = arguments[1:]
    print("Actual arguments (excluding script name):", actual_arguments)


if __name__ == "__main__":
    main()
