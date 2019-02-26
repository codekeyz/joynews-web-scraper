from joyscraper import JoyScraper

#HeadLines
headlines = JoyScraper.get_headlines()
print(headlines)

# Crime News
crimeNews = JoyScraper.get_crimenews()
print(crimeNews)
