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

    user_info_list = GreetingsBot()
    if user_info_list[0]['Trucks Owned'] == 'yes':
        # Continue only if the user owns a truck ...
        truck_brands_list = TruckNameBot()
        truck_summaries = SpecsBot(truck_brands_list[0])
        
        print(os.linesep + 'User information, truck summaries, and dialogs are saved.')

        with open('results/user_information.txt', 'w') as fo:
            print(';'.join(['user_name', user_info_list[0]['User Name']]), file=fo)
            print(';'.join(['company', user_info_list[0]['Company Name']]), file=fo)
            print(';'.join(  ['trucks_owned', user_info_list[0]['Trucks Owned']]   ), file=fo)


        with open('results/truck_summaries.txt', 'w') as fo:
            print(';'.join(['brand','model','count','engine_size','axles','weight','max_load']), file=fo)
            for i in range(len(truck_summaries)):
                specs = list(map(str, truck_summaries[i][1][1][0]))
                print( ';'.join([truck_summaries[i][0],truck_summaries[i][1][0]] + specs), file=fo)


        with open('results/chatlog.txt', 'w') as fo:
            for i in range(len(user_info_list)):
                print('Chatbot: ' + user_info_list[1][i].replace('\n',''), file=fo)
                print('User: ' + user_info_list[2][i].replace('\n',''), file=fo)
            for i in range(len( truck_brands_list[2])):
                print('Chatbot: ' + truck_brands_list[2][i].replace('\n',''),file=fo)
                print('User: ' + truck_brands_list[3][i].replace('\n',''),file=fo)

            for i in range(len(truck_summaries )):
                print('\n ---- \n',file=fo)


                for k in range(len(truck_summaries[i][1][2])):

                    print('Chatbot: ' + truck_summaries[i][1][2][k].replace('\n',''),file=fo)
                    try:
                        print('User: ' + str(truck_summaries[i][1][3][k]).replace('\n',''),file=fo)
                    except:
                        print(' ',file=fo)
    else:
        print(os.linesep + "Good Bye! Drive safe and efficient...")
                        

# execute
ChatForTrucks()
