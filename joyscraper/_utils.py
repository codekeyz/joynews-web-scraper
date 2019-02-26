def getImageFromElementCSS(element):
    styles = str(element).split(';')
    if styles:
        matches = []
        for style in styles:
            if style.startswith('background-image'):
                matches.append(style)
        return matches[0].split('(')[1].split(")")[0]
    else:
        return ''


def parseArticle(articles):
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
        # data['image'] = getImageFromElementCSS(article.div['style'])
        result.append(data)
    return result
