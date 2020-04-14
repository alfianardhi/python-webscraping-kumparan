import requests
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kumparan-trends')
def getKumparanTrends():
    html_datas = requests.get('https://kumparan.com/trending')
    soup = BeautifulSoup(html_datas.text, 'html.parser')

    trend_news = soup.find(attrs={'class':'NewsCardContainerweb__Scroll-sc-1fei86o-2 cXaeCj'})
    titles = trend_news.find_all(attrs={'class':'TextBoxweb__StyledTextBox-n41hy7-0 jVPDss'})

    return render_template('index.html', titles = titles)

if __name__ == '__main__':
    app.run(debug=True)
