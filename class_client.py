# -*- coding: utf-8 -*-

import socket
import json
import time
import threading


class Client:
    def __init__(self, conf):
        config = json.loads(open(conf, "r").read())
        self.server = config["server"]
        self.port = config["port"]
        self.sock = None

    def connect(self):
        while True:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.server, self.port))
                break
            except Exception as err:
                print err
                time.sleep(5)
        return 0

    def send(self, message):
        self.sock.send(message)

    def startth(self, target, args = (), daemon = False):
        th = threading.Thread(target = target, args = args)
        th.setDaemon(daemon)
        th.start()
        return th