import os
import re

import urllib
import requests
class image_crawller:
    def __init__(self,save_dirpath,start_page,maximum_download):
        self.save_dirpath=save_dirpath
        self.crawl_url_list=[start_page]
        self.stocked_url=set()
        self.maximum_download=maximum_download
        self.download_counter=0
