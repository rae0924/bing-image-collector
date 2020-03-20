import os
from multiprocessing.dummy import Pool as ThreadPool
import socket
import itertools
import urllib.request
import array


class ImageDownloader(object):

    def __init__(self, root_dir='./data', workers=1):
        self.workers = 1
        self.root_dir = root_dir

    def download_images(self, urls_dict):
        if not os.path.exists(self.root_dir):
            os.mkdir(self.root_dir)
        thread_pool = ThreadPool(self.workers)
        for search_term in urls_dict:
            urls = urls_dict[search_term]
            save_dir = os.path.join(self.root_dir, search_term.replace(' ', '_'))
            if not os.path.exists(save_dir):
                os.mkdir(save_dir)
            thread_pool.map(self.download, zip(urls, itertools.repeat(save_dir), range(len(urls))))
            
    def download(self, args):
        url = args[0]
        save_dir = args[1]
        count = args[2]
        image_file_name = str(count) + '_' + os.path.basename(save_dir) + '.jpg'
        image_path = os.path.join(save_dir, image_file_name)
        try:
            response = urllib.request.urlopen(url, timeout=15)
        except urllib.error.HTTPError as err:
            print(f'HTTP Error: {err.reason}\n url: {url}')
            return
        except urllib.error.URLError as err:
            print(f'Urlopen Error: {err.reason}\n url: {url}')
            return
        except socket.timeout as err:
            print(f'Socket Timeout: Response took more than 15 seconds \n url: {url}')
            return
        with open(image_path, 'wb') as image_file:
            image_file.write(response.read())
        

