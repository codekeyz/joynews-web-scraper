# JoyNews Ghana Web Scraper
Tired of Going online to read some hot News from JoyNews Ghana Web, so just decide to create this little script and use in an API for my own customized Android News App.

## Usage

```python
from joyscraper import JoyScraper

headlines = JoyScraper.get_headlines()
crimenews = JoyScraper.get_crimenews()

print(headlines)

print(crimenews)

```

#### Headlines Response

```jsons
[
    {   
        'link': 'https://www.myjoyonline.com/news/2019/February-25th/eoco-boss-kk-amoah-retires.php',
        'title': 'EOCO boss K.K. Amoah to retire end of February ', 
        'category': 'Main Headline', 
        'image': 'https://photos.myjoyonline.com/photos/news/201401/176552325124_166433872499.jpg'
    }
    ...
]
```

#### Crime News Response

```jsons
[ 
    {
        'link': 'https://www.myjoyonline.com/news/2019/February-19th/shs-student-in-court-over-5-robbery-at-knifepoint.php',
        'image': 'https://photos.myjoyonline.com/photos/news/201501/4417680729077_4626410929744.jpg", 
        'title': "SHS student in court over \u00a25 robbery at knifepoint", 
        'date': "February 19, 2019",
        'views': '5588'
    }
    ...
]
```

#### Todo's
- Latest Business News
- Latest Politics News


##### Inspired by [Eklhënäm Mensah]('https://github.com/maaddae')
