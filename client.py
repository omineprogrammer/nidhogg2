# -*- coding: utf-8 -*-

import class_client


def main():
    client = class_client.Client("client.conf")
    client.connect()
    client.send("hola")
    pass


if __name__ == '__main__':
    main()
