from ._utils import getImageFromElementCSS
from ._conditions import is_crime_news
from ._request import simple_get
from ._parser import parse, tojson


class JoyScraper:

    @staticmethod
    def get_headlines(retry=False, retrytimes=0, retrymillis=0):
        response = simple_get('https://www.myjoyonline.com/ghana-news/news.php', retry, retrytimes, retrymillis)
        response = parse(response)
        if response is not '':
            mainentry = response.find('div', class_="entry-page-wrapper")
            if mainentry:
                articles = mainentry.findAll('article')
                if articles:
                    result = []
                    for article in articles:
                        data = {}
                        data['link'] = article.div.find('a')['href']
                        data['title'] = article.div.find('h2', class_="entry-title").text
                        category = article.find('div', class_="entry-category")
                        if category:
                            data['category'] = category.text
                        else:
                            data['category'] = 'Main Headline'

                        data['image'] = getImageFromElementCSS(article.div['style'])
                        result.append(data)
                    return tojson(result)
                else:
                    return None
            else:
                return None
        else:
            return None

    def get_crimenews(retry=False, retrytimes=0, retrymillis=0):
        response = simple_get('https://www.myjoyonline.com/ghana-news/news.php', retry, retrytimes, retrymillis)
        response = parse(response)
        if response:
            content = response.findAll('div', class_="wpb_wrapper")
            if content:
                for cont in content:
                    result = cont.find(is_crime_news)
                    if result:
                        articles = result.findAll('article')
                        if articles:
                            result = []
                            for article in articles:
                                data = {}

                                # Extracting the links
                                data['link'] = article.div.find('a')['href']

                                # Extracting the Trending Title
                                trending_title = article.div.find('h2', class_="entry-title")
                                if trending_title:
                                    data['title'] = trending_title.text

                                # Getting the Trending Category
                                trending_cat = article.find('div', class_="entry-category")
                                if trending_cat:
                                    data['category'] = trending_cat.text

                                # Getting the Trending Image
                                if article.div.has_attr('style'):
                                    style = article.div['style']
                                    data['image'] = getImageFromElementCSS(style)

                                # Getting the Sideline Crime New Image
                                imgdiv = article.find('img')
                                if imgdiv:
                                    style = imgdiv['style']
                                    if style:
                                        data['image'] = getImageFromElementCSS(style)

                                # Getting the Sideline Crime New Title
                                titlediv = article.find('h3', class_="entry-title")
                                if titlediv:
                                    data['title'] = titlediv.a.text

                                # Getting the Sideline Crime Date
                                datediv = article.find('span', class_="date-display")
                                if datediv:
                                    data['date'] = datediv.text

                                # Getting the Sideline Views Count
                                viewcount = article.find('span', class_="views-count")
                                if viewcount:
                                    data['views'] = viewcount.text

                                result.append(data)
                        return tojson(result)
        else:
            return None
