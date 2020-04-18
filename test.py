import requests
from bs4 import BeautifulSoup
import pandas as pd

"""html_datas = requests.get('https://kumparan.com/trending')
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
    #print(hasil.text)"""

header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'}
for page in range(0,3):
    page_number = page + 1
    html_datas = requests.get('https://www.yell.com/ucs/UcsSearchAction.do',
                              params={'keywords': 'Restaurants', 'location': 'united+kingdom',
                                      'scrambleSeed': '1558621577', 'pageNum': page_number}, headers=header)
    soup = BeautifulSoup(html_datas.text, 'html.parser')

    soup_datas = soup.find(attrs={'class': 'row results--row results--capsuleList'})
    restaurants_datas = soup_datas.find_all(attrs={'class': 'row businessCapsule--mainRow'})

    for restaurants in restaurants_datas:
        restaurant_name = restaurants.find('span', 'businessCapsule--name')
        restaurants_class = restaurants.find('div', 'col-sm-24 businessCapsule--classStrap').find('a','businessCapsule--classification businessCapsule--link')
        restaurant_telp = restaurants.find('span', 'business--telephoneNumber')
        restaurant_web = restaurants.find('div', 'col-sm-24 businessCapsule--ctas').find('a', {
            'rel': 'nofollow noopener'})
        if not restaurant_web:
            restaurant_web = 'No Web'
        else:
            restaurant_web = restaurant_web['href']
        restaurant_str_addrs = restaurants.find('span', {'itemprop': 'streetAddress'})
        restaurant_addrs_local = restaurants.find('span', {'itemprop': 'addressLocality'})
        restaurant_pstl_code = restaurants.find('span', {'itemprop': 'postalCode'})
        restaurant_rating = restaurants.find('span', 'starRating--average')
        if not restaurant_rating:
            restaurant_rating = 'No Rating'
        else:
            restaurant_rating = restaurant_rating.text

        print('Data page: ', page_number)
        print('Name: ', restaurant_name.text)
        print('classification: ', restaurants_class.text)
        print('Telephone: ', restaurant_telp.text)
        print('Web: ', restaurant_web)
        print('streetAddress: ', restaurant_str_addrs.text)
        print('addressLocality: ', restaurant_addrs_local.text)
        print('postalCode: ', restaurant_pstl_code.text)
        print('Rating: ', restaurant_rating)


data = [
    {'name': 'aaa', 'age': '23', 'country': 'Indonesia'},
    {'name': 'bbb', 'age': '33', 'country': 'Indonesia'}
]

df = pd.DataFrame(data)
df.to_csv('results.csv', index=False)
df.to_excel('results.xlsx', index=False)




