inputs = input().strip().split(' ')
stack = list()
out = list()
for i in inputs:
    if(i == '+'):
        y = int(stack.pop())
        x = int(stack.pop())
        z = x + y
        stack.append(z)
    elif(i=='-'):
        y = int(stack.pop())
        x = int(stack.pop())
        z = x - y
        stack.append(z)
    elif(i=='*'):
        y = int(stack.pop())
        x = int(stack.pop())
        z = x * y
        stack.append(z)
    else:
        stack.append(i)
print(stack[-1])
