import requests

def list_breweries_by_state(state):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_state={state}")
    breweries = response.json()
    print(f"Breweries in {state}: {[brewery['name'] for brewery in breweries]}")
    print(f"Count of breweries in {state}: {len(breweries)}")
    
    city_brewery_count = {}
    for brewery in breweries:
        city = brewery['city']
        if city in city_brewery_count:
            city_brewery_count[city] += 1
        else:
            city_brewery_count[city] = 1
    print(f"Breweries per city in {state}: {city_brewery_count}")
    
    has_website_count = sum(1 for brewery in breweries if brewery['website_url'])
    print(f"Breweries with websites in {state}: {has_website_count}")

# Example usage for Alaska, Maine, New York:
list_breweries_by_state("Alaska")
list_breweries_by_state("Maine")
list_breweries_by_state("New York")
