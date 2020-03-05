from bing_image_collector import ImageDownloader, LinkFetcher
import shutil

class BingImageCollector(object):

    def __init__(self, api_key=''):
        self.api_key = api_key
        self.fetcher = None
        self.downloader = None

    def set_api_key(self, api_key):
        self.api_key = api_key

    def collect(self, 
        search_terms,           # list of search terms
        api_key='',             # in case they wanted to pass key through here
        root_dir='./data',      # the root directory to store downloaded images
        num=100,                # number of images to grab
        workers=1,              # number of threads to boost i/o speed
        sleep=0.5,              # seconds to sleep between requests
        clear_root=False        # clears root directory before process
        ):
        
        print(clear_root)
        if clear_root:
            shutil.rmtree(root_dir)

        self.api_key = api_key

        if self.api_key is '':
            raise Exception('API Key is empty, please use set_api_key()')
        
        self.fetcher = LinkFetcher(api_key=self.api_key)
        urls_dict = self.fetcher.fetch(search_terms, num, sleep)
        self.downloader = ImageDownloader(root_dir, workers)
        self.downloader.download_images(urls_dict)









    