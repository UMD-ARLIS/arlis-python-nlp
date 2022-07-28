import transformers
from transformers import pipeline

from newspaper import Article
import nltk
nltk.download('punkt')
import pandas as pd
import spacy
nlp = spacy.load('en_core_web_lg')

#Location Finder
def locationFinder(text):
    gpe = [] # countries, cities, states
    loc = [] # non gpe locations, mountain ranges, bodies of water
    doc = nlp(text)
    for ent in doc.ents:
      if (ent.label_ == 'GPE'):
        gpe.append(ent.text)
      elif (ent.label_ == 'LOC'):
        loc.append(ent.text)
    return gpe, loc

#Extraction people and organizations involved
def nameEntityFinder(paragraph):
    doc = nlp(paragraph)
    nameEntityDict = {}
    nameEntityDict_v2 = {}
    for ent in doc.ents:
      nameEntityDict[ent.text] = ent.label_
      
    for (key, value) in nameEntityDict.items():
        if value == 'PERSON' or value == 'ORG':
            nameEntityDict_v2[key] = value
    return nameEntityDict_v2

#Returns sector of deployment
def get_Sector_of_Deployment(text):
  sectorDeployment = ['Information and communication', 'Arts, entertainment and recreation', 'Transportation and storage', 'Public administration and defence', 'Administrative and support service activities', 'Human health and social work activities', 'Education', 'Professional, scientific and technical activities', 'Financial and insurance activities', 'Wholesale and retail trade', 'Activities of households as employers', 'Accommodation and food service activities']
  vector = classifier(text, sectorDeployment)
  return vector['labels'][0]

#Return sector of infrastructure
def get_infrastructure_sector(text):
  infrastructureSector = ['Transportation', 'Healthcare and public health', 'Government facilities', 'Communications', 'Food and agriculture', 'Critical manufacturing', 'Nuclear', 'Financial services', 'Information technology']
  vector = classifier(text, infrastructureSector)
  return vector['labels'][0]

#Return harm type
def get_harm_type(text):
  harmType = ['Harm to social or political systems', 'Harm to civil liberties', 'Harm to physical health/safety', 'Psychological harm', 'Financial harm', 'Harm to physical property', 'Harm to intangible property', 'Other:Harm to publicly available information', 'Other:Reputational harm; False incarceration', 'Other:Reputational harm', 'Other:Privacy', 'Other', 'Other:Reputational harm/social harm (libel and defamation)']
  vector = classifier(text, harmType)
  return vector['labels'][0]

#Returns pandas dataframe of all functions
def totalFunctions(url):
  article = Article(url)
  article.download()

  article.parse() #parses through the text
  article.nlp() 
  article.keywords
  df = pd.DataFrame()
  df['Function']=['Keywords', 'Author', 'Article Summary', 'Harm Type', 'Sector of Deployment', 'Sector of Infrastructure', 'Named Entities']
  df['Result']=[article.keywords, article.authors, article.summary, get_harm_type(article.text), get_Sector_of_Deployment(article.text), get_infrastructure_sector(article.text), nameEntityFinder(article.text)]
  return df
