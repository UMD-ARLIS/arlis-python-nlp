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

### Creating article summary object for the article link 
To enter the website link into the code, the way it is done is through creating a article summary object. In the code block down below, the ArticleSummary object is article and inside the paranthesis of ArticleSummary is where you would enter your article link. The article would then be parsed, which is shown with the article.parse() command. 

```
article = ArticleSummary('https://www.cbsnews.com/news/is-starbucks-shortchanging-its-baristas/')
article.download()
article.parse() 
```

### Printing the article text into console 
To check if the above steps have worked, you can use the print(article.text) command and it would print all of the text from the article. This step is optional however it is highly reccomended in order to make sure the previous code has worked correctly. 

```
print(article.text)
```

### Using the library's functions to extract key information 
Once the above steps have been completed, you are know able to use the functions to get key information such as the article's summary and the article's publish date. Instructions on how to use these functions will be shown in the code blocks below.

#### Article summary
This function is used to get the summary of what the article is about. When this line of code is run, the summary of the article would get printed on the python console 

```
print(article.summary)
```

#### Article's authors
This function will be used to get the authors of the article itself, which will be printed on the python console.

```
print(article.authors)
```

#### Article's publish date
This function will get the date of when the article was published, which will then be printed using print().
```
print(article.publish_date)
```

#### Extracting the locations involved
This function will get the location's involved in the article. For example if the story of the article took place in the city of Seattle or Yosemitte National Park, this function will print those locations. 
```
print(article.locationfinder(articletext))
```

#### Getting the article's sector of deployment 
The AIID database has a taxonomy called [sector of deployment](https://incidentdatabase.ai/taxonomy/cset). This taxonomy categorizes an article based on the categories that AIID created. The list of categories is shown down below.
|                | Category List               |         |
|-----------------------------------------------|---------------------------------------------------|-------------------------------------------|
| Transportation and storage                    | Public administration and defence                 | Wholesale and retail trade                |
| Administrative and support service activities | Human health and social work activities           | Activities of households as employers     |
| Education                                     | Professional, scientific and technical activities | Accommodation and food service activities |
| Information and communication                 | Arts, entertainment and recreation                | Financial and insurance activities        |

Therefore it is important to know when using the function, the article would be cateogrized only based on the categories above. The codeblock that shows how to use this function is shown down below.
```
print(get_Sector_of_Deployment(article.text))
```

df2 = totalFunctions('https://www.washingtonpost.com/graphics/2019/local/teen-graffiti-hate-crime-divides-maryland-high-school/')


df2.to_csv('Test.csv', encoding='utf-8', index=False)


## Conclusion 
This library can extract key information however it is important to know that this process may not always be correct. Therefore if you are using this library for an important task, it is highly reccomended to check the results the code provides. Down below is a table that includes the names and contact information of the creators of this library. Please feel free to contact us using this contact information for any questions 
|Name       | Email Address|
|-----------|--------------|
Ujwal Gupta | ugupta12@umd.edu|
Marcus Hill | mhill128@umd.edu|
Ayushi Saxena | asaxena1@umd.edu|

