from QAPUBSUB import producer

import json

c = producer.publisher_routing(exchange='qamdgateway', host='192.168.2.117', durable=True)

c.pub(json.dumps({'account_cookie': 'aa', 'code': '000001'}), routing_key='All')
