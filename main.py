# coding: utf-8

import click
import sys
from modules import GetProxyList as getprls
from modules import CheckConnectProxy as chkconpr

@click.group()
def subcommand():
    pass

@subcommand.command(help='プロキシ一覧を取得します')
def get_proxy():
    '''
    プロキシ接続を試みる
    '''
    proxy = getprls.GetProxyList()
    proxylist = proxy.parse_sslproxies()
    if len(proxylist) == 0:
        print('Empty list')
        return

    for list in proxylist:
        print(list)
        checkproxy = chkconpr.CheckConnectProxy()
        checkproxy.check_connect(list)

        #checkproxy = chkconpr.CheckConnectProxy()
        #checkproxy.proxy_connect(list)
        #return

def main():
    subcommand()

if __name__ == '__main__': main()
