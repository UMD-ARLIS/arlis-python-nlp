#On console: pip install arlis-python-nlp

from arlis-python-nlp import ArticleSummary
from arlis-python-nlp import ArticleExtraction
import nltk
nltk.download('punkt')

article = ArticleSummary('https://www.washingtonpost.com/graphics/2019/local/teen-graffiti-hate-crime-divides-maryland-high-school/')
article.download()

#parses through the text
article.parse() 
article.nlp() 
article.keywords

#Print article text
print(article.text)

#Get Summary of article (Full Description on AIID)
print(article.summary)

#Get authors
Article.authors

#Get publish date
article.publish_date
