import configparser
import os
import requests

def shorten(uri):
    config = configparser.ConfigParser()
    #config.read(os.path.join(os.path.expanduser('~'), 'api.cfg'))
    config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'api.cfg'))

    query_params = {
        'access_token': bitly_config['bitly']['access_token'],
        'longUrl': uri
    }

    endpoint = 'https://api-ssl.bitly.com/v3/shorten'
    response = requests.get(endpoint, params=query_params, verify=False)

    data = response.json()

    if data['status_code'] != 200:
        exit(
            f"Unexpected status_code: {data['status_code']} in bitly response. {response.text}"
        )
    return data['data']['url']

print(shorten("http://code-maven.com/"))

