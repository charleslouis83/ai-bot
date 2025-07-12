import hashlib
from flask import Flask, jsonify, render_template
import feedparser
from newspaper import Article

app = Flask(__name__)
COINS = []

NEWS_FEED = 'https://news.google.com/rss'


def fetch_latest_news_image():
    feed = feedparser.parse(NEWS_FEED)
    if not feed.entries:
        return None
    entry = feed.entries[0]
    url = entry.link
    title = entry.title
    img_url = None
    try:
        article = Article(url)
        article.download()
        article.parse()
        img_url = article.top_image
    except Exception:
        pass
    return {
        'title': title,
        'url': url,
        'image': img_url or 'https://via.placeholder.com/150'
    }


def create_coin():
    news = fetch_latest_news_image()
    if not news:
        return None
    name = news['title'][:40]
    symbol = ''.join(word[0] for word in name.split() if word.isalnum()).upper()[:4]
    token_id = hashlib.sha256(name.encode('utf-8')).hexdigest()[:10]
    coin = {
        'name': name,
        'symbol': symbol or 'MC',
        'image': news['image'],
        'token_id': token_id,
        'article': news['url']
    }
    COINS.append(coin)
    return coin


@app.route('/')
def home():
    return render_template('index.html', coins=COINS)


@app.route('/create', methods=['POST'])
def create_route():
    coin = create_coin()
    if coin:
        return jsonify(coin)
    return jsonify({'error': 'Could not create coin'}), 500


@app.route('/coins')
def list_coins():
    return jsonify(COINS)


if __name__ == '__main__':
    app.run(debug=True)
