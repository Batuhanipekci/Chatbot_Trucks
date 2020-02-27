# TracksGmbH_Chatbot
Submission to the Recruitment Exam of Tracks GmbH

# Task Description
We need to build a small interactive system (Chat Bot) to identify trucks, their specification and number in particular fleet.

* Customer is Fleet Owner or Fleet manager.

* End result of conversation should be a list of trucks with their specifications and numbers.

* All conversations should be recorded for future analysis.


# How to Use

Install required packages (pandas and textdistance) in [requirements.txt](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/requirements.txt)

Run [chatbot_trucks.py](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/chatbot_trucks.py) in terminal.

The output will be written in the file [records.txt](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/records.txt)

# Submission
A detailed explanation can be found at [Notebook_Chatbot.ipynb](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/Notebook_Chatbot.ipynb)

The steps are rougly the following:

1. Web scraping the names of truck manufacturers and track models from https://en.wikipedia.org/wiki/List_of_trucks and writing them to truck_names.txt. It serves as a corpus which is used for correcting misspellings and making model recommendations.

2. Text Preprocessing by tokenizing the text and normalizing it different ways to capture the user input better.

3. Measuring text similarity by a scaled version of Levenshtein distance https://en.wikipedia.org/wiki/Levenshtein_distance

4. A function is written to give recommendations based on text similarity between the user input and the corpus.

5. The chat bot ChatForTrucks() is constructed by considering various scenarios including misspellings of the truck manufacturer's name, missing information on the truck model, user inputs which are irrelevant to the purpose of collecting the data from the fleet managers. In addition, knowledge on the fleet number and the specification (the total axle size) is gathered. The results are written in [records.txt](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/records.txt).

6. Various test cases are tried and their results are reported in the seventh chapter of [Notebook_Chatbot.ipynb](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/master/Notebook_Chatbot.ipynb)

7. Further uses of the gathered data are discussed for future reference.
