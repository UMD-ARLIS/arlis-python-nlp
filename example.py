#On console: pip install arlis-python-nlp

from arlis-python-nlp import ArticleSummary
from arlis-python-nlp import ArticleExtraction
from arlis-python-nlp import ArticleCategory
import nltk
nltk.download('punkt')

#Article Summary's object here is called article
article = ArticleSummary('https://www.washingtonpost.com/graphics/2019/local/teen-graffiti-hate-crime-divides-maryland-high-school/')
article.download()

#parses through the text
article.parse() 
article.nlp() 
article.keywords

#Print article text
articletext = print(article.text)

#Get Summary of article (Full Description on AIID)
print(article.summary)

#Get authors
Article.authors

#Get publish date
article.publish_date


#Article Extraction's object here is called extraction
extraction = ArticleExtraction
