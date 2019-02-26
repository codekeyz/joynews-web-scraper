# Logic to Select the Block that has Crime News
def is_crime_news(tag):

    # Find All the Div's with section-title as class
    blocks = tag.findAll('div', {'class': 'section-title'})
    if blocks:
        for block in blocks:

            # check if the Block is a Crime News Block
            return block and block.find('span') and str(block.find('span').text).__eq__("Crime")
