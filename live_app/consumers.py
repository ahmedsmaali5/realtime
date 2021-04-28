from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        for i in range(1000):
            context=json.dumps({'message':randint(1,100)})
            self.send(context)
            sleep(1)
