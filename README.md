# JoyNews Ghana Web Scraper
Tired of Going online to read some hot News from JoyNews Ghana Web, so just decide to create this little script and use in an API for my own customized Android News App.

## Usage

```python
from joyscraper import JoyScraper

headlines = JoyScraper().get_headlines()

print(headlines)
```

### Response

```jsons
[
    {   
        'link': 'https://www.myjoyonline.com/news/2019/February-25th/eoco-boss-kk-amoah-retires.php',
        'title': 'EOCO boss K.K. Amoah to retire end of February ', 
        'category': 'Main Headline', 
        'image': 'https://photos.myjoyonline.com/photos/news/201401/176552325124_166433872499.jpg'
    }
]
```

#### Todo's
- Latest Business News
- Latest Crime News
- Latest Politics News



##### Inspired by [Eklhënäm Mensah]('https://github.com/maaddae')
