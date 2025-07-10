import csv
import requests

def reqSymbols(api_key):
    CSV_URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=' + api_key

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
    
    with open('output.csv', 'a', newline='') as csvfile:
        cw = csv.writer(csvfile)
        cw.writerows(my_list)

