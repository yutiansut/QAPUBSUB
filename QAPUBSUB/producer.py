#!/usr/bin/env python 3
import pika
import QUANTAXIS as QA
from QAPUBSUB.base import base_ps
#########  生产者 #########
# 链接rabbit服务器（localhost是本机，如果是其他服务器请修改为ip地址）


class publisher(base_ps):
    def __init__(self, host='localhost', port=5672, user='guest', password='guest', channel_number=1, queue_name='', routing_key='default',  exchange='', exchange_type='fanout'):
        super().__init__(host, port, user, password, channel_number,
                         queue_name, routing_key,  exchange, exchange_type)
        self.channel.queue_declare(self.queue_name)
        self.channel.exchange_declare(self.exchange, self.exchange_type)

    def pub(self, text):
        # channel.basic_publish向队列中发送信息
        # exchange -- 它使我们能够确切地指定消息应该到哪个队列去。
        # routing_key 指定向哪个队列中发送消息
        # body是要插入的内容, 字符串格式
        if isinstance(text, bytes):
            pass
        elif isinstance(text, str):
            text = bytes(text, encoding='utf-8')
        try:
            self.channel.basic_publish(exchange=self.exchange,
                                       routing_key='testa',
                                       body=text)
        except Exception as e:
            print(e)
            self.reconnect().channel.basic_publish(exchange=self.exchange,
                                                   routing_key='testa',
                                                   body=text)

    def exit(self):
        self.connection.close()





if __name__ == '__main__':
    import datetime
    p = publisher(exchange='z')
    while True:
        p.pub('{}'.format(datetime.datetime.now()))
