import assignmentModule14a
def chech_symbol(symbol,val1,val2):
    if symbol == "+":
        return assignmentModule14a.addition(val1,val2)
    elif symbol == "-":
        return assignmentModule14a.minus(val1,val2)
    elif symbol == "*":
        return assignmentModule14a.multiplication(val1,val2)
    elif symbol == "/":
        return assignmentModule14a.division(val1,val2)
    else:
        print("invalid symbol input")