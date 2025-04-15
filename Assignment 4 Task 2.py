def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')


def read_file(filename):
    with open(filename, 'r') as file:
        print("\nFinal content of the file:")
        for line in file:
            print(line.strip())


def main():
    filename = "output.txt"

    while True:
        user_input = input("Enter text to write to the file (or type 'exit' to stop): ")
        if user_input.lower() == 'exit':
            break
        write_to_file(filename, user_input)


    read_file(filename)


if __name__ == "__main__":
    main()