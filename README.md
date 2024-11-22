# Polymarket Histories

A collection of Python scripts to fetch timeseries and event details from Polymarket APIs.

## Features
- Fetch timeseries data for Polymarket markets.
- Fetch event details using Polymarket slugs.

## Repository Link
[Polymarket Histories Repository](https://github.com/academy17/polymarket-histories)

## Prerequisites
- Python 3.8 or higher
- A working internet connection

## Setup Instructions
**Clone the Repository**:
   ```bash
   git clone https://github.com/academy17/polymarket-histories.git
   cd polymarket-histories
```

**Set up a virtual environment** (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Install dependencies**:
```bash
pip install -r requirements.txt
```

Run the scripts:

**Fetch Event Details**:
```bash
python scripts/fetch_event_details_slug.py
```

**Fetch Timeseries Data**:
```bash
python scripts/fetch_timeseries_id.py
```



## Notes
If you choose not to use a virtual environment, ensure all dependencies listed in `requirements.txt` are installed globally:
```bash
pip install -r requirements.txt
```

The scripts will work if your system already has the required dependencies installed without explicitly activating a virtual environment.

## Example Usage

**Fetch Event Details**:
Run the `fetch_event_details_slug.py` script to fetch event details for a specific market slug:
```bash
python scripts/fetch_event_details_slug.py
```

Follow the prompts to enter the market slug and retrieve event details. You'll need the market id's to query the timeseries data.

**Fetch Timeseries Data**:
Run the `fetch_timeseries_id.py` script to fetch historical price data for a Polymarket market:
```bash
python scripts/fetch_timeseries_id.py
```

You will be prompted to enter the number of markets, provide the market ID(s), specify the data interval (e.g., 1d, 1w, 1h, max), and provide the fidelity in minutes (e.g., 1440 for daily data).

