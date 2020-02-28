import pandas as pd
import textdistance
import os
import re


truck_df = pd.read_csv('truck_names.txt',sep=";")

truck_df.model = truck_df.model.str.replace('-',' ')

def tokenize_basic(text):
    '''
    This function makes user input case-insensitive.
    Additionally, it tokenizes the text 
    so that future operations can be applied easier.
    '''
    
    text = str(text)
    tokens = []
    text = re.sub(r'-|,|\.|\||_',' ',text)
    for word in text.split():
        if word.isalpha:
            word_low = word.lower()
            tokens.append(word_low)
        else:
            tokens.append(word)
    return(tokens)   


truck_df['model_tokens'] = truck_df.model.apply(tokenize_basic)
truck_df['model_tokens_joined'] = truck_df.model_tokens.apply(lambda x: ''.join(x))
truck_df['manufacturer_tokens'] = truck_df.manufacturer.apply(tokenize_basic)
truck_df['manufacturer_tokens_joined'] = truck_df.manufacturer_tokens.apply(lambda x: ''.join(x))
truck_df['model_number'] = truck_df.model_tokens.apply(
    lambda x:[element for element in x if element.isdigit()])
truck_df['model_number'] = truck_df.model_number.apply(
    lambda x: ''.join(x) if len(x) > 0 else '-')

def similarity_score(s1,s2):
    '''
    This function returns a measure of a text similarity 
    based on Levenshtein distance.
    
    It is scaled by the maximum length of the compared strings. 
    The value returned is between 0 and 1, 
    therefore text similarities can be compared with each other.
    
    1 minus the scaled distance gives the similarity, just to make things intuitive.
    '''
    return(1-textdistance.levenshtein.distance(s1,s2)/max(len(s1),len(s2)))


def truck_recommender(tokens):
    '''
    This function takes the tokenized user as input 
    and returns a data frame of most similar 
    truck manufacturer and model name pairs.
    
    The similarity is measured by the function similarity_score,
    which is defined previously.
    '''
    user_truck = ''.join(tokens)
    
    if user_truck in truck_df.model_tokens_joined.tolist():
    # If the tokenized and joined user response happens to be in the data set,
    # return the relevant subset of the data set.
        return(truck_df[truck_df.model_tokens_joined == user_truck])
    
    else:
    # If not, collect and join all the words in the user response.
    # Then search for the most similar manufacturer (or manufacturers) 
    # to the obtained string.
    
        suggested_truck = ''.join([t for t in user_truck if t.isalpha()])
        
        # The function similarity_score is applied here:
        similarities = truck_df.manufacturer_tokens_joined.apply(
            lambda x: similarity_score(x,suggested_truck))
        
        # Collect the indices of the most similar manufacturers in the data frame
        sim_idx = similarities[similarities == similarities.max()].index.tolist()
        
        return(truck_df.iloc[sim_idx])

