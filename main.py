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
    dragons_approach_text = 'You feel the gound shaking and soon sound of something big approach fast. It most be the dragon.'
    game_over = 'Dragons lair is over, hopp you hade fun and please try again, who know what will happen next time.'

    you_are_list = ('Strong', 'Fast', 'Smart')

    print('What are you')
    you_are_index = user_chose_from_list(you_are_list)

    print('You have manage to find a secret way into the dragons lair, but here a strange sound an notes the way you come form now is a solid stone wall.\nYou look around and see all kinds of treaseure and pils of gold to the celing')
    print('You find servral sevral thing of intressed. What do you want to get a closer to and have better look at?')
    look_closer_list = ('Lots of weaopns', 'Biggest pile of gems', 'Ropes in varius color')
    looked_closer_at = user_chose_from_list(look_closer_list)
    
    # depending on what user chose to look closer at will change what happens next
    if looked_closer_at == 0:
        # User have looked closer at Lots of weaopns
        print('You find many intressing and exotic weapons, some normal looking, some valuable looking.')
        print(dragons_approach_text)
        print('You look around but no good place to hidde. You panic, you think fight with one of the weapons is you best chans and grab?')
        weapon_list = ('Shine sword', 'Big axe', 'Sharp dagger')
        weapon_index = user_chose_from_list(weapon_list)

        if weapon_index == 0:
            print('With the Shine sword you will try to attack. As the dragons change at you, you dodge and attack the dragons and hit right in in its chest. You watch in horror as the blade of the swords brakes of into two pieces and shortly after you end as the dragons meal.')
            print(game_over)
            return True
        elif weapon_index == 1:
            print('With the Big axe you will try to attack. As the dragons change at you, you dodge and attack the dragons and hit right in in its chest.')
            if you_are_index == 0: # you_are_index 0 is Strong
                print('It hitts depp and the dragons falls over, rolling arund knocking arund treasure. Soon it is still and dead. Bringing back as much treasure you can carry. You liva a good life free from more danger in luxury.')
                print(game_over)
                return True
            else:
                print('It bounces of the dragons scale and shortly after you end as the dragons meal.')
                print(game_over)
                return True
        elif weapon_index == 2:
            print('With the sharp dagger ready in hand, the dragon gets close and open it mouth and a red light glows from it. You throw the dagger in its mouth. The dragon starts cough and you taka this chanse to flee. Weeks later far from the dragons lair you hear news that all settelment close to where you find the dragons lair hade beeen burnt down.')
            print(game_over)
            return True
        else:
            raise ValueError(f'Something has gone wrong and weapon_index is not a valid value but is: {weapon_index}')


    elif looked_closer_at == 1:
        # User have looked closer at biggest pile of gems
        print('You find you self drawn to the biggest pile of gems. It has gems of many color')
        print(dragons_approach_text)
        print('You have to get out of here, mayby you can sneak out, but leaving all the gems do not feel right.')
        while True:
            gems_taken = get_user_int_input('How many gems do you wish to take?\n')
            if gems_taken >= 0:
                break
            print('You dont have any gems to give')
        if gems_taken == 0:
            print('You easly sneak out without the dragons noticeing you. The rest of you live is as poor man where nothing intresting happen. Only now and the dream how life been if you hade take some of the gems at the dragons lair')
            print(game_over)
            return True
        elif gems_taken <= 21:
            print('You easly sneak out without the dragons noticeing you. You manage to live a modest life by selling you plunder form the dragons lair')
            print(game_over)
            return True
        elif gems_taken <= 44 or (you_are_index == 0 and gems_taken <= 58): # if user is strong it can carry more gems
            print('You sneak out without the dragons noticeing you but almost found you as all the gems slowed you down. You manage to live better then the king by selling you plunder form the dragons lair')
            print(game_over)
            return True
        else:
            print('You sneaking out was easy, until you drop some of the gems on the ground. As you turn around to see of the dragon notis you, all you see is a lot of flame filling the area. You are dead')
            print(game_over)
            return True

    elif looked_closer_at == 2:
        # User have looked closer ropes in varius color
        print('Something about the ropes are unusually and you find it intresting how many diffrent kind of rope the is here.')
        print(dragons_approach_text)
        print('What will you do. Mayby one of the ropes can be of used?')
        rope_list = ('Gray iron rope made by the orcs', 'Red silk rope with range markings', 'Thin yellow rope, probebly made by a fairy')
        rope_index = user_chose_from_list(rope_list)
        if rope_index == 0: # Gray iron rope made by the orcs
            if you_are_index == 0: # User is strong
                print('You bearly manage to lift the heavy iron rope. Not know what to do next, the dragon steps on you. You are dead')
                print(game_over)
                return True
            else:
                print('You don\'t manage to lift the heavy iron rope. Not know what to do next, the dragon steps on you. You are dead')
                print(game_over)
                return True
        elif rope_index == 1 or rope_index == 2: # Red silk rope with range markings or Thin yellow rope, probebly made by a fairy
            if rope_index == 1 and you_are_index == 2: # Red silk rope with range markings and Smart
                print('The dragon is get close and you take a look at the markings. It seems to be elven. Most of it you can not read, but as you read out loud the one part you can read a by speaking out melon. The rope start to glow and fly and become a collar around the dragons neck.\nNow you have a big pet dragon as the rope was magic to force someone to obey or it will start stangling the dragon. With the dragons help and your keen mind it was easy to take over the kingdom and expand it to cover the entire continent.')
                print(game_over)
                return True
            elif rope_index == 2 and you_are_index == 1: # Thin yellow rope, probebly made by a fairy and Fast
                print('You with the thin yello rope and your fast dashing to avoid danger you mange to tied up the dragon. You steal as much treasure you can and live like a king. You heard that dragons are magic create that that don\'t need to eat to survive so it may still be there, but you won\'t check as you will not risk you life ever again if you do not have to.')
                print(game_over)
                return True
            else:
                print('You stand there with you rope, but do not know what to do with it. Not know what to do next, the dragon steps on you. You are dead')
                print(game_over)
                return True

        else:
            raise ValueError(f'Something has gone wrong and rope_index is not a valid value but is: {rope_index}')
    else:
        raise ValueError(f'Something has gone wrong and looked_closer_at is not a valid value but is: {looked_closer_at}')
    raise SyntaxError(f'Something has gone wrong as the code shall not even be able to reach here')

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
