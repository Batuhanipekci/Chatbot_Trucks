import os
from helper_functions import *



def TruckNameBot():

    user_inputs = list()
    cb_prints = list()

    cb_prints.append(os.linesep + 'What brands are they?')  
    print(cb_prints[0])
    user_inputs.append(input())
    user_trucks = input_char_list(user_inputs[len(user_inputs)-1])
    #user_trucks = user_inputs[0].replace(',',' ')
    #user_trucks = user_trucks.replace(' and ',' ').split()
    # Check the user input for trucks

    recommendations = [[t] + truck_recommender(t) for t in user_trucks 
                       if truck_recommender(t)[1] == 'recommendation']
    exact_matchs = [[t] + truck_recommender(t) for t in user_trucks 
                       if truck_recommender(t)[1] == 'exact_match']
    not_founds = [[t] + truck_recommender(t) for t in user_trucks 
                       if truck_recommender(t)[1] == 'not_found']



    to_replace = []
    replace_with = []

    brand_replacements = []
    if len(recommendations)>0:
        for recomm in recommendations:
            output = did_you_mean_that(recomm[0],recomm[1])
            cb_prints = cb_prints + output[2]
            user_inputs = user_inputs + output[3]
            
            if output[1] is None:
                # Replace user's input with the recommendation
                replacement = [recomm[0],output[0]]

                to_replace.append(recomm[0])
                replace_with.append(output[0])

                brand_replacements.append(replacement)
            else:
                cb_prints.append(os.linesep + 'I am checking your input again ...')
                print(cb_prints[len(cb_prints)-1])
                new_recomm = truck_recommender(output[0])

                if new_recomm[1] == 'not_found':
                    replacement = [recomm[0],new_recomm[0]]
                    to_replace.append(recomm[0])
                    replace_with.append(new_recomm[0])

                    brand_replacements.append(replacement)
                    cb_prints.append(os.linesep + 'I couldn\'t find the brand name,' + 
                          'but I will record your suggestion.')
                    print(cb_prints[len(cb_prints)-1])
                else:
                    replacement = [recomm[0],new_recomm[0]]
                    brand_replacements.append(replacement)
                    to_replace.append(recomm[0])
                    replace_with.append(new_recomm[0])

                    cb_prints.append(os.linesep + 'Oh, you meant ' +new_recomm[0]+
                          '. Okay.')
                    print(cb_prints[len(cb_prints)-1])

    if len(not_founds)>0:
        for nf in not_founds:
            replacement = [nf[0],nf[1]]
            to_replace.append(nf[0])
            replace_with.append(nf[1])
            brand_replacements.append(replacement)
            cb_prints.append(os.linesep + 'I couldn\'t find the brand name,' + 
                  'but I will record your suggestion.')
            print(cb_prints[len(cb_prints)-1])


           


    final_trucks = []

    for tr in user_trucks:
        if tr in to_replace:
            final_trucks.append(replace_with[to_replace.index(tr)])

        else:
            final_trucks.append(tr)
            
    return([final_trucks,user_trucks,cb_prints,user_inputs ])
   