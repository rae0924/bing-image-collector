# -*- coding: utf-8 -*-
import os
import json
from multiprocessing.dummy import Pool as ThreadPool
import itertools
import urllib.request


curr_dir = os.path.dirname(__file__)
data_dir = os.path.join(curr_dir, 'data')
image_links_file_path = os.path.join(curr_dir, 'image_links.json')

def download_images(workers=1):
    try:
        with open(image_links_file_path) as image_links_file:
            urls_dict =  json.load(image_links_file)
    except FileNotFoundError:
        print('image_links.json not found: execute fetch_links.py')
        return
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    for search_term in urls_dict.keys():
        save_dir = os.path.join(data_dir, search_term.replace(' ', '_'))
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        urls = urls_dict[search_term]
        thread_pool = ThreadPool(processes=workers)
        thread_pool.map(download, zip(urls, itertools.repeat(save_dir), range(len(urls))))
    
def download(args):
    url = args[0]
    save_dir = args[1]
    count = args[2]
    image_file_name = str(count) + '_' + os.path.basename(save_dir) + '.jpg'
    image_path = os.path.join(save_dir, image_file_name)
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError as err:
        print(f'HTTP Error: {err.msg}\n url: {url}')
        return
    except urllib.error.URLError as err:
        print(f'Urlopen Error: {err.reason}')
        return
    with open(image_path, 'wb') as image_file:
        image_file.write(response.read())

if __name__ =='__main__':
    download_images(workers=4)
