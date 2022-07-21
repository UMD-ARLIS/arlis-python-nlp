# arlis-python-nlp
Natural Language Processing Libraries for Text Extraction and Indexing specifically designed for the articles in the [Artificial Intelligence Incident Database](https://incidentdatabase.ai/) (AIID)

## Introduction
This GitHub repository is for those who are involved in filling out the requried [taxonomy fields](https://incidentdatabase.ai/taxonomy/cset) for the articles in AIID. Many of the taxonomy fields as of writing this documentation have been filled manually, our program focuses on automating this process. The taxonomy fields that our program automates is Full description of the incident, Sector of deployment, Location, and Named Entities. If our work continues in the future, we will focus on trying to automate even more taxonomy fields. The way our program works is that you would import our libraries and use our functions to get these taxonomy fields. This is will be further explained in the following section.

## Usage 
This section will explain how to use our program to extract taxonomy fields for an article using our example program, [example.py](https://github.com/UMD-ARLIS/arlis-python-nlp/blob/main/example.py).

### Before using our program 
Our program uses our own library (arlis-python-nlp) as well as NLTK. Arlis-python-nlp and NLTK would have to be installed and imported for our program to run. Down below our two blocks that show how to install/import the required libraries. (Note: this does not include information on how to install NLTK)

#### Pip install our library, arlis-python-nlp
```
pip install arlis-python-nlp
```
#### Import required libraries 
```
from arlis-python-nlp import ArticleSummary
import nltk
nltk.download('punkt')
```


## Contributors
Ujwal Gupta | ugupta12@umd.edu
Marcus Hill | mhill128@umd.edu
Ayushi Saxena | asaxena1@umd.edu
If you have any questions, please contact us using the information above.
