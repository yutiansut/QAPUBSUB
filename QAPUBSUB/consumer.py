
import pika
from QAPUBSUB.base import base_ps
from QAPUBSUB.setting import qapubsub_ip, qapubsub_port, qapubsub_user, qapubsub_password
import random


class subscriber(base_ps):
    """new version (pika 1.0+) client for sub/quantaxis IO BUS

    Arguments:
        base_ps {[type]} -- [description]
    """

    def __init__(self, host=qapubsub_ip, port=qapubsub_port, user=qapubsub_user, password=qapubsub_password, exchange='', queue='qa_sub.{}'.format(random.randint(0, 1000000)), routing_key='default'):
        super().__init__(host=host, port=port, user=user,
                         password=password, exchange=exchange)
        self.queue = queue
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type='fanout',
                                      passive=False,
                                      durable=False,
                                      auto_delete=False)
        self.routing_key = routing_key
        self.queue = self.channel.queue_declare(
            queue='', auto_delete=True, exclusive=True).method.queue
        self.channel.queue_bind(queue=self.queue, exchange=exchange,
                                routing_key='qa_routing')          # 队列名采用服务端分配的临时队列
        # self.channel.basic_qos(prefetch_count=1)

    def callback(self, chan, method_frame, _header_frame, body, userdata=None):
        print(1)
        print(" [x] %r" % body)

    def subscribe(self):
        self.channel.basic_consume(self.queue, self.callback, auto_ack=True)
        self.channel.start_consuming()
        # self.channel.basic_consume(
        #     self.callback, queue=self.queue_name, no_ack=True)  # 消息接收

    def start(self):
        try:
            self.subscribe()
        except Exception as e:
            print(e)
            self.start()


class subscriber_routing(base_ps):
    """new version (pika 1.0+) client for sub/quantaxis IO BUS

    Arguments:
        base_ps {[type]} -- [description]
    """

    def __init__(self, host=qapubsub_ip, port=qapubsub_port, user=qapubsub_user, password=qapubsub_password, exchange='', queue='qa_sub.{}'.format(random.randint(0, 1000000)), routing_key='default'):
        super().__init__(host=host, port=port, user=user,
                         password=password, exchange=exchange)
        self.queue = queue
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type='direct',
                                      passive=False,
                                      durable=False,
                                      auto_delete=False)
        self.routing_key = routing_key
        self.queue = self.channel.queue_declare(
            queue='', auto_delete=True, exclusive=True).method.queue
        self.channel.queue_bind(queue=self.queue, exchange=exchange,
                                routing_key=self.routing_key)          # 队列名采用服务端分配的临时队列
        # self.channel.basic_qos(prefetch_count=1)

    def callback(self, chan, method_frame, _header_frame, body, userdata=None):
        print(1)
        print(" [x] %r" % body)

    def subscribe(self):
        self.channel.basic_consume(self.queue, self.callback, auto_ack=True)
        self.channel.start_consuming()
        # self.channel.basic_consume(
        #     self.callback, queue=self.queue_name, no_ack=True)  # 消息接收

    def start(self):
        try:
            self.subscribe()
        except Exception as e:
            print(e)
            self.start()


class subscriber_topic(base_ps):
    """new version (pika 1.0+) client for sub/quantaxis IO BUS

    Arguments:
        base_ps {[type]} -- [description]
    """

    def __init__(self, host=qapubsub_ip, port=qapubsub_port, user=qapubsub_user, password=qapubsub_password, exchange='', queue='qa_sub.{}'.format(random.randint(0, 1000000)), routing_key='default'):
        super().__init__(host=host, port=port, user=user,
                         password=password, exchange=exchange)
        self.queue = queue
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type='topic',
                                      passive=False,
                                      durable=False,
                                      auto_delete=False)
        self.routing_key = routing_key
        self.queue = self.channel.queue_declare(
            queue='', auto_delete=True, exclusive=True).method.queue
        self.channel.queue_bind(queue=self.queue, exchange=exchange,
                                routing_key=self.routing_key)          # 队列名采用服务端分配的临时队列
        # self.channel.basic_qos(prefetch_count=1)

    def callback(self, chan, method_frame, _header_frame, body, userdata=None):
        print(1)
        print(" [x] %r" % body)

    def subscribe(self):
        self.channel.basic_consume(self.queue, self.callback, auto_ack=True)
        self.channel.start_consuming()
        # self.channel.basic_consume(
        #     self.callback, queue=self.queue_name, no_ack=True)  # 消息接收

    def start(self):
        try:
            self.subscribe()
        except Exception as e:
            print(e)
            self.start()
