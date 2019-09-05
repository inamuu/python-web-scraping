# coding: utf-8

import re
import requests
from bs4 import BeautifulSoup

class GetProxyList:
    def parse_sslproxies(self):
        try:
            r = requests.get("https://www.sslproxies.org")
            soup = BeautifulSoup(r.content, "html.parser")
            tbody = soup.find('tbody').find_all('td')
        except Exception as e:
            print(e)
        else:
            for rows in tbody:
                rtext = rows.string
                ipaddr = re.match('(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])', rtext)
                if ipaddr is not None:
                    print('ipaddr: %s' % format(ipaddr.group(0)))
                port = re.match('\d{4,5}', rtext)
                if port is not None:
                    print('port: %s' % format(port.group(0)))

#proxy = GetProxyList()
#proxy.parse_sslproxies()
