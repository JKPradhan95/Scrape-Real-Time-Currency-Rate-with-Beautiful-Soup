import requests
from bs4 import BeautifulSoup

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  

        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        rate_element = soup.find("span", class_="ccOutputRslt")
        if not rate_element:
            raise ValueError("Could not find the exchange rate on the page.")

        rate_text = rate_element.get_text()
        rate = float(rate_text[:-4])

        return rate

    except requests.RequestException as e:
        print(f"An error occurred while fetching the data: {e}")
    except ValueError as ve:
        print(f"An error occurred while processing the data: {ve}")

current_rate = get_currency('EUR', 'AUD')
if current_rate:
    print(current_rate)
