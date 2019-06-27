actions=["+","-","*","/"]

class CalcException(Exception):
    pass


def check(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        arg1, arg2, action = result

        try:
            if "." in arg1:
                arg1 = float(arg1)
            else:
                arg1 = int(arg1)
        except ValueError:
            raise CalcException("error arg1")

        try:
            if "." in arg2:
                arg2 = float(arg2)
            else:
                arg2 = int(arg2)
        except ValueError:
            raise CalcException("error arg2")
        try:
            if action not in actions:
                print("action error")
        except ValueError:
            raise CalcException("error arg2")
        return arg1, arg2, action
    return wrapper

def outputData(arg1, arg2, action):
    if action == "+":
        print(arg1 + arg2)
    elif action == "-":
        print(arg1 - arg2)
    elif action == "*":
        print (arg1 * arg2)
    elif action == "/":
        print(arg1 / arg2)

@check
def inpData():
    arg1=input("print first nr")
    arg2=input("print second nr")
    action=input("specify action")
    return arg1, arg2, action




if __name__ == '__main__':
    try:
        m_arg1, m_arg2, m_action = inpData()
    except CalcException as e:
        print(e)
        exit(1)
    outputData(m_arg1, m_arg2, m_action)
