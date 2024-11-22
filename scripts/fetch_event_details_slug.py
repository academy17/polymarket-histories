import requests

def fetch_event_markets(slug):
    """Fetches event data from Polymarket and filters associated markets."""
    url = f"https://gamma-api.polymarket.com/events?slug={slug}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        event_data = response.json()

        if not event_data:
            print(f"No event found for slug: {slug}")
            return


        event_title = event_data[0].get("title", "Unknown Event")
        markets = event_data[0].get("markets", [])
        
        filtered_markets = [
            market for market in markets
            if market.get("active") and market.get("closed")
        ]

        print(f"Filtered Markets for '{event_title}' (Slug: {slug}):")
        for market in filtered_markets:
            print(f"- Market ID: {market['id']}")
            print(f"  Question: {market['question']}")
            print(f"  Volume: {market.get('volume', 'N/A')}")
            print(f"  Outcomes: {market.get('outcomes', 'N/A')}")
            print(f"  Outcome Prices: {market.get('outcomePrices', 'N/A')}")
            print()
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for slug '{slug}': {e}")

input_slug = input("Enter the Polymarket event slug (e.g. presidential-election-winner-2024): ").strip()
fetch_event_markets(input_slug)
