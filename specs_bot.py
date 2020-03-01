import os
from helper_functions import *



def collect_models(truck):
    '''
    Counts how many models there are
    for a given brand and returns the model list
    with the saved conversation
    '''
    # Collect the dialog with user_inputs and cb_prints
    user_inputs = list()
    cb_prints = list()

    cb_prints.append(os.linesep + 'How many {0} trucks do you have? '.format(truck))  
    print(cb_prints[len(cb_prints)-1])
    user_inputs.append(input_integer_select())
    number_models_truck = user_inputs[len(user_inputs)-1]


    cb_prints.append(os.linesep + 'Which models are they ? ')  
    print(cb_prints[len(cb_prints)-1])
    user_inputs.append(input())
    
    model_list=input_char_list(user_inputs[len(user_inputs)-1])


    flag = True
    while flag:

        count_list = []
        for model in model_list:
            if len(model_list) == 1:
                count = 1
                count_list.append(int(count))
                continue
            cb_prints.append(os.linesep + 'How many {0} do you have? '.format(model))  
            print(cb_prints[len(cb_prints)-1])
            user_inputs.append(input_integer_select())
            count = user_inputs[len(user_inputs)-1]
            count_list.append(int(count))

        else:
            flag = False

    return([list(zip(model_list, count_list)),cb_prints, user_inputs])


def specs_collect(model,truck_number):
    '''
    Takes collect_model()'s output as input and collect
    specifications.
    Asks the question of 'how many such trucks do you have?'
    in order to organize the information flow.
    '''
    user_inputs = list()
    cb_prints = list()

    flag=True
    while flag:

        specifications = []
        tn = 0
        actual_truck_number = truck_number
        while tn < truck_number:

            cb_prints.append('------------------------------'+ os.linesep + 'You have '
                             +'{0} unidentified trucks for {1}. '.format(actual_truck_number,model) +
                             'Please write the engine size of truck #{0} in liters.'.format(tn+1))  
            print(cb_prints[len(cb_prints)-1])
            user_inputs.append(input_integer_select(5000))
            engine_size = int(user_inputs[len(user_inputs)-1])


            cb_prints.append(os.linesep + 
                             'How many axles do you have for truck #{0}? '.format(tn+1))  
            print(cb_prints[len(cb_prints)-1])
            user_inputs.append(input_integer_select(20))
            axle_number = int(user_inputs[len(user_inputs)-1])



            cb_prints.append(os.linesep + 
                             'How much tonnes does truck #{0} weight? '.format(tn+1))  
            print(cb_prints[len(cb_prints)-1])
            user_inputs.append(input_float_select(100))
            weights = float(user_inputs[len(user_inputs)-1])

            cb_prints.append(os.linesep + 
                             'What is the maximum load in tonnes that truck #{0} can carry? '.format(tn+1))  
            print(cb_prints[len(cb_prints)-1])
            user_inputs.append(input_integer_select(100))
            max_load = int(user_inputs[len(user_inputs)-1])

            cb_prints.append(os.linesep +
                             'How many {0} with the same specification as truck #{1} do you have? '.format(model,tn+1)
                            +os.linesep + os.linesep)  
            print(cb_prints[len(cb_prints)-1])
            user_inputs.append(input_integer_select(100))
            similar_number_trucks = int(user_inputs[len(user_inputs)-1])


            specifications.append([similar_number_trucks,engine_size,axle_number,weights,max_load])
            tn = tn + similar_number_trucks
            actual_truck_number = actual_truck_number - similar_number_trucks

        if tn == truck_number:
            cb_prints.append(os.linesep + 
                             'All trucks for model {0} are recorded with success! '.format(model)+
                            os.linesep + '------------------------------' +os.linesep )  
            print(cb_prints[len(cb_prints)-1])
            flag=False
        else:
            cb_prints.append(os.linesep + '!!!!!!!!!!!!!!!'+os.linesep +
                             'The numbers do not match. Please enter specifications again: '.format(model)+
                            os.linesep + '!!!!!!!!!!!!!!!'+os.linesep)  
            print(cb_prints[len(cb_prints)-1])

    return([model,specifications,cb_prints,user_inputs])


def SpecsBot(brands):
    '''
    Runs collect_models()
    and specs_collect() in their respective loops
    '''
    results = []
    for b in brands:
        
        models_for_brand = collect_models(b)
        list_models = models_for_brand[0]
        
        for m in list_models:
            
            specs = specs_collect(m[0],m[1] )
            results.append([b,specs])
    
    return(results)



