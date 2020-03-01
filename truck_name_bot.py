import os
from helper_functions import *



def TruckNameBot():

    user_inputs = list()
    cb_prints = list()
    cb_prints.append(os.linesep + 'What brands are they?')
    print(cb_prints[0])
    user_inputs.append(input())
    user_trucks = input_char_list(user_inputs[len(user_inputs)-1])

    # Check the user input for trucks
    # The text similarities of all the entered brand names are computed
    recommendations = [[t] + truck_recommender(t) for t in user_trucks 
                       if truck_recommender(t)[1] == 'recommendation']
    exact_matchs = [[t] + truck_recommender(t) for t in user_trucks 
                       if truck_recommender(t)[1] == 'exact_match']
    not_founds = [[t] + truck_recommender(t) for t in user_trucks 
                       if truck_recommender(t)[1] == 'not_found']

    # Decide whether to change the user's input or not
    to_replace = []
    replace_with = []

    if len(recommendations)>0:
        # For the brands we have a recommendation
        for recomm in recommendations:
            # you did_you_mean_that function to ask
            # the user her opinion about the
            # recommended brand name
            
            output = did_you_mean_that(recomm[0],recomm[1])
            cb_prints = cb_prints + output[2]
            user_inputs = user_inputs + output[3]
            
            if output[1] is None:
                # If the user rejects the recommendation
                # but doesn't change her previous answer,
                # or accepts the recommendation
                replacement = [recomm[0],output[0]]

                to_replace.append(recomm[0])
                replace_with.append(output[0])

            else:
                # If the user rejects the recommendation,
                # and gives a new input
                cb_prints.append(os.linesep + 'I am checking your input again ...')
                print(cb_prints[len(cb_prints)-1])
                
                # The similarity scores for the new input are computed
                new_recomm = truck_recommender(output[0])

                if new_recomm[1] == 'not_found':
                    # If nothing can be recommended for the new input,
                    # replace user's previous input with her last input
                    replacement = [recomm[0],new_recomm[0]]
                    to_replace.append(recomm[0])
                    replace_with.append(new_recomm[0])

                    cb_prints.append(os.linesep + 'I couldn\'t find the brand name,' +
                          'but I will record your suggestion.')
                    print(cb_prints[len(cb_prints)-1])
                else:
                    # If there is a recommendation, do not let
                    # the user enter another input again.
                    # Take the recommendation as it is.
                    
                    replacement = [recomm[0],new_recomm[0]]
                    to_replace.append(recomm[0])
                    replace_with.append(new_recomm[0])

                    cb_prints.append(os.linesep + 'Oh, you meant ' +new_recomm[0]+
                          '. Okay.')
                    print(cb_prints[len(cb_prints)-1])

    if len(not_founds)>0:
        for nf in not_founds:
            # For the brands we have no recommendation
            replacement = [nf[0],nf[1]]
            to_replace.append(nf[0])
            replace_with.append(nf[1])
            cb_prints.append(os.linesep + 'I couldn\'t find the brand name,' +
                  'but I will record your suggestion.')
            print(cb_prints[len(cb_prints)-1])



    final_trucks = []
    # Replace the original brand list with the corrected brand names
    for tr in user_trucks:
        if tr in to_replace:
            final_trucks.append(replace_with[to_replace.index(tr)])

        else:
            final_trucks.append(tr)
            
    return([final_trucks,user_trucks,cb_prints,user_inputs ])
   
