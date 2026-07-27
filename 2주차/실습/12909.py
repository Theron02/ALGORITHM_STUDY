def solution(s):
    answer = True
    stk = []
    for i in range(len(s)):
        if s[i] == '(':
            stk.append(s[i])
        else:
            if len(stk) == 0:
                answer = False
                break
            else:
                stk.pop()
    if len(stk) != 0:
        answer = False
    return answer