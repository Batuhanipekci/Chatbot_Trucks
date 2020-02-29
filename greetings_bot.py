import os
from helper_functions import *



def GreetingsBot():
    
    user_inputs = list()
    cb_prints = list()

    greeting_styles = ['Hi there,','Hallo,','Welcome onboard,','Hello']
    cb_prints.append(os.linesep + random.choice(greeting_styles) + ' what is your name?' )  
    print(cb_prints[0])

    user_inputs.append(input())
    name = ' '.join([n for n in user_inputs[0].split(' ') if n != ''])
    name = re.sub(r'[^a-zA-Z\s]', '',name)

    cb_prints.append(os.linesep + 'Hi '+ name +', what is the name of your company?')
    print(cb_prints[1])

    user_inputs.append(input())
    company = user_inputs[1]
    cb_prints.append(os.linesep + 'Do you own trucks at ' +company+' ?')
    print(cb_prints[2])
    user_inputs.append(input())
    truck_yn = user_inputs[2].lower()

    if all(letter in truck_yn for letter in ['y','e','s']):
        truck_dummy = 'yes'
   
    else:
        truck_dummy = 'no'
        
    
    user_information = {'User Name':name,
                       'Company Name': company,
                       'Trucks Owned': truck_dummy}
                       
    
    return([user_information,cb_prints,user_inputs] )
 