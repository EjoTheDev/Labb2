import platform
# # Temp comment for not haveing psutil
# import psutil 
import math

def get_user_int_input(question):
    # Get input from user called int_input as int based on str question. If input is not int reppet until it is an int.
    while True:
        try:
            int_input = int(input(question))
            break
        except ValueError:
            print('You have to chose a integer')
            pass

    return int_input

def user_chose_from_list(list):
    # take a list with strings and ask user to chose one and return the int chose_index that is index for that chose in list.
    chose_text = ''
    chose_counter = 1
    chose_number = 0

    for text in list:
        chose_text += f'{chose_counter}: {text}\n'
        chose_counter += 1
        
    while True:
        chose_number = get_user_int_input(chose_text)
        
        # check if chose_number is one of the list choices
        if chose_number <= len(list) and chose_number > 0:
            break
        else:
            print('You have to chose one of this choices')

    # chose_index is index chosen based on chose_number in list
    chose_index = chose_number - 1
    return chose_index

# thor main function
def dragons_lair():
    you_are_list = ('Strong', 'Fast', 'Smart')

    print('What are you')
    you_are_index = user_chose_from_list(you_are_list)
    print(f'You are {you_are_list[you_are_index]}')

    # TODO rest of the advangeure in the drgons lair

    return True

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

# # temp comments to not run
# print(GetPCInfo()) 

dragons_lair()
