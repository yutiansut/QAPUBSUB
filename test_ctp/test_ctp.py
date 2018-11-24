from QAPUBSUB import consumer


c= consumer.consumer(exchange='ctp')
c.callback = lambda x,y,body,z: print(z)
while True:
    c.consum()