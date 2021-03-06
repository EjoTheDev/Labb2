import platform
import psutil
import math


def GetPCInfo():
    Result = "\nName: "
    Result += platform.node()
    Result += "\nOS: "
    Result += platform.platform()
    Result += "\nCPU: "
    Result += platform.processor()
    Result += "\nArchitecture: "
    Result += platform.machine()
    Result += "\nMemory: "
    Result += str(math.ceil(psutil.virtual_memory().total/(1024.**3))) + "GB"
    Result += "\nMemory Usage: "
    Result += str(psutil.virtual_memory().percent) + "%"
    Result += "\nPython Version: "
    Result += platform.python_version()
    return Result
print(GetPCInfo())



#===========START Ninos Zaiya================
def show_welcome():
    print('\n=================================')
    print('            WELCOME')
    print('Calculate volume / area of a geometric shape')

def show_options():
    print('\n=================================')
    print('choose from an option below')
    print('1.Volume of an equilateral Cube')
    print('2.Area of an Square')
    print('3.Volume of an Sphere')
    print('4.Area of an Circle')
    print('5.Volume of an Cylinder')
    print('6.Exite')
    print('=================================')


def show_thnks():
    print('\n=================================')
    print('            THANKS')
    print('=================================')

    
PI = math.pi
options = [1,2,3,4,5,6]



def is_options(value):
    try:
        int_val = int(value)
        if int_val in options:
            return True
        else:
            return False
    except ValueError:
      return False


def cal_vol_cube(length):
  return length**3


def cal_area_square(s):
  return s**2


def cal_vol_sphere(r):
  return (3/4) * PI * (r**3)


def cal_area_circle(r):
  return PI * (r**2)


def cal_vol_cylinder(r,h):
  return PI * (r**2) * h

def exite_app():
  print("The Program Has Been Terminated By The User")
  

dic_shape_form = {1:cal_vol_cube,2:cal_area_square,3:cal_vol_sphere,4:cal_area_circle,5:cal_vol_cylinder,6:exite_app}



def start_cal():
  show_welcome()
  while True:
    show_options()
    choice = int(input("Please make your choice: "))
    while is_options(choice) == False:
      choice = int(input(f"Please make your right choice between ({str(options[0])}-{str(options[-1])}): "))
    if choice in dic_shape_form.keys():
      if choice == 1:
        unit = input("Which unit you want to use in this calculation? ")
        a = int(input("Enter the side length of Cube: "))
        print(f'Volume of an equilateral Cube is: {round(dic_shape_form[choice](a),2)}{unit}')
        ask = input('Want to make anothe calculate for another shape y/n: ').lower()
        if ask == 'n':
          break
      elif choice == 2:
        unit = input("Which unit you want to use in this calculation? ")
        r = int(input("Enter the length of Square: "))
        print(f'Area of an Square is: {round(dic_shape_form[choice](r),2)}{unit}')
        ask = input('Want to make anothe calculate for another shape y/n: ').lower()
        if ask == 'n':
          break
      elif choice == 3:
        unit = input("Which unit you want to use in this calculation? ")
        l = int(input("Enter the radius of Sphere: "))
        print(f'Volume of an Sphere is: {round(dic_shape_form[choice](l),2)}{unit}')
        ask = input('Want to make anothe calculate for another shape y/n: ').lower()
        if ask == 'n':
          break
      elif choice == 4:
        unit = input("Which unit you want to use in this calculation? ")
        r = int(input("Enter the radius of Circle : "))
        print(f'Area of an Circle is: {round(dic_shape_form[choice](r),2)}{unit}')
        ask = input('Want to make anothe calculate for another shape y/n: ').lower()
        if ask == 'n':
          break
      elif choice == 5:
        unit = input("Which unit you want to use in this calculation? ")
        h = int(input("Enter the height of Cylinder : "))
        r = int(input("Enter the radius of Cylinder : "))
        print(f'Volume of an Cylinder is: {round(dic_shape_form[choice](h,r),2)}{unit}')
        ask = input('Want to make anothe calculate for another shape y/n: ').lower()
        if ask == 'n':
          break
      elif choice == 6:
        print("\n")
        dic_shape_form[choice]()
        break
      else:
        print("Please, chose the corect option!!")  
  show_thnks()
#start_cal()
#=================END Ninos Zaiya========================