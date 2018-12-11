
def add_nums(num1 = None,num2 = None):

    if num1 is not None and num2 is not None:
        sum = num1 + num2
        print(str(num1) + " + " + str(num2) + " = " + str(sum))
    else:
        print("No inputs recieved!")
        sum = None

    return(sum)

add_nums(2.2323424234,4.342352352)


def main():
    add_nums(10,12)

    
main()
