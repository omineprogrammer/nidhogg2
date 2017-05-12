# -*- coding: utf-8 -*-

import class_server


def main():
    server = class_server.Server("server.conf")
    server.mksocket()
    server.startth(server.listen)
    server.startth(server.depure)


if __name__ == '__main__':
    main()
