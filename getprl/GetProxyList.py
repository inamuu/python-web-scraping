# coding: utf-8

import re
import requests
from bs4 import BeautifulSoup

class GetProxyList:
    def parse_sslproxies(self):
        proxy_count = 1
        try:
            r = requests.get("https://www.sslproxies.org")
            soup = BeautifulSoup(r.content, "html.parser")
            tbody = soup.find('tbody').findAll('tr')
        except Exception as e:
            print(e)
        else:
            proxylist = [] 
            for rows in tbody:
                ipaddr = rows.find('td').string
                port = rows.td.next_sibling.string
                proxylist.append([ipaddr, port])
            return proxylist
