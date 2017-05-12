# -*- coding: utf-8 -*-

import socket
import json
import threading
import time


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

    def listen(self, sw = True):
        while sw:
            temp = self.sock.accept()
            self.clients[temp[1][1]] = {"ip": temp[1][0], "socket": temp[0]}

            print temp[0].recv(10240)
            print self.clients.keys()

    # def send(self, message, socket):
    #     socket.send(message)

    def depure(self, rate = 10, sw = True):
        while sw:
            for client in self.clients.keys():
                try:
                    client["socket"].send("<PING>")
                except:
                    del self.clients[client]
            time.sleep(rate)
            print self.clients

    def startth(self, target, args = (), daemon = False):
        th = threading.Thread(target = target, args = args)
        th.setDaemon(daemon)
        th.start()
        return th