# coding: utf-8

import re
import requests
from bs4 import BeautifulSoup

class CheckConnectProxy:
    def check_connect(self, proxylist):
        print(proxylist[0])