logo=''' _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | ÷ | |
| |___|___|___| |___| |
|_____________________|
'''
def add(firzt,sec):
    add=firzt+sec
    print(f"{firzt} + {sec} = {add}")
    return add
def sub(firzt,sec):
    sub=firzt-sec
    print(f"{firzt} - {sec} = {sub}")
    return sub
def mul(firzt,sec):
    mul=firzt*sec
    print(f"{firzt} * {sec} = {mul}")
    return mul
def div(firzt,sec):
    div=firzt/sec
    print(f"{firzt} / {sec} = {div}")
    return div

check1 = True
check2= True
while check2:
    print(logo)
    print("Welcome to Calculator")
    first_num=float(input("enter the first number: "))
    check1 = True
    while check1:
        print("+")
        print("-")
        print("*")
        print("/")
        operator_sign = input("Pick an Operator: ")
        sec_num=float(input("enter the next number: "))
        if operator_sign=="+":
            num=add(first_num,sec_num)
            new_num=input(f"type y to contine calculating with {num}, or type 'n' to start a new calculation : ")
            if new_num=="y":
                first_num= num
                check1= True
            else:
                check1 =False
                check2=True
        elif operator_sign=="-":
            num=sub(first_num,sec_num)
            new_num=input(f"type y to contine calculating with {num}, or type 'n' to start a new calculation: ")
            if new_num=="y":
                first_num= num
                check1=True
            else:
                check1 =False
                check2=True
        elif operator_sign=="*":
            num = mul(first_num,sec_num)
            new_num=input(f"type y to contine calculating with {num}, or type 'n' to start a new calculation: ")
            if new_num=="y":
                check1=True
                first_num= num
            else:
                check1 =False
                check2=True
        else:
            num=div(first_num,sec_num)
            new_num=input(f"type y to contine calculating with {num}, or type 'n' to start a new calculation: ")
            if new_num=="y":
                first_num= num
                check1=True
            else:
                check1 =False
                check2=True