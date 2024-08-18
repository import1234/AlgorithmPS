def f(s):
    op=[]
    num=[]
    t=''
    p=[] #parentheses, 괄호
    for x in s:
        #괄호에 대한 코드
        if t!='':
            if p: #괄호 수집중
                t+=x
                if x==')':p.pop()
                if x=='(':p.append(0)
            if p==[]: #괄호 닫히면 넘기기
                num.append(f(t[1:-1]))
                if op and op[-1]in['*','/']: #곱연산 우선
                    b=num.pop()
                    a=num.pop()
                    num.append(a+b+op.pop())
                t=''
        elif x=='(':t+='(';p.append(1)
        #괄호에 대한 코드 끝

        elif x in ['*','/','+','-']:op.append(x)#연산자 append
        else:
            num.append(x)
            if op and op[-1]in['*','/']: #곱연산 우선
                b=num.pop()
                a=num.pop()
                num.append(a+b+op.pop())
    
    #곱연산 후 나머지 덧셈 뺄셈 연산
    op.reverse()
    num.reverse()
    while op:
        num.append(num.pop()+num.pop()+op.pop())
    return ''.join(num)

print(f(input()))