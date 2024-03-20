from art import logo

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2


def calculator():
    print(logo)
    operations={'+':add,'-':sub,'*':mult,'/':div}
    num1=float(input("What's your number? "))
    for symbol in operations:
        print(symbol)

    should_continue=True

    while should_continue:
        operation_symbol=input("Select an operation symbol from the above? ")
        num2=float(input("What's your next number? "))
        caluculation= operations[operation_symbol]
        answer=caluculation(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice=input("Press y to continue and anything to exit and start new calculator: ")
        if choice=='y':
            num1=answer
        else:
            should_continue='False'
            calculator()

calculator()

