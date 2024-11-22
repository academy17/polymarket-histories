import requests
from datetime import datetime

def fetch_market_details(market_id):
    """Fetches market details to retrieve clobTokenIds."""
    url = f"https://gamma-api.polymarket.com/markets/{market_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching details for market {market_id}: {e}")
        return None

def fetch_timeseries(clob_token_id, interval, fidelity):
    """Fetches timeseries data for a given clobTokenId using interval and fidelity."""
    url = "https://clob.polymarket.com/prices-history"
    params = {
        "market": clob_token_id,
        "interval": interval,
        "fidelity": fidelity,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get("history", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching timeseries data for token {clob_token_id}: {e}")
        return []

def main():
    print("Fetch Timeseries Data by ID.")

    num_markets = int(input("How many markets to fetch timeseries data for? ").strip())

    market_ids = []
    for i in range(num_markets):
        market_id = input(f"Enter the market ID for market {i + 1}: ").strip()
        market_ids.append(market_id)

    interval = input("Enter the interval (e.g., 1d, 1w, 1h, max): ").strip()
    fidelity = int(input("Enter the fidelity in minutes (e.g., 1440 for daily): ").strip())

    for market_id in market_ids:
        print(f"\nFetching details for market ID: {market_id}")
        market_details = fetch_market_details(market_id)

        if not market_details:
            print(f"Failed to fetch details for market ID {market_id}. Skipping...")
            continue

        clob_token_ids = eval(market_details.get("clobTokenIds", "[]"))
        if not clob_token_ids:
            print(f"Missing clobTokenIds for market ID {market_id}. Skipping...")
            continue

        first_clob_token_id = clob_token_ids[0]
        print(f"Using first clobTokenId (YES Token): {first_clob_token_id}")

        timeseries_data = fetch_timeseries(
            clob_token_id=first_clob_token_id,
            interval=interval,
            fidelity=fidelity
        )

        if timeseries_data:
            print(f"Timeseries Data for Token ID {first_clob_token_id}:")
            for point in timeseries_data:
                print(f"Time: {point['t']}, Price: {point['p']}")
        else:
            print(f"No timeseries data found for token ID {first_clob_token_id}.")

if __name__ == "__main__":
    main()
