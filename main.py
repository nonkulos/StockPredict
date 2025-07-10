from dotenv import load_dotenv
from pathlib import Path
import os

def main():
    envPath = Path(".venv/.env")
    load_dotenv(dotenv_path=envPath)

    api_key = os.getenv('API_KEY')

main()