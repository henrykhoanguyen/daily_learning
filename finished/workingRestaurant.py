stack = [0, 0]

while 1:
    num = int(input())
    if num == 0:
        break
    action = []
    while num > 0:
        action.append(input().split())
        num -= 1

    for act, num in action:
        # print(act,num)
        n = int(num)
        if act == "DROP":
            stack[0] += n
            print("DROP 1", n)
        else:
            from_one = min(stack[1], n)
            if from_one != 0:
                n -= from_one
                stack[1] -= from_one
                print("TAKE 2", from_one)
            if n != 0:
                print("MOVE 1->2", stack[0])
                stack[1] = stack[0] - n
                stack[0] = 0
                print("TAKE 2", n)
