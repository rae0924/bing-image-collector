# bing-image-collector
A python package that makes it simple and easy to collect images from Bing Image Search API.

## Getting Started
This python package was developed to allow for programmers to easily extract images from Bing based on search terms using the 
[Microsoft Azure Bing Image Search API](https://docs.microsoft.com/en-us/rest/api/cognitiveservices-bingsearch/bing-images-api-v7-reference). Follow instructions below to use this package properly.

### Azure Bing Search
This package utilizes the Bing Image Search API to collect images from the Bing search engine. So you will need a Microsoft Azure account to access their services.

### Setup
Clone this repository to a preferable location:

`git clone https://github.com/rae0924/bing-image-collector.git`

Go into the cloned repository:

`cd bing-image-collector`

Install the package through pip:

`pip3 install -e .`


## Usage

### Command Line Interface
After installing, the easiest way to use this package is by running the python script cmdln.py which will take several command line arguments. Executing this script will automatically fetch results from bing and download the images into a folder. The script requires at least a single search term and must require a API key to work. For help, use:

```python3 ./cmdln.py -h```

which should print out the command line arguments and their descriptions:

```
usage: cmdln.py [-h] --api_key API_KEY [--num NUM] [--root_dir ROOT_DIR]
                [--workers WORKERS] [--sleep SLEEP] [--clear_root CLEAR_ROOT]
                search_terms [search_terms ...]
Fetch and download images from Bing

positional arguments:
  search_terms          list of terms to search on bing

optional arguments:
  -h, --help            show this help message and exit
  --api_key API_KEY     bing image search raw API key
  --num NUM             number of images
  --root_dir ROOT_DIR   root dir of images
  --workers WORKERS     number of worker threads
  --sleep SLEEP         seconds to sleep after requests
  --clear_root CLEAR_ROOT
                        clear the root dir before downloading
```
An example command:

```
python3 ./cmdln.py "apples" "bananas" "oranges" --api_key=*****
```
will result in those 3 fruit search terms to be requested on Bing Image Search API and the results will be extracted and downloaded into the default image folder called "data" that will have subfolders corresponding to each search term.

### Programmatically
You could also just import the package and use the `BingImageCollector` class in a python program to fetch and download images. Reference the example folder for how to use the class. Same arguments apply in here as in the command line.
