import json
import requests


URL = 'https://data-live.flightradar24.com/zones/fcgi/feed.js?bounds=42.00,41.95,-88.00,-87.95&faa=1&satellite=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=14400&gliders=1&stats=1&enc=CcXaDIKtFOXmcrZmMoBCKtK6rBeUs6vfYcYXPYV9zb8'


SPOOFED_USER_AGENT = ''


def enrich(data):
    return data


def main():
    data = requests.get(URL, headers={'user-agent': SPOOFED_USER_AGENT})
    print(json.dumps(enrich(data.json()), indent=2))


if __name__ == '__main__':
    main()
