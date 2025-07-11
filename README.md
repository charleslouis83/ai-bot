# AI Bot

This project aims to build an automated trading bot capable of interacting with cryptocurrency exchanges. It will leverage various data analysis libraries and exchange APIs to automate trading strategies.

## Prerequisites

- **Python 3.8+**
- **Git** to clone the repository

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-bot
   ```
2. **Create a Python virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Upgrade `pip` and install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   - `requests` – HTTP client for API calls
   - `pandas` – data manipulation
   - `ta` – technical analysis indicators
   - `flask` – optional web server for dashboards or API endpoints
   - `ccxt` – example exchange API library
These dependencies are listed in `requirements.txt`.

4. **Start developing your trading logic.** You can create Python scripts inside the repository and run them from your virtual environment.

## Example Usage

```bash
python your_script.py
```

The project currently contains only documentation; feel free to expand it with your own trading strategies and utilities.
