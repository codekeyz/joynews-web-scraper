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