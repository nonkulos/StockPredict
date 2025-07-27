from dotenv import load_dotenv
from pathlib import Path
from apicalls import *

import os
import csv

def main():
    envPath = Path(".venv/.env")
    load_dotenv(dotenv_path=envPath)

    api_key = os.getenv('API_KEY')

    symbolList = reqSymbols(api_key)

    csv_path = "data.csv"
    with open(csv_path, "w", newline='') as file:
        fieldnames = ["timestamp", "open", "high", "low", "close", "adjusted close", "volume", "dividend amount", "symbol"]
        writehead = csv.DictWriter(file, fieldnames=fieldnames)
        writehead.writeheader()
    
    for i in range(1, len(symbolList)):
        createCSV(api_key, symbolList[i], csv_path)

    

main()