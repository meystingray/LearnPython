def add_nums(num1,num2,num3 = 0,num4 = 0,num5 = 0):
    sum = num1 + num2 + num3 + num4 + num5
    print(num1,'+', num2,'+', num3,'+', num4,'+', num5, ' = ', sum)

def add_nums(*args):
    sum = 0
    printString = ""
    count = 1
    for i in args:
        sum = sum + i
        if count < len(args):
            printString = printString + str(i) +  " + "
        else:
            printString = printString + str(i)
        count = count + 1
    
    printString = printString + " = " + str(sum)
    print(printString)
    return(sum)


def main():
    add_nums(1,2)
    add_nums(1,2,3)
    add_nums(11,12,13,14)
    add_nums(101,201,301)
    add_nums(1,2,3,4,5,6,7,8,9,10)


main()