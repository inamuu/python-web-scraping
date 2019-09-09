# coding: utf-8

import click
import sys
from getprl import GetProxyList as getprl

@click.group()
def subcommand():
    pass

@subcommand.command(help='プロキシ一覧を取得します')
def get_proxy_list():
    proxy = getprl.GetProxyList()
    proxy.parse_sslproxies()

if __name__ == '__main__': main()
