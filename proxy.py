from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route('/api/offers')
def get_offers():
    url = "https://www.prospektangebote.de/angebote/tassimo"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    offers = []
    for item in soup.select('.offer-item'):
        produkt = item.select_one('.offer-title').get_text(strip=True) if item.select_one('.offer-title') else None
        preis = item.select_one('.offer-price').get_text(strip=True) if item.select_one('.offer-price') else None
        haendler = item.select_one('.offer-store').get_text(strip=True) if item.select_one('.offer-store') else None
        gueltig_bis = item.select_one('.offer-validity').get_text(strip=True) if item.select_one('.offer-validity') else None
        if produkt and preis:
            offers.append({
                'produkt': produkt,
                'preis': preis,
                'haendler': haendler,
                'gueltig_bis': gueltig_bis
            })
    return jsonify(offers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
