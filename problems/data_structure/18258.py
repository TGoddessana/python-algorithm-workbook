import sys
from collections import deque

readline = sys.stdin.readline

queue = deque()

for _ in range(int(readline())):
    command = readline()

    if command.startswith("push"):
        element = command.split()[1]
        queue.appendleft(element)

    elif command.startswith("pop"):
        try:
            print(queue.pop())
        except IndexError:
            print(-1)

    elif command.startswith("size"):
        print(len(queue))

    elif command.startswith("empty"):
        print(1 if len(queue) == 0 else 0)

    elif command.startswith("front"):
        try:
            print(queue[-1])
        except IndexError:
            print(-1)

    elif command.startswith("back"):
        try:
            print(queue[0])
        except IndexError:
            print(-1)
