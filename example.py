#On console: pip install arlis-python-nlp

from arlis-python-nlp import ArticleSummary
import nltk
nltk.download('punkt')

#Article Summary's object here is called article
article = ArticleSummary('https://www.washingtonpost.com/graphics/2019/local/teen-graffiti-hate-crime-divides-maryland-high-school/')
article.download()

#parses through the text - needed before article.text
article.parse() 

#Print article text if wanted (optional)
print(article.text)

#Get Summary of article (Full Description on AIID)
print(article.summary)

#Get authors
Article.authors

#Get publish date
article.publish_date


#Article Extraction's object here is called extraction
extraction = ArticleExtraction

#Get location of artilce
print(article.locationfinder(articletext))

#Get sector of deployment for article
get_Sector_of_Deployment(article.text)

#Get infrastructure deployment
get_infrastructure_sector(article.text)
