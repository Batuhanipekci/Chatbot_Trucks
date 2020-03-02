import os
from helper_functions import *
from truck_name_bot import *
from greetings_bot import *
from specs_bot import *


def ChatForTrucks():
    print("""

        Welcome to the Tracks GmbH Truck Identification System

        This is your personal assistant.

        """)
    dialog = list()
    user_info_list = GreetingsBot()
    dialog = dialog + user_info_list[1]
    if user_info_list[0]['Trucks Owned'] == 'yes':
        # Continue only if the user owns a truck ...
        truck_brands_list = TruckNameBot()
        dialog = dialog + truck_brands_list[2]
        truck_specs = SpecsBot(truck_brands_list[0])
        truck_summaries = truck_specs[0]
        dialog = dialog + truck_specs[1]
        
        print(os.linesep + 'User information, truck summaries, and dialogs are saved.')

        with open('results/user_information.txt', 'w') as fo:
            print(';'.join(['user_name', user_info_list[0]['User Name']]), file=fo)
            print(';'.join(['company', user_info_list[0]['Company Name']]), file=fo)
            print(';'.join(  ['trucks_owned', user_info_list[0]['Trucks Owned']]   ), file=fo)


        with open('results/truck_summaries.txt', 'w') as fo:
            print(';'.join(['brand','model','count','engine_size','axles','weight','max_load']), file=fo)
            for i in range(len(truck_summaries)):
                if len(truck_summaries[i][1][1]) == 0:
                    continue
                else:
                    for k in range(len(truck_summaries[i][1][1])):
                        specs = list(map(str, truck_summaries[i][1][1][k]))

                        print( ';'.join([truck_summaries[i][0],truck_summaries[i][1][0]] + specs), file=fo)

        with open('results/chatlog.txt', 'w') as fo:
            for d in range(len(dialog)):
                print(dialog[d].replace('\n',''), file=fo)
           
    else:
        print(os.linesep + "Good Bye! Drive safe and efficient...")
        with open('results/user_information.txt', 'w') as fo:
            print(';'.join(['user_name', user_info_list[0]['User Name']]), file=fo)
            print(';'.join(['company', user_info_list[0]['Company Name']]), file=fo)
            print(';'.join(  ['trucks_owned', user_info_list[0]['Trucks Owned']]   ), file=fo)
        
        with open('results/chatlog.txt', 'w') as fo:
            for d in range(len(dialog)):
                print(dialog[d].replace('\n',''), file=fo)
                        

# execute
ChatForTrucks()



