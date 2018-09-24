import sys
import random
import itertools
def CalculateExpress(num):
    symbols = ['+', '-', '*', '/']
    expression = [str(random.randint(1, num))]
    for i in range(0, 3):
        expression.append(str(random.sample(symbols, 1)[0]))
        choice = random.randint(0, 2)
        if choice is 0 :
            expression.append(str(random.randint(1, num)))
        elif choice is 1:
            nm = random.randint(1, num-1)
            dm = random.randint(nm, num)
            expression_detail = ['[', str(nm), '/', str(dm), ']']
            expression.append(expression_detail)
        else:
            nm = random.randint(1, num-1)
            dm = random.randint(nm, num)
            nd = random.randint(1, num-1)
            expression_detail = ['[', str(nd), '\'', str(nm), '/', str(dm), ']']
            expression.append(expression_detail)
    if random.randint(0, 1) is 1:
        expression.append('')
        left_l = random.randint(0, 3)
        right_l = random.randint(left_l, 3)
        expression.insert(left_l * 2, '(')
        expression.insert(right_l * 2 + 2, ')')
    return list(itertools.chain.from_iterable(expression))

data = [str(i) for i in range(1,100)]
cal = {"+":"1","-":"1","*":"2","/":"2","'":"2"}
cal1={"(":"0"}

def RemoveRe(calculate):
    result = []
    c=[]
    for item in calculate:
        if item =="'":
            item ="*"
        if item in data:
            result.append(item)
        elif not c and item in cal.keys():
            c.append(item)
            continue
        elif c and item in cal.keys():
            for x in range(c.__len__()):
                z=c[-1]
                temp=cal[z] if z in cal else cal1[z]
                if temp >= cal[item]:
                    result.append(c.pop())
                else:
                    c.append(item)
                    break
            if not c:
                c.append(item)
        elif item==")":
            for x in range(c.__len__()):
                if c[-1]=="(":
                    c.pop()
                    break
                else:
                    result.append(c.pop())
        elif item =="(":
            c.append(item)
    for x in range(c.__len__()):
        result.append(c.pop())
    return result

def caculate(expression):
    num=[]
    for i in expression:
        if i in data :
            num.append(i)
        else:
            num1=num.pop()
            num2=num.pop()
            try:
                num.append(str(eval("%s%s%s"%(num2,i,num1))))
            except:
                return "null"
    return round(float(num[0]),1)

def CalculateNum(num):
    result = []
    f1=open('a.txt','w')
    f2=open('answer.txt','w')
    i=1
    while i <= int(num):
        a = CalculateExpress(10)
        f1.write(str(i)+'.  '+''.join(a)+'\n')
        nbl = RemoveRe(a)
        answer=caculate(nbl)
        f2.write(str(answer)+'\n')
        result.append(''.join(a))
        i+=1
    f1.close()
    f2.close()

def CalculateRange(num):
    print(''.join(CalculateExpress(int(num))))

def CalculateCheck(file_a,file_c):
    f2=open(file_a,'r').readlines()
    f3=open(file_c,'r').readlines()
    wrong_list=[]
    right_list=[]
    print(len(f3))
    for i in range(0,len(f3)):
        if f2[i]!=f3[i]:
            wrong_list.append(i+1)
        else:
            right_list.append(i+1)
    print('总共答对'+str(len(right_list))+'题\n'+'正确的是:'+str(right_list)+'\n错误的是:'+str(wrong_list))



def main():
    if sys.argv[1] =='-n':
        CalculateNum(sys.argv[2])
    elif sys.argv[1] =='-r':
        CalculateRange(sys.argv[2])
    elif sys.argv[1] =='-e':
        CalculateCheck( sys.argv[2], sys.argv[3])
    else:
        print("输入格式有误")
    sys.exit(1)
if __name__=="__main__":
    main()