def ChatForTrucks():
    exit_flag=True
    welcome_message = """

    Welcome to the Tracks GmbH Truck Identification System

    This is your personal assistant
    In case you want to exit and save the progress, type exit

    """

    goodbye_message = "Good Bye! Drive safe and efficient..."
    truck_name_query = "Please type the manufacturer and the model of your truck. Example: Agrale 8700"
    truck_number_query = "What is the fleet number of "
    truck_spec_query = "What is the total axle load of "
    non_digit_warning = "This record will be skipped if you don\'t enter a digit"

    print(welcome_message)
    records = []
    while(exit_flag==True):
        if len(records)>0:
        # If there are already recorded trucks, print 'Next Truck' at the beginning.
            print(os.linesep + os.linesep + 'Next Truck: ' + truck_name_query)
        else:
        # Else begin with asking the truck's manufacturer its model name. 
            print(truck_name_query)

        # Tokenize the user response for the truck manufacturer and model.
        user_response = input()
        user_response_tokens = tokenize_basic(user_response)

        if 'exit' not in user_response_tokens:

            # Get a name recommendation based on Levenshtein distance
            # in case the user input cannot be matched with any manufacturer-model pairs.
            df_recommend = truck_recommender(user_response_tokens)

        ### Case 1: 1-to-1 truck manufacturer and name match
            if ''.join(user_response_tokens) in truck_df.model_tokens_joined.tolist():    
                print('The manufacturer is identified as ' + df_recommend.manufacturer.iloc[0])
                print(truck_number_query + df_recommend.model.iloc[0] + "?")
                print(non_digit_warning)

                # Proceed on requesting the fleet number in Case 1.
                fleet_number = input()
                if str(fleet_number).lower() == 'exit':
                    # Premature exit for the fleet number in Case 1.
                    # Exiting: Write the log file and give the user a notice about it.
                    print(goodbye_message + os.linesep)
                    print('... Logging ...' + os.linesep)
                    with open('records.txt', 'w') as fo:
                        print(';'.join(['manufacturer_model','fleet_number','total_axle_load']), file=fo)
                        for rec in records:
                            print(';'.join(rec), file=fo)
                    print(';'.join(['manufacturer_model','fleet_number','total_axle_load']))
                    for rec in records:
                        print(';'.join(rec))
                    exit_flag = False    

                elif fleet_number.isdigit() == False :
                    # Invalid response for the fleet number in Case 1.
                    print('The truck is not recorded.')
                    continue
                    print(os.linesep)
                else:
                    # Valid response for the fleet number in Case 1.
                    print(truck_spec_query + df_recommend.model.iloc[0] + ' Fleet #'+ str(fleet_number))
                    print(non_digit_warning)

                    # Proceed on requesting the truck specification in Case 1.
                    truck_spec = input()
                    if str(truck_spec).lower() == 'exit':
                        # Premature exit for the truck specification in Case 1.
                        # Exiting: Write the log file and give the user a notice about it.
                        print(goodbye_message + os.linesep)
                        print('... Logging ...' + os.linesep)
                        with open('records.txt', 'w') as fo:
                            print(';'.join(['manufacturer_model','fleet_number','total_axle_load']), file=fo)
                            for rec in records:
                                print(';'.join(rec), file=fo)
                        print(';'.join(['manufacturer_model','fleet_number','total_axle_load']))
                        for rec in records:
                            print(';'.join(rec))
                        exit_flag = False

                    elif truck_spec.isdigit() == False:
                        # Invalid response for the truck specification in Case 1.
                        print('The truck is not recorded.')
                        continue
                        print(os.linesep)
                    else:
                        # Valid response for the truck specification in Case 1.
                        print('Entry is recorded with success.')
                        print(df_recommend.model.iloc[0] +' Fleet #'+ str(fleet_number)
                              + ' Total Axle Load: ' + str(truck_spec))

                        record = [df_recommend.model.iloc[0],fleet_number,truck_spec ]
                        records.append(record)

        ### Case 2: no 1-to-1 truck manufacturer and name match
            else:
                if df_recommend.manufacturer_tokens_joined.unique().shape[0] == 1:
                # Find the most similar manufacturer (only manufacturer) to the user input in Case 2.
                    print('The manufacturer is identified as ' + df_recommend.manufacturer.iloc[0])

                    if len([t for t in user_response_tokens if t.isdigit()])==0:
                    # If the entry does not contain any number besides the manufacturer name,
                    # ask for the model number.

                        print('However, the model is missing.')
                        print('Please enter the model for '+ df_recommend.manufacturer.iloc[0] +':')
                        user_response_truck_model = input()
                        truck_model = user_response_truck_model.upper()
                        new_truck_name = df_recommend.manufacturer.iloc[0] + ' ' + truck_model
                    else:
                    # If the entry contains any number besides the manufacturer name,
                    # try to extract it without asking.

                        print('The model number you entered is new.')
                        print('It will be added to the database.')

                        remaining = re.sub(df_recommend.manufacturer_tokens_joined.iloc[0],
                                           '',''.join(user_response_tokens))
                        truck_model = remaining.upper()
                        new_truck_name = df_recommend.manufacturer.iloc[0] + ' ' + truck_model

                    print(truck_number_query + new_truck_name + ' ? ')
                    print(non_digit_warning)

                    # Proceed on requesting the fleet number for Case 2
                    fleet_number = input()
                    if str(fleet_number).lower() == 'exit':
                        # Premature exit for the fleet number in Case 2.
                        # Exiting: Write the log file and give the user a notice about it.
                        print(goodbye_message + os.linesep)
                        print('... Logging ...' + os.linesep)
                        with open('records.txt', 'w') as fo:
                            print(';'.join(['manufacturer_model','fleet_number','total_axle_load']), file=fo)
                            for rec in records:
                                print(';'.join(rec), file=fo)
                        print(';'.join(['manufacturer_model','fleet_number','total_axle_load']))
                        for rec in records:
                            print(';'.join(rec))
                        exit_flag = False   
                    elif fleet_number.isdigit() == False:
                        # Invalid response for the fleet number in Case 2.
                        print('The truck is not recorded.')
                        continue
                        print(os.linesep)
                    else:
                        # Valid response for the fleet number in Case 2.
                        print(truck_spec_query  + new_truck_name + ' Fleet #'+ str(fleet_number) + '?')
                        print(non_digit_warning)

                        # Proceed on requesting the truck specification in Case 2.
                        truck_spec = input()
                        if str(truck_spec).lower() == 'exit':
                            # Premature exit for the truck specification in Case 2.
                            # Exiting: Write the log file and give the user a notice about it.
                            print(goodbye_message + os.linesep)
                            print('... Logging ...' + os.linesep)
                            with open('records.txt', 'w') as fo:
                                print(';'.join(['manufacturer_model','fleet_number','total_axle_load']), file=fo)
                                for rec in records:
                                    print(';'.join(rec), file=fo)
                            print(';'.join(['manufacturer_model','fleet_number','total_axle_load']))
                            for rec in records:
                                print(';'.join(rec))
                            exit_flag = False


                        elif truck_spec.isdigit() == False :
                            # Invalid response for the truck specification in Case 2.
                            print('The truck is not recorded.')
                            continue
                            print(os.linesep)
                        else:
                            # Valid response for the truck specification in Case 2.
                            print('Entry is recorded with success.')
                            print(new_truck_name +' Fleet #'+ str(fleet_number)
                              + ' Total Axle Load: ' + str(truck_spec))

                            record = [new_truck_name ,fleet_number,truck_spec ]
                            records.append(record)

                else:
                     print('''

                     The manufacturer is not known at all.

                     Please contact to us.

                     ''')
        else:
            # Exiting: Write the log file and give the user a notice about it.
            print(goodbye_message + os.linesep)
            print('... Logging ...' + os.linesep)
            with open('records.txt', 'w') as fo:
                print(';'.join(['manufacturer_model','fleet_number','total_axle_load']), file=fo)
                for rec in records:
                    print(';'.join(rec), file=fo)
            print(';'.join(['manufacturer_model','fleet_number','total_axle_load']))
            for rec in records:
                print(';'.join(rec))
            exit_flag = False
            
            
# initialize
ChatForTrucks()
