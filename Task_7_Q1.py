import requests

class CountryInfo:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

    def display_countries_and_currencies(self, data):
        for country in data:
            country_name = country['name']['common']
            if 'currencies' in country:
                currencies = list(country['currencies'].keys())
                symbols = [currency_data['symbol'] for currency_data in country['currencies'].values() if 'symbol' in currency_data]
                print(f"Country: {country_name}, Currencies: {currencies}, Symbols: {symbols}")
            else:
                print(f"Country: {country_name}, Currencies: Not Available")

    def display_countries_by_currency(self, data, currency_name):
        countries = [country['name']['common'] for country in data if 'currencies' in country and currency_name in country['currencies']]
        print(f"Countries using {currency_name}: {countries}")

# Example usage:
url = "https://restcountries.com/v3.1/all"
country_info = CountryInfo(url)
data = country_info.fetch_data()

country_info.display_countries_and_currencies(data)
country_info.display_countries_by_currency(data, "USD")
country_info.display_countries_by_currency(data, "EUR")
