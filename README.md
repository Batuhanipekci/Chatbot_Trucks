# Tracks GmbH Chat Bot V2
Submission to the Recruitment Exam of Tracks GmbH

Run the file [chat_trucks_run.py](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/chat_trucks_run.py) on terminal, after installing necessary packages (only textdistance) at [requirements.txt](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/requirements.txt).

## Task Description
We need to build a small interactive system (Chat Bot) to identify trucks, their specification and number in particular fleet.

* Customer is Fleet Owner or Fleet manager.

* End result of conversation should be a list of trucks with their specifications and numbers.

* All conversations should be recorded for future analysis.

The second version of the project focused on conversational aspects of the chat bot. The first version, which discussed mainly the data-science related issues, can be found in the branch [version1](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/tree/version1).


## Chat Bot 

The chat bot asks the user if the company has trucks. After retrieving the information for the truck brand and model names, truck specifications are collected and organized.

At the end of the conversation, the [user_information](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/results/user_information.txt)), [truck_summaries](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/results/truck_summaries.txt), and the [chatlog](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/results/chatlog.txt) are written in respective files.

There are three main parts of the chat bot:

1. [The greetings bot](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/greetings_bot.py) welcomes the user, collects the user information, as well as, whether the company owns trucks.

2. If the company owns trucks, [the truck name bot](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/truck_name_bot.py) inquiries about the brand and model names. In order to ensure consistency between user inputs and the available database, it attempts to correct the misspellings in the brand name. This is done by calculating Levenshtein distance between the input and the web scraped data set of truck model names. The functionality at the [version1](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/tree/version1) is simplified by only focusing on brand names. Three cases are identified:

* In case of exact match, the user input is accepted as it is.
* In case of misspelling (happens when a unique maximum Levensthein similarity is attained within the data set), the chat bot gives recommendations by printing 'Did you mean that?' and expects confirmation. If the user does not confirm, (s)he is asked to enter a new brand name.
* In case there are more than one possible recommendable choices in the data set, the chat bot accepts what the user has given without asking anything. 

3. Having a list of brand names, [the specs bot](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/specs_bot.py) asks for model names for each brand and collects their specification. It attempts to organize the bulk of knowledge by asking 'how many such trucks do you have?' and writing the trucks with the same specifications as the count of a truck model, avoiding duplicate entries.


The script [helper_functions](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/helper_functions.py) stores functions that are common to all parts, such as specific input functions, a 'did you mean that' loop, a text cleaning function, a truck recommender tool based on Levenshtein distance etc. 

The run script [chat_trucks_run.py](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/chat_trucks_run.py) organizes all the three parts and prints out the results.

An example conversation is seen at [chatlog.txt](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/results/chatlog.txt) 


