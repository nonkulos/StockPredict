import csv
import requests
from datetime import datetime, timedelta

def reqSymbols(api_key):
    CSV_URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=' + api_key
    symbols = []

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
    
    for i in my_list:
        symbols.append(i[0])

    return symbols

def createCSV(api_key, symbol, csv_path):
    # make call to api
    data = []
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=' + symbol + '&datatype=csv&apikey=' + api_key
    res = requests.get(CSV_URL)
    decode = res.content.decode('utf-8')
    reader = csv.reader(decode.splitlines(), delimiter=',')
    next(reader)

    for row in reader:
        row.append(symbol)
        try: 
            dt = datetime.strptime(row[0], '%Y-%m-%d')
            epoch_time_days = (dt - datetime(1985, 1, 1)) / timedelta(days=1)
            row[0] = epoch_time_days
        except ValueError:
            print("gayus momentous")
        except Exception:
            pass
        data.append(row)
    
    with open(csv_path, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)