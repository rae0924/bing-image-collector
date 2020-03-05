import json
import requests
import time


endpoint = 'https://api.cognitive.microsoft.com/bing/v7.0/images/search'

class LinkFetcher(object):

    def __init__(self, api_key=''):
        self.api_key = api_key

    def set_api_key(self, api_key):
        self.api_key = api_key

    def fetch(self, search_terms, num=100, sleep=0.5):
        if self.api_key is '':
            raise Exception('API Key is empty, please use set_api_key()')
        headers = {'Ocp-Apim-Subscription-Key': self.api_key}
        urls_dict = {}
        for search_term in search_terms:
            urls_list = []
            offset = 0
            while offset < num:
                if offset + 150 <= 0:
                    count = 150
                else:
                    count = num - offset
                params = {'q': search_term, 'count': count, 'offset': offset}
                response = requests.get(endpoint, params, headers=headers)
                json_object = response.json()
                if response.status_code != 200:
                    raise Exception(f"{response.status_code} {response.reason}")
                for image_object in json_object['value']:
                    urls_list.append(image_object['contentUrl'])
                offset += 150
                # sleep to not pass request limits under Azure
                time.sleep(sleep)
            urls_dict.update({search_term: urls_list})
        return urls_dict

    



