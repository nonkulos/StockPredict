from dotenv import load_dotenv
from pathlib import Path
from apicalls import reqSymbols

import os

def main():
    envPath = Path(".venv/.env")
    load_dotenv(dotenv_path=envPath)

    api_key = os.getenv('API_KEY')
    reqSymbols(api_key)

main()