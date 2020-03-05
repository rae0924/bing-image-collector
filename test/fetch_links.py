import requests
import json
import os
import math
import time

curr_dir = os.path.dirname(__file__)
key_file_path = os.path.join(curr_dir, 'key.json')
image_links_file_path = os.path.join(curr_dir, 'image_links.json')
url = 'https://api.cognitive.microsoft.com/bing/v7.0/images/search'

def fetch_links(search_terms=[], count=100):
    
    try:
        with open(file=key_file_path, mode='r') as key_file:
    	    key_object = json.load(key_file)
    	    api_key = key_object['api_key']
    except FileNotFoundError:
        print('key.json file no found: please create the file')
    except KeyError:
        print('key error: key.json file has wrong keys')
    
    headers = {'Ocp-Apim-Subscription-Key': api_key}

    urls_dict = {}
    for search_term in search_terms:
        url_list = []
        offset = 0
        while offset < count: 
            if offset + 150 <= count:
                ct = 150
            else:
                ct = count - offset
            params = {'q': search_term, 'count': ct, 'offset': offset}
            print(params)
            response = requests.get(url, params, headers=headers)
            json_object = response.json()
            for image_object in json_object['value']:
                url_list.append(image_object['contentUrl'])
            offset += 150  
            # sleep to not pass 3 transactions per second  
            time.sleep(0.5)
        urls_dict.update({search_term: url_list})
    
    if not len(urls_dict) == 0:
        with open(image_links_file_path, 'w') as image_links_file:
            json.dump(urls_dict, image_links_file)

if __name__ == '__main__':
    search_terms = ['mark zuckerberg']
    count = 500
    fetch_links(search_terms, count)
