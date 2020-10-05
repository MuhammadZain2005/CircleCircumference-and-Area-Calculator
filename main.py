# Circumference and Area Calculator

class color:  # Color Class
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print("*********" + '\033[1m' "Circle's Circumference and Area Calculator" + color.END + "*********")


def circlewithradius(number1):
    return number1


def circlewithdiameter(number1a):
    return number1a


while True:
    input1 = input(
        '\033[94m' + "Choose Radius or Diameter\nIf radius then press R , or D for diameter" + color.END + '\033[91m' + "\nTo Quit Type "
                                                                                                                            "'quit' or 'q'" +
        color.END + "\nType your input = ")

    if input1 == "R" or input1 == "r":
        radius = float(input("What is the radius of your circle = "))
        Area = float(radius * radius * 3.14)
        circ = float(2 * 3.14 * radius)
        print("The area of the circle is = " + str(circlewithradius(Area)))
        print("The circumference of the circle is = " + str(
            circlewithradius(circ)) + "\n----------------------------------------")


    elif input1 == "D" or input1 == "d":

        dia = float(input("What is the diameter of your circle = "))
        Area1 = float(dia * dia * 0.25 * 3.14)
        circ1 = float(3.14 * dia)
        print("The area of the circle is " + str(circlewithdiameter(Area1)))
        print("The circumference of your circle is = " + str(
            circlewithdiameter(circ1)) + "\n----------------------------------------")
        continue

    elif input1 == "quit" or input1 == "Quit" or input1 == "q" or input1 == "Q":
        break

    else:
        print("Enter 'R' or 'D' \n----------------------------------------")
        continue
