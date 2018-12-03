

import pika


class base_ps():

    def __init__(self, host='localhost', port=5672, user='guest', password='guest', channel_number=1, queue_name='', routing_key='default',  exchange='', exchange_type='fanout'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

        self.queue_name = queue_name
        self.exchange = exchange
        self.routing_key = routing_key
        self.exchange_type = exchange_type
        self.channel_number = channel_number
        # fixed: login with other user, pass failure @zhongjy
        credentials=pika.PlainCredentials(self.user, self.password, erase_on_connect=True)
        self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.host, port=self.port,
                    credentials=credentials, heartbeat_interval=0, socket_timeout=5,
                )
            )

        self.channel = self.connection.channel(
            channel_number=self.channel_number)

    def reconnect(self):
        try:
            self.connection.close()
        except:
            pass

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port,
                                      heartbeat_interval=0,
                                      socket_timeout=5,))

        self.channel = self.connection.channel(
            channel_number=self.channel_number)
        return self
