def operation(a, b, operator):
    try:
        if operator=='+':
            return a+b
        elif operator=='-':
            return a-b
        elif operator=='*':
            return a*b
        elif operator=='/':
            if b==0:
                return ZeroDivisionError
            return a/b
        elif operator=='%':
            if b==0:
                return ZeroDivisionError
            return a%b
        elif operator=='**':
            return a**b
        else:
            return TypeError

    except Exception as e:
        print(e)

try:
    a=float(input("Enter A value"))
except ValueError as e:
    print(e)
try:
    b=float(input("Enter B value"))
    operator=input("Enter Operator")
    answer=operation(a, b, operator)
    print(answer)
except ValueError as e:
    print(e)

