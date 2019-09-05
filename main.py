# coding: utf-8

import sys
from getprl import GetProxyList as getprl

def main():
    proxy = getprl.GetProxyList()
    proxy.parse_sslproxies()

if __name__ == '__main__': main()
