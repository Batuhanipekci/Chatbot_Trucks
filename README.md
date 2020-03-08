# First Ideas
Building a chatbot for getting truck fleet information

## Task Description
We need to build a small interactive system (Chat Bot) to identify trucks, their specification and number in particular fleet.

* Customer is Fleet Owner or Fleet manager.

* End result of conversation should be a list of trucks with their specifications and numbers.

* All conversations should be recorded for future analysis.


## Chat Bot
The chat bot is designed to retrieve data from fleet managers. If the user input is found exactly in the predefined corpus of truck manufacturers and names, it asks for the fleet number and then a truck specification (total axle load). Otherwise, the chat bot tries to correct the user input depending on a text similarity measure. If the manufacturer's name can be extracted, but not the truck model, the chat bot tries to infer the model name (by looking if there is any number in the user input). When the user exits the chatbot, it writes the accepted entries in a file, [records.txt](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/version1/records.txt).

This selective behavior allows us to retrieve data from the fleet managers in a clean way. Irrelevant entries are not accepted, and ones which can be corrected are attempted to correct.

The following diagram demonstrates the functionality of the chat bot

![Chatbot Graph](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/version1/chatbot_graph.png)
## How to Use

Install required packages (pandas and textdistance) in [requirements.txt](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/version1/requirements.txt)

Run [chatbot_trucks.py](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/version1/chatbot_trucks.py) on terminal.

The output will be written in the file [records.txt](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/version1/records.txt)

## Submission
A detailed explanation can be found at [Notebook_Chatbot.ipynb](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/version1/Notebook_Chatbot.ipynb)

The steps are roughly the following:

1. Web scraping the names of truck manufacturers and track models from https://en.wikipedia.org/wiki/List_of_trucks and writing them to [truck_names.txt](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/version1/truck_names.txt). It serves as a corpus which is used for correcting misspellings and making model recommendations.

2. Text Preprocessing by tokenizing the text and normalizing it different ways to capture the user input better.

3. Measuring text similarity by a scaled version of Levenshtein distance https://en.wikipedia.org/wiki/Levenshtein_distance

4. A function is written to give recommendations based on text similarity between the user input and the corpus.

5. The chat bot ChatForTrucks() is constructed by considering various scenarios including misspellings of the truck manufacturer's name, missing information on the truck model, user inputs which are irrelevant to the purpose of collecting the data from the fleet managers. In addition, knowledge on the fleet number and the specification (the total axle size) is gathered. The results are written in [records.txt](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/version1/records.txt).

6. Various test cases are tried and their results are reported in the seventh chapter of [Notebook_Chatbot.ipynb](https://github.com/Batuhanipekci/TracksGmbH_Chatbot/blob/version1/Notebook_Chatbot.ipynb)

7. Further uses of the gathered data are discussed for future reference.
