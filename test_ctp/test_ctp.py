from QAPUBSUB import consumer


c = consumer.subscriber(exchange='ctp')
c.callback = lambda x, y, body, z: print(z)
c.start()
