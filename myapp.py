import sys
import random

def CalculateExpress(num):
    symbols = ['+', '-', '*', '/']
    expression = [str(random.randint(0, 10))]
    for i in range(0, 3):
        expression.append(str(random.sample(symbols, 1)[0]))
        choice = random.randint(0, 2)
        if choice is 0:
            expression.append(str(random.randint(0, 10)))
        elif choice is 1:
            nm = random.randint(1, 9)
            dm = random.randint(nm, 10)
            expression_detail = ['[', str(nm), '/', str(dm), ']']
            expression.append(''.join(expression_detail))
        else:
            nm = random.randint(1, 9)
            dm = random.randint(nm, 10)
            nd = random.randint(1, 9)
            expression_detail = ['[', str(nd), '\'', str(nm), '/', str(dm), ']']
            expression.append(''.join(expression_detail))
    if random.randint(0, 1) is 1:
        expression.append('')
        left_l = random.randint(0, 3)
        right_l = random.randint(left_l, 3)
        expression.insert(left_l * 2, '(')
        expression.insert(right_l * 2 + 2, ')')
    return  ''.join(expression)

def RemoveRe(calculate):
    # for p in calculate:
    #     if p =='(' :
    #         for q in calculate[calculate.index(p):]:
    #             if q == ')':
    #                 RemoveRe(calculate[calculate.index(p)+1:calculate.index(q)])
    #     if p =='[' :
    #         for q in calculate[calculate.index(p):]:
    #             if q == ']':
    #                 RemoveRe(calculate[calculate.index(p)+1:calculate.index(q)])
    #     if p == '+':
    return True

def CalculateNum(num):
    result = []
    while len(result) < 10:
        a = CalculateExpress(int(num))
        if RemoveRe(list(a)):
            result.append(a)
    print(result)

def CalculateRange(num):
    print(CalculateExpress(int(num)))

def CalculateCheck(cmd_a,file_a,cmd_c,file_c):
    print(cmd_a,file_a,cmd_c,file_c)


def main():
    if sys.argv[1] =='-n':
        CalculateNum(sys.argv[2])
    elif sys.argv[1] =='-r':
        CalculateRange(sys.argv[2])
    elif sys.argv[1] =='-e':
        CalculateCheck(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("输入格式有误")
    sys.exit(1)
if __name__=="__main__":
    main()