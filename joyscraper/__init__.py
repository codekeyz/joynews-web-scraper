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
                            # Getting All the CSS styles applied to the article child (DIV)
                        divstyles = str(article.div['style']).split(';')
                        if divstyles:
                            matches = []
                            for style in divstyles:
                                if style.startswith('background-image'):
                                    matches.append(style)

                        # Trying to get the background-image from the css applied to the div
                        data['image'] = matches[0].split('(')[1].split(")")[0]
                        result.append(data)
                    return tojson(result)
                else:
                    return None
            else:
                return None
        else:
            return None
