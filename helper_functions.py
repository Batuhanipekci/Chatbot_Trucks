import textdistance
import random
import string
import os
import re


def input_integer_select(integer_limit = 100):
    flag = True
    user_input = input()

    while flag:
        if user_input.isdigit():
            if int(user_input) > integer_limit:
                warning = ('Sorry, I can\'t process more than {0} ' + 
                           'right now. Please enter again:').format(integer_limit)
                print(warning)
                user_input = input()
            else:
                flag=False
        else:
            warning = 'I don\'t understand. Please enter an integer:'
            print(warning)
            user_input = input()
            
    return(int(user_input))


def input_char_list(text):
    text_list = text.split(',')
    result = []
    for tl in text_list:
        result = result + [tl.replace(' and ','').strip()]
    return(result)


def input_float_select(float_limit = 100.0):
    flag = True
    user_input = input()

    while flag:
        if user_input.replace('.','').isdigit():
            if float(user_input) > float_limit:
                warning = ('Sorry, I can\'t process more than {0}' + 
                           'right now. Please enter again:').format(float_limit)
                print(warning)
                user_input = input()
            else:
                flag=False
        else:
            warning = 'I don\'t understand. Please enter a floating number:'
            print(warning)
            user_input = input()
            
    return(round(float(user_input),2))

def did_you_mean_that(what_user_does,what_we_want):
    cb_prints = list()
    user_inputs_rec = list()
    
    
    cb_prints.append(os.linesep +'Did you mean {0} by saying {1} ?'.format(what_we_want,what_user_does))
    print(cb_prints[len(cb_prints)-1])
    user_input = input()
    user_inputs_rec.append(user_input)
    
    if all(letter in user_input.lower() for letter in ['y','e','s']):
        out = what_we_want
        suggestion = None
    
    else:
        cb_prints.append(os.linesep + 'Are you sure you meant that {0} exists? '.format(what_user_does))
        print(cb_prints[len(cb_prints)-1])
        user_input_sub = input()
        user_inputs_rec.append(user_input_sub)
        
        if all(letter in user_input_sub.lower() for letter in ['y','e','s']):
            cb_prints.append(os.linesep + 'If so, it seems like the entry doesn\'t exist in our database '+
                  os.linesep + 'We will save it now.')
            print(cb_prints[len(cb_prints)-1])
            out = what_user_does
            suggestion = None
        else:
            cb_prints.append(os.linesep +
                 'Could you then write what you meant?')
            print(cb_prints[len(cb_prints)-1])
            
            user_input_suggestion = input()
            out = user_input_suggestion
            user_inputs_rec.append(user_input_suggestion)
            suggestion = True
            
    return([out,suggestion,cb_prints,user_inputs_rec])





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

def clean_basic(text):
    '''
    This function makes user input case-insensitive.
    Additionally, it tokenizes the text 
    so that future operations can be applied easier.
    '''

    text = str(text)
    punct = set(string.punctuation)
    clean_text = ''.join(char for char in text if char not in punct)
    
    tokens = []
    for word in text.split():
            word_low = word.lower()
            tokens.append(word_low)

    return(''.join(tokens))   
    

def truck_recommender(user_input):
    '''
    Returns the most similar 
    truck manufacturer if exists
    '''
    user_input_rec = user_input
    user_input_clean = clean_basic(user_input)
    
    # Read the list
    manu_list = [line.rstrip('\n') for line in open('data/truck_manufacturer.txt','r')][1:]
    
    # Ensure that manufacturer's list is consisted of unique names
    manu_list = list(set(manu_list))
    
    manu_list_clean = [clean_basic(element) for element in manu_list]

    if user_input_clean in manu_list_clean:
    # If the cleaned user response happens to be in the list, return it.
        out = manu_list[manu_list_clean.index(user_input_clean)]
        status = 'exact_match'
        
    
    else:
    # If not, search for the most similar manufacturers
    
        similarities = [similarity_score(user_input_clean,x) for x in manu_list_clean]
        
        sim_idx = []
        for index, x in enumerate(similarities):
            if x == max(similarities):
                sim_idx.append(index)
        
        if len(sim_idx) == 1:
        # Uniquely most similar manufacturer
            out = manu_list[sim_idx[0]]
            status = 'recommendation'
        else:
        # Many most similar manufacturer
            out = user_input
            status = 'not_found'
    
    return([out, status, user_input_rec])
        

