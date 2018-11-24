
import pika
from QAPUBSUB.base import base_ps


class consumer(base_ps):
    def __init__(self, host='localhost', port=5672, user='guest', password='guest', exchange=''):
        super().__init__(host=host, port=port, user=user,
                         password=password, exchange=exchange)
        self.result = self.channel.queue_declare(exclusive=True)
        self.queue_name = self.result.method.queue            # 队列名采用服务端分配的临时队列
        self.channel.queue_bind(exchange=exchange, queue=self.queue_name)

    def callback(self, method, properties, body, *args, **kwargs):
        print(" [x] %r" % body)

    def consum(self):

        self.channel.basic_consume(
            self.callback, queue=self.queue_name, no_ack=True)  # 消息接收
        self.channel.start_consuming()


if __name__ == '__main__':
    c = consumer(exchange='z')
    while True:
        c.consum()
