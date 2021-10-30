def rp(string, x, y, ans, flag):
    stack = []
    for char in string:
        if char == 'p':
            if stack and stack[-1] == 'r':
                ans[0] += y
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
    if flag:
        pr("".join(stack), x, y, ans, False)


def pr(string, x, y, ans, flag):
    stack = []
    for char in string:
        if char == 'r':
            if stack and stack[-1] == 'p':
                ans[0] += x  
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
    if flag:
        rp("".join(stack), x, y, ans, False)
    
def solve():

    string = input()
    x, y = map(int, input().split())
    ans = [0]

    if x  > y:
        pr(string, x, y, ans, True)
    else:
        rp(string, x, y, ans, True)
    print(ans[0])
        

for _ in range(int(input())):
    solve()
