inputs = list(input())
stack = []
tmp_stack = []
L = []
tmp_total = 0
counter = 0
upper = 0
for i in inputs:
    print(stack)
    if(i == '\\'):
        stack.append(i)
    elif(i=='/'):
        if(len(stack)!=0):
            stack.pop()
            counter += 1
            tmp_total +=  counter * 2 - 1 + upper
            print(tmp_total)
            if(len(stack) == 0):
                L.append(tmp_total)
                counter = 0
                upper = 0
                tmp_total = 0
    else:
        upper += 1
print(' '.join([str(i) for i in L]))
