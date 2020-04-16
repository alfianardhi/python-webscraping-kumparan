import requests

from bs4 import BeautifulSoup

html_datas = requests.get('https://kumparan.com/trending')
print(html_datas.status_code)
soup = BeautifulSoup(html_datas.text, 'html.parser')

trend_news = soup.find(attrs={'class':'NewsCardContainerweb__Scroll-sc-1fei86o-2 cXaeCj'})

titles = trend_news.find_all(attrs={'class':'TextBoxweb__StyledTextBox-n41hy7-0 jVPDss'})
for hasil in titles:
    print(hasil.find('a')['href'])
    print(hasil.find('a').find('span').text)

images = soup.find_all(attrs={'class':'Viewweb__StyledView-sc-61094a-0 gOZlJf'})
#for hasil in images:
    #print(hasil.find('a').find('img')['src'])

types_news = soup.find_all(attrs={'class':'FlexDominantweb__FlexDominant-rk9j2j-0 bMfDPz'})
#for hasil in types_news:
    #print(hasil.text)