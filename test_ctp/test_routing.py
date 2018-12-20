#!/usr/bin/env python

import QAPUBSUB
import threading

from QAPUBSUB.consumer import subscriber_routing
from QAPUBSUB.producer import publisher_routing




z1= subscriber_routing(exchange='xx',routing_key='x1')
z2 = subscriber_routing(exchange='xx',routing_key='x2')

z1.callback= lambda a,b,c,x: print('FROM X1 {}'.format(x))
z2.callback= lambda a,b,c,x: print('FROM X2 {}'.format(x))

p = publisher_routing(exchange='xx')


threading.Thread(target=z1.start).start()

threading.Thread(target=z2.start).start()

p.pub('xxxxx',routing_key='x1')

p.pub('xxxxx',routing_key='x2')

