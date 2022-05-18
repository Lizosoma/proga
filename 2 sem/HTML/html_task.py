from bs4 import BeautifulSoup
import requests

def lecture(year, season):
    response = requests.get(f'http://students.iposov.spb.ru/{year}{season}/')
    html = BeautifulSoup(response.text, features="html.parser")
    section = html.find('section', {'class':'main-content'})
    univ = section.find('ul')
    courses = univ.find_all('ul')
    for i in courses:
        for j in i.find_all('li'):
            yield j.find('a').text


print(list(lecture(22, 'spring')))

def taxonomy(animal):
    response = requests.get(f'https://ru.wikipedia.org/wiki/{animal}')
    html = BeautifulSoup(response.text, features="html.parser")
    table = html.find('td', {'class':'plainlist'})
    classes = table.find_all('div', {'class':'ts-Taxonomy-rang-row'})
    dictionary = dict()
    for item in classes:
        classification = item.find('div', {'class':'ts-Taxonomy-rang-label'}).text.replace(':', '')
        name = item.find('div', {'class':'ts-Taxonomy-rang-name'}).text
        dictionary[classification] = name
    return dictionary

print(taxonomy('Ирбис'))

def circylarity(link):
    reference = f'/wiki/{link}'
    titles = []
    for l in range(101):
        response = requests.get(f'https://ru.wikipedia.org{reference}')
        html = BeautifulSoup(response.text, features="html.parser")
        title = html.find('h1', {'class':'firstHeading'}).text
        if title in titles:
            break
        else:
            titles.append(title)
        info = html.find('div', {'id':'mw-content-text'})
        paragraph = info.find_all('p')
        b_flag = False
        for p in paragraph:
            links = p.find_all('a')
            sups = p.find_all('sup')
            for a in links:
                flag = False
                for sup in sups:
                    if a in sup:
                        flag = True
                        break
                if flag:
                    flag = False
                    continue
                if 'язык' in str(a.get('title')) or 'https' in str(a.get('href')) or 'index' in str(a.get('href')):
                    continue
                else:
                    reference = a.get('href')
                    b_flag = True
                    break
            if b_flag:
                b_flag = False
                break
    return titles

print(circylarity('Эксперимент Хофлинга'))
