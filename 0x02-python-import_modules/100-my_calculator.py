#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, div, mul, sub
    if not len(sys.argv) == 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    answer = 0
    if operator == '+':
        answer = add(a, b)
    elif operator == '-':
        answer = sub(a, b)
    elif operator == '*':
        answer = mul(a, b)
    elif operator == '/':
        answer = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, answer))
