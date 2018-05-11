import sys

def get_char_limit(limit):
    try:
        castInt = int(limit)
    except ValueError:
        print('Please enter an integer argument.')
        sys.exit()

    last_char = sys.argv[1][-1]

    print(sys.argv[1], end='')

    for i in range(castInt - len(sys.argv[1])):
        print(last_char, end='')

    print()

def no_char_limit():
    total_remaining_chars = 1000 - len(sys.argv[1])
    last_char = sys.argv[1][-1]

    print(sys.argv[1], end='')

    for i in range(total_remaining_chars):
        print(last_char, end='')

    print()

def main():
    if (len(sys.argv) < 2):
        print("Please include one or more arguments and re-run the script.")
        sys.exit()

    if (len(sys.argv) < 3):
        print("No character limit specified, defaulting on 1000 character limit.")
        no_char_limit()
    else:
        print("Character limt of : ", sys.argv[2], " specified, printing...")
        get_char_limit(sys.argv[2])


if __name__ == '__main__':
    main()
