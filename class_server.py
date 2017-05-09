# -*- coding: utf-8 -*-

import socket
import json


class Server:
    def __init__(self, conf):
        config = json.loads(open(conf, "r").read())
        self.port = config["port"]
        self.maxconn = config["maxconn"]
        self.sock = None
        self.clients = {}

    def mksocket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("", self.port))
        sock.listen(self.maxconn)
        return sock

    def listen(self):
        temp = self.sock.accept()
        client = {"ip": temp[1][0], "socket": temp[0]}
        self.clients[temp[1][1]] = client

    def addclient(self, client):
        self.clients[client[0]] = client[1]
