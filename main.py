import math
import platform


def get_os_info():
    result = "\nName: "
    result += platform.node()
    result += "\nOS: "
    result += platform.platform()
    result += "\nCPU: "
    result += platform.processor()
    result += "\nArchitecture CPU: "
    result += platform.machine()
    result += "\nMemory: "
    result += "\nMemory Usage: "
    result += "\nPython Version: "
    result += platform.python_version()
    return result

print(get_os_info())


def get_input():
    try:
        res = int(input())
        return res
    except:
        return 0


def area_of_tetrahedron(side):
    return (side ** 3 / (6 * math.sqrt(2)))


def area_of_cube(side):
    volume = side**3
    return (volume)

def show_menu():
    print("välja en form")
    print("1. en kub ")
    print("2. tetrahedron")
    print("3. avsluta")


try:
    while True: 
        show_menu()
        option = get_input()
        if option == 1:
            side = float(input('Ange sida på en kuboid i cm '))
            print("Volym av kub = ", area_of_cube(side), "cm³")
        elif option == 2:
            side = float(input('Ange liksidig  på en tetrahedron i cm '))
            print("Volym av tetrahedron = ",round(area_of_tetrahedron(side), 4))
        elif option == 3:
            break
        else:
            print("det finns ett fel med input type")


except:
    print("error occurred during operation")