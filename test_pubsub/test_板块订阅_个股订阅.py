#!/usr/bin/env python

import QAPUBSUB
import threading

from QAPUBSUB.consumer import subscriber_topic
from QAPUBSUB.producer import publisher_topic


z1 = subscriber_topic(exchange='testTopic', routing_key='000001.#')
z2 = subscriber_topic(exchange='testTopic', routing_key='#.000300.#')
z2.add_sub(exchange='testTopic', routing_key='#.000050.#')
z3 = subscriber_topic(exchange='testTopic', routing_key='#.SZ.#')


z1.callback = lambda a, b, c, x: print('FROM 个股订阅 000001 {}'.format(x))
z2.callback = lambda a, b, c, x: print('FROM 板块订阅/ 沪深300/ 上证50 {}'.format(x))
z3.callback = lambda a, b, c, x: print('FROM 市场订阅/深圳市场 {}'.format(x))
p = publisher_topic(exchange='testTopic', )


threading.Thread(target=z1.start).start()

threading.Thread(target=z2.start).start()
threading.Thread(target=z3.start).start()


p.pub('000001', routing_key='000001.SZ.000300.000050')

p.pub('000002', routing_key='000002.SZ.000300.000050')
p.pub('601318', routing_key='601318.SH.000300.000050')
"""
在exchange为 xx的mq中


routing_key = x1 ==>  有一个订阅者 z1
routing_key = x2 ==>  有两个订阅者 z2, z3

"""
