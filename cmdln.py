import argparse
from bing_image_collector.collector import BingImageCollector


parser = argparse.ArgumentParser(description='Fetch and download images from Bing')
parser.add_argument('search_terms', nargs='+', help='list of terms to search on bing')
parser.add_argument('--api_key', help='bing image search raw API key', required=True)
parser.add_argument('--num', help='number of images', default=100)
parser.add_argument('--root_dir', help='root dir of images', default='./data')
parser.add_argument('--workers', help='number of worker threads', default=4)
parser.add_argument('--sleep', help='seconds to sleep after requests', default=0.5)
parser.add_argument('--clear_root', help='clear the root dir before downloading', default=False)

if __name__ == "__main__":
    args = parser.parse_args()
    collector = BingImageCollector()
    collector.collect(**vars(args))
