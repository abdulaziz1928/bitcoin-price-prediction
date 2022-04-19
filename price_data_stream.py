import requests


def main():
    api_key="6dac7d551badb052ee4e75a160a8490332152641a48430d874ce368b55bb846d"
    url="https://min-api.cryptocompare.com/data/blockchain/histo/day?fsym=BTC&api_key="+api_key
    data = requests.get(url).json()["Data"]
    print(data)

main()
        
