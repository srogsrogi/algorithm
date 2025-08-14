    def push(stack, char):
        stack.append(char)

    def pop(stack):
        stack.pop()

    stack_1 = []

    push(stack_1, 'A')
    push(stack_1, 'B')
    push(stack_1, 'C')

    print(stack_1)

    pop(stack_1)
    pop(stack_1)
    pop(stack_1)

    print(stack_1)
