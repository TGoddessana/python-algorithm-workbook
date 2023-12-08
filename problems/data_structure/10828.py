import sys

command_count = int(sys.stdin.readline())

stack = []

for _ in range(command_count):
    command = sys.stdin.readline()

    if command.startswith("push"):
        stack.append(int(command.split()[1]))

    elif command.startswith("pop"):
        try:
            print(stack.pop())
        except IndexError:
            print(-1)

    elif command.startswith("size"):
        print(len(stack))

    elif command.startswith("empty"):
        print(1 if len(stack) == 0 else 0)

    elif command.startswith("top"):
        try:
            print(stack[-1])
        except IndexError:
            print(-1)
