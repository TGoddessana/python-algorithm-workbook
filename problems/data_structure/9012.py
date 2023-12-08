import sys

try_count = int(sys.stdin.readline().rstrip())

for _ in range(try_count):
    brackets = sys.stdin.readline().rstrip()

    stack = []

    for bracket in brackets:
        if stack:
            if bracket == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(bracket)
        else:
            stack.append(bracket)

    print("YES" if not stack else "NO")
