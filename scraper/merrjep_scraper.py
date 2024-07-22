from bs4 import BeautifulSoup
from pathlib import Path
import requests
import json


def mj_listing_scraper(nr_pages):
    """Scrape a nr of real estate pages from merrjep and
    return an html code with all listings"""

    all_listings = []

    for i in range(1, nr_pages + 1):
        response = requests.get(
            f"https://www.merrjep.al/njoftime/imobiliare-vendbanime/shtepi/tirane?Page={i}"
        ).text

        soup = BeautifulSoup(response, 'lxml')

        # Extract listings.
        scraper_njoftime_colored = soup.find_all('div', class_='new row row-listing colored')
        scraper_njoftime = soup.find_all('div', class_='new row row-listing')
        
        all_listings.extend(scraper_njoftime_colored)
        all_listings.extend(scraper_njoftime)

    return all_listings
    

def partial_url_extract(scraper_njoftime):
    """Extract url for each listing."""
    liste_njoftime = []

    for njoftim in scraper_njoftime:
        header = njoftim.find('h2')
        link = header.find('a')
        url = link.get('href')
        liste_njoftime.append(url)
    
    return liste_njoftime


def njoftime_url(liste_njoftime):
    """Build a full url from partial listings urls."""
    mj_main_url = 'https://www.merrjep.al'
    mj_njoftime_url = []

    for url in liste_njoftime:
        mj_njoftim_url = mj_main_url + url
        mj_njoftime_url.append(mj_njoftim_url)
    
    return mj_njoftime_url  


def extract_data_njoftime_url(njoftime_url):
    """Extract link, date, price, currency and other elements."""
    te_dhena_totale = []

    for link in njoftime_url:
        response = requests.get(link).text
        soup = BeautifulSoup(response, 'lxml')

        te_dhena = {}

        # Extract link.
        te_dhena['Link'] = link

        # Extract daten.
        try:
            date_elements = soup.find('bdi', class_='published-date')
            data = date_elements.get_text()
        except AttributeError:
            print(f"Listing has no published date: {link}")

        te_dhena['Data e Publikimit'] = data

        # Extract cmimin dhe valuten, dhe append te data dictionary.
        try:
            price_elements = soup.find('bdi', class_='new-price')
            value_tags = price_elements.find('span', class_='format-money-int')
        except AttributeError:
            print(f"Listing has no price data: {link}")

        try:
            cmimi = value_tags.get('value')
            valuta = value_tags.find_next_sibling('span').get_text(strip=True)

            te_dhena['Cmimi'] = cmimi
            te_dhena['Valuta'] = valuta
        except UnboundLocalError:
            print(f"Listing has no price data: {link}")

        # Extract te dhena te tjera per njoftimin.
        a_tags = soup.find_all('a', class_='tag-item')

        for a_tag in a_tags:
            span_tag = a_tag.find('span')
            bdi_tag = a_tag.find('bdi')
            if span_tag and bdi_tag:
                span_text = span_tag.get_text(strip=True)
                bdi_text = bdi_tag.get_text(strip=True)
                te_dhena[span_text] = bdi_text
            
        te_dhena_totale.append(te_dhena)
    
    return te_dhena_totale

# Start scraper
scraper_njoftime = mj_listing_scraper(100)
liste_njoftime = partial_url_extract(scraper_njoftime)
njoftime_url = njoftime_url(liste_njoftime)
te_dhena = extract_data_njoftime_url(njoftime_url)


print(len(te_dhena))

# Write to json file
path = Path('njoftime.json')
contents = json.dumps(te_dhena)
path.write_text(contents)


