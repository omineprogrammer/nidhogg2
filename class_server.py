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
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("", self.port))
        self.sock.listen(self.maxconn)

    def listen(self):
        temp = self.sock.accept()
        self.clients[temp[1][1]] = {"ip": temp[1][0], "socket": temp[0]}

    def addclient(self, client):
        self.clients[client[0]] = client[1]
