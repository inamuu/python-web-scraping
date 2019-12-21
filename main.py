# coding: utf-8

import click
import sys
from modules import GetProxyList as getprls

@click.group()
def subcommand():
    pass

@subcommand.command(help='プロキシ一覧を取得します')
def get_proxy_list(proxynum):
    """
    プロキシリストを取得
    """
    try:
        instance = conpr.ConProxy()
        proxylist = instance.parse_sslproxies()
        if len(proxylist) == 0:
            print('Empty list')
            return

        """
        取得したプロキシから良質なプロキシリストを生成
        """
        goodproxylist = []
        for list in proxylist:
            result = instance.check_connect(list)
            if result is True:
                print(list[0] + ':' + list[1] + ' -> OK\n')
                goodproxylist.append(list)
            if len(goodproxylist) >= int(proxynum):
                break

        print('Number of good proxy: ' + str(len(goodproxylist)))
        if len(goodproxylist) < 2:
            """
            良質なプロキシが0の場合はsleepして再度リスト取得を試みる。
            1台だけだと繰り返し実行時に同じサーバーになってしまうので、2台取得できるまでリトライする。
            """
            print('retry get_proxy_list until get proxy list more than 2 servers')
            time.sleep(5)
        return goodproxylist
    except:
        raise


def main():
    subcommand()

if __name__ == '__main__': main()

