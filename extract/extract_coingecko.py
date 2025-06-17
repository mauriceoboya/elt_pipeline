import requests
import pandas as pd
from datetime import datetime
import json

def extract_crypo_data():
    url="https://api.coingecko.com/api/v3/coins/markets"
    params={"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10}
    response=requests.get(url,params=params)
    data=response.json()

    df= pd.DataFrame(data)
    df['extracted_at']=datetime.now()
    return df

if __name__ == '__main__':
    df = extract_crypo_data()
    df.to_csv("crypto_data.csv", index=False)
    print("Data saved to crypto_data.csv")
