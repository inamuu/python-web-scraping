# coding: utf-8

import requests
import urllib
from socket import *

class CheckConnectProxy:
    def check_connect(self, proxylist):
        ipaddr = proxylist[0]
        port   = proxylist[1]

        print('check connection -> https://' + ipaddr + ':' + port)
        proxy = urllib.request.ProxyHandler(
                {
                    'https': 'https://' + ipaddr + ":" + port
                }
            )

        '''
        プロキシ接続したあとのIPアドレスを取得する
        '''
        goodproxylist = []
        try:
            opener = urllib.request.build_opener(proxy)
            urllib.request.install_opener(opener)
            proxyipdata = urllib.request.urlopen('https://ifconfig.me', timeout=2)
            proxyip = proxyipdata.read().decode()
            print('connect proxy: ' + proxyip + '\n')
            goodproxylist.append(ipaddr, port)
            proxyipdata.close()
        except:
            print('timeout: ' + ipaddr + '\n')

