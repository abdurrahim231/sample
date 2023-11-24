import assignmentModule14b

def run_again_check():
    run_again = input("do you wan to execute it again(y/n): ")

    if run_again == 'y':
        take_user_input()
    else:
        print("code end")


def take_user_input():
    value1 = float(input("Please enter the first value: "))
    value2 = float(input("Please enter the second value: "))


    symbol = input("Please enter the symbol(+,-,*,/) to execute: ")

    result = assignmentModule14b.chech_symbol(symbol,value1,value2)

    print("Result of your provided symbol '{}' is: {}".format(symbol,result))

    run_again_check()
    

if __name__ == "__main__":
    take_user_input()