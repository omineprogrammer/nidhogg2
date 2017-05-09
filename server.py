# -*- coding: utf-8 -*-

import class_server


def main():
    server = class_server.Server("server.conf")
    sock = server.mksocket()
    sw = True
    while sw:
        server.listen(sock)
        print server.clients.keys()


if __name__ == '__main__':
    main()
