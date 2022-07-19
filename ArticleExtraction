import spacy
nlp = spacy.load('en_core_web_lg')

import nltk
import sklearn
from newspaper import Article
nltk.download('punkt')
import bs4 as bs
import urllib.request
import re

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
