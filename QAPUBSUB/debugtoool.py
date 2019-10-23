import click
from QAPUBSUB.consumer import subscriber, subscriber_routing, subscriber_topic
from QAPUBSUB.producer import publisher, publisher_routing, publisher_topic


@click.command()
@click.option('--exchange')
@click.option('--model', default='fanout')
@click.option('--routing_key', default='None')
@click.option('--user', default='admin')
@click.option('--password', default='admin')
@click.option('--host', default='127.0.0.1')
@click.option('--durable', default=False)
def debug_sub(exchange, model, routing_key, user, password, host, durable):
    if model == 'fanout':
        subscriber(host=host, user=user, password=password,
                   exchange=exchange).start()
    elif model == 'direct':
        subscriber_routing(host=host, user=user, password=password,
                           exchange=exchange, routing_key=routing_key, durable=durable).start()
    elif model == 'topic':
        subscriber_topic(host=host, user=user, password=password,
                         exchange=exchange, routing_key=routing_key, durable=durable).start()


@click.command()
@click.option('--exchange')
@click.option('--model', default='fanout')
@click.option('--routing_key', default='None')
@click.option('--user', default='admin')
@click.option('--password', default='admin')
@click.option('--host', default='127.0.0.1')
@click.option('--content', default='hello')
def debug_pub(exchange, model, routing_key, user, password, host, content):
    if model == 'fanout':
        publisher(host=host, user=user, password=password,
                  exchange=exchange).pub(content)
    elif model == 'direct':
        print(routing_key)
        publisher_routing(host=host, user=user, password=password,
                          exchange=exchange, routing_key=routing_key).pub(content, routing_key=routing_key)
    elif model == 'topic':
        publisher_topic(host=host, user=user, password=password,
                        exchange=exchange, routing_key=routing_key).pub(content, routing_key=routing_key)
