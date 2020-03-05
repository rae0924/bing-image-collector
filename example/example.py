from bing_image_collector.collector import BingImageCollector

api_key = ''

# recommend limiting the number of images to less than 900

collector = BingImageCollector()
collector.set_api_key(api_key)
search_terms = ['cat', 'dog', 'mouse', 'goldfish']
collector.collect(search_terms, workers=4, num=10, clear_root=True)